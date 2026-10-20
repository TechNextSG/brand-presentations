# -*- coding: utf-8 -*-
"""Brand kits as plain HTML pages (TechNext branding): index.html + one scrolling page per brand, from kit_data.py.
Run: python -B _src/build.py"""
import html as _h
import io
import json
import pathlib
import re
import sys

import segno

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
sys.path.insert(0, str(SRC))
import kit_data as KD  # noqa: E402
import kit_update  # noqa: E402,F401  (15 Oct live check: corrections + detail)

ICONS = json.loads((SRC / "icons.json").read_text(encoding="utf-8"))
V = "13"
ORDER = ["technext", "hummingbeing", "bhdasia", "tre-singapore"]
QR = {"technext": "https://technext.asia/", "hummingbeing": "https://hummingbeing.com/", "bhdasia": "https://bhdasia.com/", "tre": "https://tre-in-singapore.com/"}
SECTIONS = [("basics", "Basics"), ("web", "Web identity"), ("logo", "Logo"), ("colour", "Colour"), ("type", "Typography"), ("ui", "UI tokens"),
            ("a11y", "Accessibility"), ("imagery", "Imagery"), ("formats", "Formats and templates"), ("wording", "Voice and wording"),
            ("rules", "Do's and don'ts"), ("masters", "Masters and open items"), ("materials", "All materials")]


def e(s):
    return _h.escape(s, quote=True)


def icon(n):
    return ICONS[n]


def qr(key, dark):
    q = segno.make(QR[key], error="m"); b = io.BytesIO()
    q.save(b, kind="svg", scale=1, border=0, dark=dark, light=None, xmldecl=False, svgns=True, nl=False, svgclass="qr", omitsize=True)
    return b.getvalue().decode("utf-8")


def dl(path, label="PNG"):
    return f'<a class="dl" href="{path}" download="{path.rsplit("/", 1)[-1]}">{icon("file")}{label}</a>'


def head(title, desc):
    return f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<meta name="color-scheme" content="light">
<meta name="theme-color" content="#1E4691">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" type="image/png" sizes="48x48" href="assets/img/favicon-48.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="stylesheet" href="assets/fonts.css?v={V}">
<link rel="stylesheet" href="assets/kit.css?v={V}">
<link rel="stylesheet" href="assets/b-specimens.css?v={V}">
</head>"""


def topbar(cur):
    links = "".join(f'<a href="{s}.html"{" aria-current=\"page\"" if s == cur else ""}>{e(KD.BRANDS[s]["name"])}</a>' for s in ORDER)
    return f"""<header class="top"><div class="wrap top-in">
  <a class="top-logo" href="./"><img src="assets/img/technext/logo-h-blue.png" alt="TechNext" width="642" height="93"><span>Brand kits</span></a>
  <nav class="top-nav" aria-label="Brand kits">{links}</nav>
</div></header>"""


def foot():
    return f"""<footer class="foot"><div class="wrap foot-in"><span>Brand kits compiled by TechNext · internal, unlisted · October 2026</span><a href="https://technext.asia/" target="_blank" rel="noopener">technext.asia</a></div></footer>
