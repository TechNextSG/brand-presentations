# -*- coding: utf-8 -*-
"""Build the brand kits (presentation-style brand guides on the TechNext deck engine).

Sources live in _src/decks/*.html and are written to the repo root with these tokens expanded:
  {{head}}              shared <head> tags (charset, viewport, noindex, favicons, deck fonts, deck.css)
  {{icon:name}}         inline SVG from the technext.asia icon set (_src/icons.json)
  {{qr:key}}            inline SVG QR code for a known link (QR below)
  {{og:slug}}           Open Graph tags from the page's <title> and description
  {{include:name}}      the contents of _src/partials/name.html
  {{v}}                 the asset version
Run: python -B _src/build.py
"""
import html as _html
import io
import json
import pathlib
import re
import secrets
import sys

import segno

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
sys.path.insert(0, str(SRC))
ICONS = json.loads((SRC / "icons.json").read_text(encoding="utf-8"))
ASSET_V = "5"
BASE = "https://technextsg.github.io/brand-presentations/"

QR = {
    "technext": "https://technext.asia/",
    "hummingbeing": "https://hummingbeing.com/",
    "bhdasia": "https://bhdasia.com/",
    "tre": "https://tre-in-singapore.com/",
}

HEAD = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<link rel="icon" type="image/png" sizes="48x48" href="assets/img/favicon-48.png">
<link rel="icon" type="image/png" sizes="192x192" href="assets/img/favicon-192.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/plus-jakarta-sans-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/fonts.css?v={v}">
<link rel="stylesheet" href="assets/deck.css?v={v}">
<link rel="stylesheet" href="assets/motion.css?v={v}">
<link rel="stylesheet" href="assets/brand.css?v={v}">""".replace("{v}", ASSET_V)

# The launcher (index.html) is generated from this list: a deck appears once its HTML is built.
DECKS = [
    ("TechNext", [
        dict(slug="technext", tags="tech", title="TechNext", mins=10, pdf="Brand-Kit-TechNext.pdf",
             alt="TechNext brand kit cover",
             desc="Name and lines, every logo file with downloads, the blue palette and tokens, Plus Jakarta Sans, Inter and Caveat, UI tokens, Nexi poses, imagery, formats, wording and where the masters live."),
    ]),
    ("Isabelle's brands", [
        dict(slug="hummingbeing", tags="wellness", title="HummingBeing", mins=10, pdf="Brand-Kit-HummingBeing.pdf",
             alt="HummingBeing brand kit cover",
             desc="Name and lines, the hummingbird logo files with downloads, navy, gold and cream tokens, Playfair Display, Lato and PT Serif, button and event-page tokens, photo library, poster and thumbnail formats."),
        dict(slug="bhdasia", tags="leadership", title="BHD Asia", mins=10, pdf="Brand-Kit-BHD-Asia.pdf",
             alt="BHD Asia brand kit cover",
             desc="Name and lines, the logo and traced mark with downloads, the warm marigold and ivory tokens, Figtree, the marigold pill and motion tokens, photo library, social post and event formats."),
        dict(slug="tre-singapore", tags="leadership wellness", title="TRE in Singapore", mins=10, pdf="Brand-Kit-TRE-Singapore.pdf",
             alt="TRE in Singapore brand kit cover",
             desc="Name and lines, the official logo and its open items, navy, bronze and cream tokens, Plus Jakarta Sans and Inter, the pills and tremor field, photo library and share-card formats."),
    ]),
]
GROUPS = {
    "TechNext": ("ours", "Our own brand kit."),
    "Isabelle's brands": ("isabelle", "BHD Asia, HummingBeing and TRE in Singapore."),
}
TOPICS = [("tech", "Tech"), ("wellness", "Wellness"), ("leadership", "Leadership")]
WORDS = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}

# ---------------------------------------------------------------- share links
SHARE_FILE = SRC / "share.json"
_share = {}


def share_tokens():
    if not _share:
        tok = json.loads(SHARE_FILE.read_text(encoding="utf-8")) if SHARE_FILE.exists() else {}
        new = [d["slug"] for _, ds in DECKS for d in ds if d["slug"] not in tok]
        for slug in new:
            tok[slug] = "".join(secrets.choice("abcdefghijkmnpqrstuvwxyz23456789") for _ in range(7))
        if new:
            SHARE_FILE.write_text(json.dumps(tok, indent=1) + "\n", encoding="utf-8")
        _share.update(tok)
    return _share


def share_copy(html, slug):
    """The shared copy of a built deck: no way back to the launcher, links to other decks (data-internal) removed."""
    name = f"s-{share_tokens()[slug]}.html"
    s = html.replace(' data-home="./"', " data-shared", 1)
    s = re.sub(r"<(p|a|div|li)\b[^>]*\bdata-internal\b[^>]*>.*?</\1>", "", s, flags=re.S)
    s = s.replace(f'<meta property="og:url" content="{BASE}{slug}.html">', f'<meta property="og:url" content="{BASE}{name}">')
    decks = "|".join(re.escape(d["slug"]) for _, ds in DECKS for d in ds)
    leak = re.findall(r'href="((?:\./|index\.html|(?:%s)\.html)[^"]*)"' % decks, s)
    if leak or "data-shared" not in s:
        sys.exit(f"{slug}: the shared copy still leads to {leak or 'the launcher'}: mark those links data-internal")
    return name, s


def launcher():
    groups, tabs, n, slides_all, mins_all = [], [], 0, 0, 0
    for gname, decks in DECKS:
        gkey, blurb = GROUPS[gname]
        cards = []
        for d in decks:
            html = ROOT / (d["slug"] + ".html")
            if not html.exists():
                continue
            slides = len(re.findall(r'<section class="slide[ "]', html.read_text(encoding="utf-8")))
            th = f"assets/img/thumbs/{d['slug']}"
            second = (f'\n        <img class="ix-thumb-2" src="{th}-2.jpg" alt="" width="960" height="540" loading="lazy" decoding="async">' if (ROOT / f"{th}-2.jpg").exists() else "")
            has_pdf = (ROOT / "pdf" / d["pdf"]).exists()
            pdf = (f'<a class="ix-btn ix-btn--t" href="pdf/{d["pdf"]}">{{{{icon:file}}}}PDF</a>' if has_pdf else "")
            share = (f'<button type="button" class="ix-btn ix-btn--t ix-share" data-share="{BASE}s-{share_tokens()[d["slug"]]}.html" data-title="{d["title"]}"'
                     f' aria-haspopup="dialog" aria-expanded="false">{{{{icon:link}}}}Share</button>')
            more = f'\n          <span class="ix-more">{pdf}{share}</span>'
            tags = d.get("tags", "").split()
            chips = "".join(f'<span class="ix-tag">{label}</span>' for key, label in TOPICS if key in tags)
            words = " ".join([d["title"], d["desc"], gname] + [label for key, label in TOPICS if key in tags]).lower()
            cards.append(f"""    <article class="ix-card" data-g="{gkey}" data-tags="{' '.join(tags)}" data-mins="{d['mins']}" data-slides="{slides}" data-order="{n}" data-title="{_html.escape(d['title'].lower())}" data-words="{_html.escape(words)}">
      <a class="ix-thumb" href="{d['slug']}.html" aria-label="Open {d['title']}" tabindex="-1">
        <img src="{th}.jpg" alt="{d['alt']}" width="960" height="540" loading="lazy">{second}
        <span class="ix-len">{d['mins']} min</span>
      </a>
      <div class="ix-body">
        <p class="ix-meta"><span class="ix-cat">{gname}</span><span class="ix-sl">{slides} slides</span></p>
        <h3><a href="{d['slug']}.html">{d['title']}</a></h3>
        <p class="ix-desc">{d['desc']}</p>
        <p class="ix-tags">{chips}</p>
        <div class="ix-acts">
          <a class="ix-btn ix-btn--p" href="{d['slug']}.html">Present</a>
          <a class="ix-btn" href="{d['slug']}.html?kiosk" aria-label="Kiosk loop">Kiosk<span class="ix-kl">&nbsp;loop</span></a>{more}
        </div>
      </div>
    </article>""")
            n += 1
            slides_all += slides
            mins_all += d["mins"]
        if cards:
            tabs.append(f'<button type="button" class="ix-tab" data-g="{gkey}" aria-pressed="false">{gname}<span>{len(cards)}</span></button>')
            groups.append(f'  <section class="ix-group" data-g="{gkey}" style="--n:{min(len(cards), 4)}" aria-labelledby="g-{gkey}">\n'
                          f'    <header class="ix-gh"><h2 id="g-{gkey}">{gname}</h2><span class="ix-gn">{len(cards)}</span><p>{blurb}</p></header>\n'
                          f'    <div class="ix-grid">\n' + "\n".join(cards) + "\n    </div>\n  </section>")
    topics = "".join(f'<button type="button" class="ix-chip" data-t="{k}" aria-pressed="false">{v}</button>' for k, v in TOPICS)
    bar = f"""  <div class="ix-bar" id="decks" role="search" aria-label="Find a brand kit">
    <div class="ix-bar-1">
      <label class="ix-q">{{{{icon:search}}}}<input type="search" placeholder="Search the brand kits" aria-label="Search the brand kits" autocomplete="off" spellcheck="false"><kbd aria-hidden="true">/</kbd></label>
      <div class="ix-tabs" role="group" aria-label="Group"><button type="button" class="ix-tab" data-g="" aria-pressed="true">All<span>{n}</span></button>{''.join(tabs)}</div>
    </div>
    <div class="ix-bar-2">
      <div class="ix-chips" role="group" aria-label="Topic"><span class="ix-lbl">Topic</span>{topics}</div>
      <div class="ix-end">
        <label class="ix-sort"><span class="ix-lbl">Sort</span><select aria-label="Sort"><option value="">By group</option><option value="az">A to Z</option><option value="short">Shortest first</option><option value="long">Longest first</option></select></label>
        <div class="ix-view" role="group" aria-label="View"><button type="button" data-view="grid" aria-pressed="true" aria-label="Grid">{{{{icon:grid}}}}</button><button type="button" data-view="list" aria-pressed="false" aria-label="List">{{{{icon:menu}}}}</button></div>
      </div>
    </div>
  </div>
  <p class="ix-count" role="status" aria-live="polite"><span data-count>All {n} brand kits</span><button type="button" class="ix-clear" data-clear hidden>Clear filters</button></p>
  <div class="ix-results">
