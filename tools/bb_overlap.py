"""Find overlapping or overflowing content on the brand kit pages, at desktop (1440) and phone (390) widths."""
import pathlib, sys, json
sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/technext-presentations/scripts"))
from _cdp import serve, Chrome  # noqa: E402

R = pathlib.Path.home() / "ClaudeWork/brand-presentations"
pages = sys.argv[1:] or ["index", "technext", "hummingbeing", "bhdasia", "tre-singapore"]
JS = r"""
(() => {
  const out = [];
  const vis = el => { const s = getComputedStyle(el); return s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity !== 0; };
  const name = el => (el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).join('.') : '')) + ' "' + (el.textContent || el.alt || '').trim().replace(/\s+/g, ' ').slice(0, 40) + '"';
  // leaf boxes: elements with direct text, plus images
  const leaves = [...document.querySelectorAll('main *, .hero *')].filter(el => vis(el) && (el.tagName === 'IMG' || [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())));
  const boxes = leaves.map(el => {
    if (el.tagName === 'IMG') return { el, r: el.getBoundingClientRect() };
    const rg = document.createRange(); rg.selectNodeContents(el); return { el, r: rg.getBoundingClientRect() };
  }).filter(b => b.r.width > 2 && b.r.height > 2);
  for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
    const a = boxes[i], b = boxes[j];
    if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
    if (a.el.closest('.lg-stage, .dn-v, .file-v, .kc-v, .hero-card, .tre-field, .lb, svg') || b.el.closest('.lg-stage, .dn-v, .file-v, .kc-v, .hero-card, .tre-field, .lb, svg')) continue;
    const x = Math.min(a.r.right, b.r.right) - Math.max(a.r.left, b.r.left), y = Math.min(a.r.bottom, b.r.bottom) - Math.max(a.r.top, b.r.top);
    if (x > 3 && y > 3) out.push('OVERLAP ' + name(a.el) + ' x ' + name(b.el) + ' @' + Math.round(a.r.top + scrollY));
  }
  // text spilling out of a clipping or bordered box
  for (const el of document.querySelectorAll('main td, main th, main .card, main .sw, main .file, main .dn, main .ts, main .kc, main .ez')) {
    if (el.scrollWidth > el.clientWidth + 2) out.push('SPILL-X ' + name(el) + ' ' + el.scrollWidth + '>' + el.clientWidth + ' @' + Math.round(el.getBoundingClientRect().top + scrollY));
  }
  for (const el of document.querySelectorAll('main *')) {
    const s = getComputedStyle(el);
    if ((s.overflow === 'hidden' || s.textOverflow === 'ellipsis') && el.scrollWidth > el.clientWidth + 2 && el.textContent.trim() && !el.closest('.lg-stage, .dn-v, .strip, .ratio, .pic')) out.push('CLIPPED ' + name(el) + ' ' + el.scrollWidth + '>' + el.clientWidth);
  }
  return [...new Set(out)];
})()
"""
with serve(R) as base:
    for w, h, tag in [(1440, 900, "desktop"), (390, 844, "phone")]:
        with Chrome(w=w, h=h, mobile=(tag == "phone")) as c:
            for p in pages:
                c.open(base + p + ".html", settle=.8); c.images_loaded()
                res = c.ev(JS)
                print(f"== {p} {tag}: {len(res)} issue(s)")
                for r in res[:40]:
                    print("  ", r)