<script src="assets/kit.js?v={V}"></script>
</body></html>"""


def sec(sid, n, title, body, note=""):
    note = f'<p class="note">{note}</p>' if note else ""
    return f'<section class="sec" id="{sid}"><h2><span>{n:02d}</span>{title}</h2>{note}{body}</section>'


def table(rows, cls="tbl"):
    return f'<table class="{cls}"><tbody>' + "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rows) + "</tbody></table>"


def sw(name, hx, role, big=False):
    return (f'<button type="button" class="sw{" sw-big" if big else ""}" data-hex="{hx}"><span class="sw-chip"></span>'
            f'<span class="sw-t"><b>{e(name)}</b><code>{hx}</code><span class="sw-rgb"></span><span class="sw-role">{role}</span><span class="sw-c"></span></span></button>')


MAT = json.loads((SRC / "materials.json").read_text(encoding="utf-8")) if (SRC / "materials.json").exists() else {}


def materials(slug):
    items = MAT.get(slug, [])
    if not items:
        return '<p class="src">The materials list is being compiled.</p>'
    cats, out = [], []
    for it in items:
        if it["cat"] not in cats:
            cats.append(it["cat"])
    zip_ = f'<a class="dl dl-big" href="downloads/{slug}-brand-kit.zip" download>{icon("file")}Download all ({len([i for i in items if i.get("file")])} files, ZIP)</a>' if (ROOT / f"downloads/{slug}-brand-kit.zip").exists() else ""
    out.append(f'<div class="mat-head"><span>{len(items)} materials in {len(cats)} groups</span>{zip_}</div>')
    for c in cats:
        rows = []
        for it in [i for i in items if i["cat"] == c]:
            th = f'<img src="{it["thumb"]}" alt="" loading="lazy" class="zoom" data-cap="{e(it["title"])}">' if it.get("thumb") else (icon("layers") if it.get("folder") is not None else f'<span class="mat-ext">{e(it.get("fmt", "").upper()[:4])}</span>')
            size = " · ".join(x for x in [it.get("fmt", "").upper(), f'{it["w"]}×{it["h"]}' if it.get("w") else "", (f'{it["kb"] / 1024:.1f} MB' if it.get("kb", 0) >= 1024 else f'{it.get("kb", 0)} KB') if it.get("kb") else ""] if x)
            get = dl(it["file"], "Download") if it.get("file") else (f'<span class="mat-src">folder · {it["folder"]} files</span>' if it.get("folder") is not None else '<span class="mat-src">over 8 MB · at the path</span>')
            off = '<span class="mat-off">official</span>' if it.get("official") else ""
            rows.append(f'<div class="mat"><div class="mat-v">{th}</div><div class="mat-t"><b>{e(it["title"])}</b>{off}<small>{size}</small><code>{e(it["path"])}</code></div><div class="mat-a">{get}</div></div>')
        out.append(f'<h3 class="sub">{e(c)} <span class="cnt">{len(rows)}</span></h3><div class="mats">' + "".join(rows) + "</div>")
    return "".join(out)


def page(slug):
    B = KD.BRANDS[slug]; C = B["colours"]
    strip = "".join(f'<i style="background:{h}" title="{h}"></i>' for _, h, _ in C["primary"])
    meta = "".join(f'<div><small>{e(k)}</small><b>{v}</b></div>' for k, v in B["cover"]["meta"])
    hero = f"""<section class="hero"><div class="wrap hero-in">
  <div class="hero-copy"><p class="eyebrow">Brand kit · compiled October 2026</p><h1>{e(B['name'])}</h1>
    <p class="lead">{B['cover']['lead']}</p><div class="hero-meta">{meta}</div><p class="checked">{icon('check')}{e(B.get('updated', ''))}</p></div>
  <div class="hero-card"><img src="{B['logo_light']}" alt="{e(B['name'])} logo"><div class="strip">{strip}</div><small>{e(B['site'])}</small></div>