"""
    empty = '  <div class="ix-empty" hidden><b>No brand kit matches that.</b><p>Try another word, or <button type="button" data-clear>clear the filters</button>.</p></div>\n'
    flat = '  <div class="ix-grid ix-flat" hidden></div>\n'
    return bar + "\n".join(groups) + "\n" + flat + empty + "  </div>", n, slides_all, mins_all


def qr_svg(key, dark="#1F1F3D"):
    q = segno.make(QR[key], error="m")
    buf = io.BytesIO()
    q.save(buf, kind="svg", scale=1, border=0, dark=dark, light=None, xmldecl=False, svgns=True, nl=False, svgclass="qr", lineclass="qr-p", omitsize=True)
    s = buf.getvalue().decode("utf-8")
    return s.replace("<svg ", '<svg aria-hidden="true" preserveAspectRatio="xMidYMid meet" ', 1)


def icon(name):
    if name not in ICONS:
        raise KeyError("unknown icon: " + name)
    return ICONS[name]


def og(s, name, page):
    t = re.search(r"<title>(.*?)</title>", s).group(1)
    d = re.search(r'<meta name="description" content="(.*?)">', s).group(1)
    url = BASE + ("" if page == "index.html" else page)
    return (f'<meta property="og:type" content="website">\n<meta property="og:site_name" content="Brand kits">\n'
            f'<meta property="og:title" content="{t}">\n<meta property="og:description" content="{d}">\n'
            f'<meta property="og:url" content="{url}">\n<meta property="og:image" content="{BASE}assets/img/thumbs/{name}-og.jpg">\n'
            f'<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta name="twitter:card" content="summary_large_image">')


def expand(s, page=""):
    if "{{kit:" in s:
        import kit
        s = re.sub(r"\{\{kit:([a-z-]+)\}\}", lambda m: kit.expand_kit(m.group(1)), s)
    s = re.sub(r"\{\{og:([a-z-]+)\}\}", lambda m: og(s, m.group(1), page), s)
    for _ in range(3):
        s = re.sub(r"\{\{include:([a-z0-9_-]+)\}\}", lambda m: (SRC / "partials" / (m.group(1) + ".html")).read_text(encoding="utf-8"), s)
    s = s.replace("{{head}}", HEAD).replace("{{v}}", ASSET_V)
    s = re.sub(r"\{\{icon:([a-z0-9_-]+)\}\}", lambda m: icon(m.group(1)), s)
    s = re.sub(r"\{\{qr:([a-z]+)(?::(#[0-9A-Fa-f]{6}))?\}\}", lambda m: qr_svg(m.group(1), m.group(2) or "#1F1F3D"), s)
    # pictures carry the asset version too, so an offline copy never keeps an old file
    s = re.sub(r'(assets/img/[a-z0-9/_-]+\.(?:jpg|png|webp|svg))(?=")', r"\1?v=" + ASSET_V, s)
    left = re.findall(r"\{\{[^}]*\}\}", s)
    if left:
        raise ValueError("unexpanded tokens: " + ", ".join(sorted(set(left))[:10]))
    return s


def main():
    out = []
    for p in sorted((SRC / "decks").glob("*.html"), key=lambda p: p.name == "index.html"):
        src = p.read_text(encoding="utf-8")
        if "{{launcher}}" in src:
            cards, n, ns, nm = launcher()
            src = (src.replace("{{launcher}}", cards).replace("{{deck_count}}", WORDS.get(n, str(n)))
                   .replace("{{slide_count}}", str(ns)).replace("{{minutes}}", str(nm)))
        html = expand(src, p.name)
        (ROOT / p.name).write_text(html, encoding="utf-8", newline="\n")
        out.append((p.name, len(html)))
        if p.stem in share_tokens():
            name, shared = share_copy(html, p.stem)
            (ROOT / name).write_text(shared, encoding="utf-8", newline="\n")
    live = {f"s-{t}.html" for t in share_tokens().values()}
    for old in ROOT.glob("s-*.html"):
        if old.name not in live:
            old.unlink(); print("  retired share link", old.name)
    missing = []
    for f in ROOT.glob("*.html"):
        for ref in set(re.findall(r'(?:src|href)="(assets/img/[^"?]+)', f.read_text(encoding="utf-8"))):
            if not (ROOT / ref).exists() and "/thumbs/" not in ref:
                missing.append(f"{f.name}: {ref}")
    if missing:
        sys.exit("missing pictures:\n  " + "\n  ".join(sorted(set(missing))))
    for name, n in out:
        print(f"  {name:28s} {n/1024:7.1f} KB")


if __name__ == "__main__":
    main()