</div></section>"""
    nav = "".join(f'<a href="#{sid}">{t}</a>' for sid, t in SECTIONS)

    # 01 basics
    fam = ""
    if B.get("family"):
        fam = '<div class="fam">' + "".join(f'<div class="fam-c{" me" if me else ""}"><img src="{img}" alt=""><b>{e(n)}</b><small>{e(r)}</small></div>' for n, img, r, me in B["family"]) + "</div>"
    side = re.sub(r"\{\{dl:([^}]+)\}\}", lambda m: dl(m.group(1)), B.get("basics_side", "").replace(' data-in style="--d:300ms"', ""))
    s1 = sec("basics", 1, "Basics", f'<div class="g2">{table(B["basics"])}<div>{fam}{side}</div></div>')

    # 02 logo
    L = B["logo"]; tile = "background:#fff;padding:16px 22px;border-radius:14px;box-sizing:content-box;"
    imgs = "".join(f'<img class="lg-img" data-on="{on}" src="{src}" alt="{e(alt)}" style="{tile if B.get("tile") and "dark" in on else ""}width:{min(w, 420)}px"{" hidden" if i else ""}>' for i, (on, src, alt, w) in enumerate(L["stage"]))
    bgs = "".join(f'<button type="button" data-bg="{k}"{" aria-pressed=\"true\"" if i == 0 else ""}><i style="background:{h}"></i>{lab}</button>' for i, (k, lab, h) in enumerate(L["grounds"]))
    notes = "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in L["notes"])
    viewer = f"""<div class="g2 g2-w"><div class="lg-wrap"><div class="lg-stage" data-cs-label="{e(L['cs_label'])}" style="--cs:{round(L['cs'] * .7)}px;--photo:url({L.get('photo', '')})">{imgs}</div>
      <div class="lg-bgs">{bgs}<span class="sp"></span><button type="button" data-guide aria-pressed="false">Clear space</button></div></div><div class="stack">{notes}</div></div>"""
    files = "".join(f"""<div class="file"><div class="file-v" style="background:{f['bg']}"><img src="{f['img']}" alt="" style="{'background:#fff;padding:8px 12px;border-radius:10px;' if f.get('tile') else ''}"></div>
      <div class="file-t"><b>{e(f['name'])}</b>{dl(f['img'], f.get('dl', 'PNG'))}<small>{f['use']}</small><code>{e(f['master'])}</code></div></div>""" for f in B["logo_files"])
    R = B["logo_rules"]
    mis = "".join(f'<div class="dn {"ok" if ok else "no"}"><div class="dn-v" style="{bg}">{v}</div><p>{t}</p></div>' for ok, bg, v, t in R["misuse"])
    sweb = sec("web", 2, "Web identity", table(B.get("web", [])), "As the live site presents the brand: titles, navigation, footer, contacts, icons and share images.")
    s2 = sec("logo", 3, "Logo", viewer + f'<h3 class="sub">Files</h3><div class="files">{files}</div>' +
             (f'<p class="src">{B["logo_files_note"]}</p>' if B.get("logo_files_note") else "") +
             f'<h3 class="sub">Rules and misuse</h3><div class="g2 g2-n">{table(R["specs"])}<div class="mis">{mis}</div></div>')

    # 03 colour
    prim = "".join(sw(n, h, r, True) for n, h, r in C["primary"])
    ratio = "".join(f'<i style="flex:{w};background:{c}"{" class=\"lt\"" if lt else ""}>{t}</i>' for t, w, c, lt in C["ratio"])
    more = "".join(sw(n, h, r) for n, h, r in C["more"])
    grads = "".join(f'<div class="grad" style="background:{css};{"color:" + fg if fg else ""}">{lab}</div>' for css, lab, fg in C.get("gradients", []))
    s3 = sec("colour", 4, "Colour", f'<div class="sws sws-p" data-ink="{C["ink"]}">{prim}</div><div class="ratio">{ratio}</div>'
             f'<h3 class="sub">All tokens</h3><div class="sws sws-s" data-ink="{C["ink"]}">{more}</div>'
             + (f'<h3 class="sub">Gradients</h3><div class="grads">{grads}</div>' if grads else ""),
             f'Click a colour to copy its hex. Contrast is measured against white and the brand ink {C["ink"]}. {C.get("notes", "")}')

    # 04 type
    tests = []
    for f in B["fonts"]:
        ws = "".join(f'<button type="button" data-w="{w}"{(" data-style=\"" + st + "\"") if st else ""}{" aria-pressed=\"true\"" if j == f.get("on", 0) else ""}>{lab}</button>' for j, (w, st, lab) in enumerate(f["weights"]))
        lo, hi, v = f["size"]
        tests.append(f"""<div class="ts"><div class="ts-h"><b style="font-family:{f['css']}">{e(f['name'])}</b><small>{f['role']}</small></div>
      <div class="ts-line" style="font-family:{f['css']};{f.get('line', '')}">{f['sample']}</div>
      <div class="ts-ctl"><div class="seg">{ws}</div><input type="range" min="{max(14, lo - 6)}" max="{hi - 16}" value="{max(16, v - 10)}" data-size aria-label="Size"><span class="ts-px"></span></div>
      <p class="src">{f['src']}</p></div>""")
    rows = "".join(f'<tr><th>{e(k)}</th><td><span style="{css}">{sample}</span></td><td class="m">{meta}</td></tr>' for k, css, sample, meta in B["scale"])
    side = "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in B["scale_side"])
    s4 = sec("type", 5, "Typography", f'<div class="tss tss-{len(tests)}">{"".join(tests)}</div><h3 class="sub">Scale</h3>'
             f'<div class="g2 g2-w"><table class="tbl scale"><tbody>{rows}</tbody></table><div class="stack">{side}</div></div>', B.get("type_notes", ""))

    # 05 ui
    U = B["ui"]
    ez = "".join(f'<div class="ez" style="--fn:{c};--dur:{ms}ms"><div><b>{e(n)}</b><code>{e(c.replace("cubic-bezier", ""))} · {ms}ms</code></div><div class="ez-t"><i></i></div></div>' for n, c, ms in U["eases"])
    toks = table([(e(k), f"<code>{e(v)}</code>") for k, v in U["tokens"]])
    s5 = sec("ui", 6, "UI tokens", f'<div class="g2"><div class="stack"><div class="card"><h3>Buttons, live</h3>{U["buttons"].replace("{{icon:arrow}}", icon("arrow"))}</div>{ez}</div>{toks}</div>', U["lead"] + ("" if "curve" in U["lead"] else " Click a curve to play it."))

    # accessibility
    a = "".join(f'<tr><th>{e(k)}</th><td class="m">{r}:1</td><td>{e(v)}</td></tr>' for k, r, v in B.get("a11y", []))
    sa = sec("a11y", 7, "Accessibility", f'<table class="tbl a11y"><thead><tr><th>Pair</th><th>Contrast</th><th>Use</th></tr></thead><tbody>{a}</tbody></table><p class="src">{B.get("a11y_notes", "")}</p>',
             "WCAG 2.x contrast, computed from the live tokens.")

    # 06 imagery
    I = B["imagery"]
    pics = "".join(f'<figure class="pic zoom" data-cap="{e(c)} · {e(p)}"><img src="{img}" alt="{e(c)}" loading="lazy"><figcaption>{e(c)}</figcaption></figure>' for img, c, p in I["photos"])
    s6 = sec("imagery", 8, "Imagery", f'<div class="g2 g2-n"><div class="card"><ul class="ul">{"".join(f"<li>{r}</li>" for r in I["rules"])}</ul><p class="src">{I["src"]}</p></div><div class="lib">{pics}</div></div>')

    # 07 formats
    fr = "".join(f'<tr><td class="th">{("<img class=" + chr(34) + "zoom" + chr(34) + " src=" + chr(34) + t + chr(34) + " alt=" + chr(34) + chr(34) + " loading=" + chr(34) + "lazy" + chr(34) + ">") if t else ""}</td><th>{a}</th><td class="m">{s}</td><td>{sp}</td></tr>' for a, s, sp, t in B["formats"])
    anat = "".join(f'<div class="card"><h3>{e(t)}</h3><p>{d}</p></div>' for t, d in B.get("anatomy", []))
    s7 = sec("formats", 9, "Formats and templates", f'<table class="tbl fmt"><thead><tr><th></th><th>Application</th><th>Size</th><th>Spec</th></tr></thead><tbody>{fr}</tbody></table>'
             + (f'<h3 class="sub">Templates and page anatomy</h3><div class="anat">{anat}</div>' if anat else ""))

    # 08 wording
    W = B["words"]
    traits = "".join(f"<span>{t}</span>" for t in W["traits"])
    tone = "".join(f"<li>{e(t)}</li>" for t in B.get("tone", []))
    ctas = "".join(f'<div class="cta-g"><b>{e(g)}</b><p>' + "".join(f'<span>{e(x)}</span>' for x in xs) + "</p></div>" for g, xs in B.get("ctas", []))
    s8 = sec("wording", 10, "Voice and wording", f'<div class="traits">{traits}</div>'
             + ('<div class="g3" style="margin:14px 0">' + "".join(f'<div class="card"><h3>{e(h)}</h3><p>{e(t)}</p></div>' for h, t in B.get("voice_pillars", [])) + "</div>" if B.get("voice_pillars") else "")
             + (f'<div class="g2 g2-w"><div class="card"><h3>In the brand\'s own words (verbatim, live)</h3><ol class="tone">{tone}</ol></div><div class="card"><h3>Button and link labels in use</h3>{ctas}</div></div>' if tone else "")
             + f'<div class="g3" style="margin-top:14px"><div class="card yes"><h3>Use</h3><ul class="ck">{"".join(f"<li>{x}</li>" for x in W["use"])}</ul></div>'
             f'<div class="card no"><h3>Avoid</h3><ul class="ck">{"".join(f"<li>{x}</li>" for x in W["avoid"])}</ul></div>{table(W["spelling"])}</div>')

    # 09 rules
    s9 = sec("rules", 11, "Do's and don'ts", f'<div class="g2"><div class="card yes"><h3>Do</h3><ul class="ck">{"".join(f"<li>{x}</li>" for x in B["do"])}</ul></div>'
             f'<div class="card no"><h3>Don\'t</h3><ul class="ck">{"".join(f"<li>{x}</li>" for x in B["dont"])}</ul></div></div>')

    # 10 masters
    M = B["masters"]
    s10 = sec("masters", 12, "Masters and open items", f'<div class="g2 g2-w">{table([(e(k), f"<code>{e(v)}</code>") for k, v in M["paths"]])}'
              f'<div class="stack"><div class="card open"><h3>Open items</h3><ul class="ul">{"".join(f"<li>{x}</li>" for x in M["open"])}</ul></div>'
              f'<div class="card qr-c">{qr(M["qr"], M.get("qr_c", "#1F1F3D"))}<div><b>{e(B["site"])}</b><small>{M["sources"]}</small></div></div></div></div>')

    s11 = sec("materials", 13, "All materials", materials(slug), "Every material for this brand, with its source path. Download buttons give the file kept in this kit; large originals stay at the path shown.")
    body = s1 + sweb + s2 + s3 + s4 + s5 + sa + s6 + s7 + s8 + s9 + s10 + s11
    desc = f"{B['name']} brand kit: basics, logo files, colour tokens, typography, UI tokens, imagery, formats and wording."
    html = (head(f"{B['name']} Brand Kit · TechNext", desc) + f'\n<body data-kit="{slug}">\n' + topbar(slug) + hero +
            f'<div class="wrap layout"><nav class="side" aria-label="Sections">{nav}<a class="print" href="javascript:print()">Print / PDF</a></nav><main class="main">{body}</main></div>\n' + foot())
    return html.replace("{{icon:arrow}}", icon("arrow"))


def index():
    cards = []
    for s in ORDER:
        B = KD.BRANDS[s]; C = B["colours"]
        strip = "".join(f'<i style="background:{h}"></i>' for _, h, _ in C["primary"])
        fonts = next((v for k, v in B["cover"]["meta"] if k in ("Fonts", "Font")), " · ".join(f["name"] for f in B["fonts"]))
        line = next((v for k, v in B["basics"] if k in ("Hero line", "Tagline", "Home H1", "Brand line")), "")
        chips = "".join(f'<i style="background:{h}" title="{n} {h}"></i>' for n, h, _ in C["primary"])
        nmat = len(MAT.get(s, []))
        cards.append(f"""<a class="kc" href="{s}.html"><div class="kc-v"><img src="{B['logo_light']}" alt=""></div><div class="strip">{strip}</div>
  <div class="kc-t"><b>{e(B['name'])}</b><small>{e(B['site'])}</small><p class="kc-line">{line}</p>
  <dl><div><dt>Primary</dt><dd><code>{C['primary'][0][1]}</code> {e(C['primary'][0][0])}</dd></div><div><dt>Accent</dt><dd><code>{C['primary'][1][1]}</code> {e(C['primary'][1][0])}</dd></div>
  <div class="w2"><dt>Fonts</dt><dd>{fonts}</dd></div>
  <div><dt>Logo files</dt><dd>{len(B['logo_files'])}</dd></div><div><dt>Colour tokens</dt><dd>{len(C['primary']) + len(C['more'])}</dd></div>
  <div><dt>Materials</dt><dd>{nmat or '—'}</dd></div><div><dt>Live check</dt><dd>15 Oct 2026</dd></div></dl>
  <span class="go">Open kit {icon('arrow')}</span></div></a>""")
    secs = "".join(f"<li>{t}</li>" for _, t in SECTIONS)
    return (head("Brand Kits · TechNext", "Brand kit compilations for TechNext, HummingBeing, BHD Asia and TRE in Singapore.") + "\n<body>\n" + topbar("") +
            f"""<section class="hero hero-ix"><div class="wrap"><p class="eyebrow">Brand kits · compiled October 2026</p><h1>Four brand kits, <span>in one place.</span></h1>
<p class="lead">Logos with downloads, colour tokens, fonts, UI tokens, accessibility, photo libraries, formats, templates, wording and every material for each brand. Checked against the live sites on 15 Oct 2026.</p></div></section>
<main class="wrap ix"><div class="kcs">{"".join(cards)}</div><div class="card ix-in"><h3>In every kit</h3><ol class="ix-l">{secs}</ol></div></main>
""" + foot())


def main():
    for s in ORDER:
        (ROOT / f"{s}.html").write_text(page(s), encoding="utf-8", newline="\n")
    (ROOT / "index.html").write_text(index(), encoding="utf-8", newline="\n")
    miss = []
    for f in ROOT.glob("*.html"):
        for ref in set(re.findall(r'(?:src|href)="(assets/[^"?]+)', f.read_text(encoding="utf-8"))):
            if not (ROOT / ref).exists():
                miss.append(f"{f.name}: {ref}")
    if miss:
        sys.exit("missing:\n  " + "\n  ".join(sorted(miss)))
    print("built", ", ".join(ORDER + ["index"]))


if __name__ == "__main__":
    main()
