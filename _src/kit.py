# -*- coding: utf-8 -*-
"""Brand kit decks, generated from _src/kit_data.py: every brand gets the same compilation, slide for slide.
A deck source is just {{kit:<slug>}} inside the <main>; build.py calls expand_kit()."""
import html as _h

import kit_data as KD


def e(s):
    return _h.escape(s, quote=True)


def d(i, base=200, step=40):
    return f'--d:{base + i * step}ms'


def head(kicker, title, lead=""):
    lead = f'\n    <p class="lead" data-in style="--d:160ms">{lead}</p>' if lead else ""
    return f"""  <div class="sec-head">
    <span class="kicker" data-in>{kicker}</span>
    <h2 class="h-m" data-in style="--d:80ms">{title}</h2>{lead}
  </div>"""


def slide(sid, title, body, notes, cls="", extra=""):
    c = f' {cls}' if cls else ""
    return f"""
<section class="slide{c}" id="{sid}" data-title="{e(title)}"{extra}>
{body}
  <aside class="notes"><p>{notes}</p></aside>
</section>"""


def dl(path, label="PNG"):
    name = path.rsplit("/", 1)[-1]
    return f'<a class="kit-dl" href="{path}" download="{name}" data-i>{{{{icon:file}}}}{label}</a>'


def cover(B):
    C = B["cover"]
    meta = "".join(f"<div>{e(k)}<b>{v}</b></div>" for k, v in C["meta"])
    strip = "".join(f'<i style="background:{h}" title="{h}"></i>' for _, h, _ in B["colours"]["primary"])
    return slide("cover", f'{B["name"]} brand kit', f"""  <div class="bk-cover">
    <div class="bk-cover-copy">
      <img class="bk-cover-logo" src="assets/img/technext/logo-h-white.png" alt="TechNext" style="height:46px" data-in>
      <span class="bk-eyebrow" data-in style="--d:60ms">Brand kit · compiled October 2026</span>
      <h1 class="h-xl" data-in style="--d:120ms">{e(B['name'])} <span class="hl">brand kit.</span></h1>
      <p class="lead" data-in style="--d:220ms">{C['lead']}</p>
      <div class="bk-cover-meta" data-in style="--d:320ms">{meta}</div>
    </div>
    <div class="kit-cv" data-in data-fx="scale" style="--d:240ms">
      <div class="kit-cv-card"><img src="{B['logo_light']}" alt="{e(B['name'])} logo" style="max-height:{C.get('card_h', 150)}px"><div class="kit-cv-strip">{strip}</div><small>{e(B['site'])}</small></div>
    </div>
  </div>""", "A compilation of the brand as it is used today, for reference: what the files are, where they live and the values to use.",
                 "dark cover", ' data-chrome="none"')


SECTIONS = [("basics", "Brand basics", "Names, lines, family"), ("logo", "Logo", "Viewer, clear space"), ("logo-files", "Logo files", "Every file, with downloads"),
            ("logo-rules", "Logo rules", "Sizes and misuse"), ("colour", "Colour", "Primary palette"), ("colour-2", "Colour tokens", "Every value"),
            ("type", "Typography", "Families and weights"), ("type-scale", "Type scale", "Sizes in use"), ("ui", "UI tokens", "Buttons, radii, motion"),
            ("imagery", "Imagery", "Style and photo library"), ("formats", "Formats", "Sizes and templates"), ("words", "Wording", "Voice and spelling rules"),
            ("dodont", "Do's and don'ts", "On one page"), ("masters", "Where the masters live", "Files and sources")]


def index(B):
    links = "".join(f'<a href="#" data-go="{sid}" data-in style="{d(i, 180, 25)}"><span>{i + 1:02d}</span><div>{t}<small>{s}</small></div></a>'
                    for i, (sid, t, s) in enumerate(SECTIONS))
    return slide("contents", "Kit index", head("kit index", f'Everything in the <span class="hl">{e(B["short"])} kit.</span>') +
                 f'\n  <nav class="bk-toc kit-toc" aria-label="Sections">{links}</nav>', "Click a section to jump to it.")


def basics(B):
    rows = "".join(f"<tr><th>{e(k)}</th><td>{v}</td></tr>" for k, v in B["basics"])
    fam = ""
    if B.get("family"):
        cards = "".join(f'<div class="kit-fam{" is-me" if me else ""}"><img src="{img}" alt="{e(n)}"><b>{e(n)}</b><small>{e(r)}</small></div>' for n, img, r, me in B["family"])
        fam = f'<div class="kit-fam-row" data-in style="--d:260ms"><p class="kit-sub">Brand family</p><div class="kit-fams">{cards}</div></div>'
    return slide("basics", "Brand basics", head("01 · basics", B["basics_title"]) + f"""
  <div class="kit-2" style="margin-top:24px">
    <table class="kit-tbl" data-in style="--d:200ms"><tbody>{rows}</tbody></table>
    <div>{fam}{B.get('basics_side', '')}</div>
  </div>""", "The reference facts for the name and lines. Quote taglines exactly as written here.")


def logo(B):
    L = B["logo"]
    tile = "background:#fff;padding:22px 28px;border-radius:18px;box-sizing:content-box;"
    imgs = "".join(f'<img class="lg-img" data-on="{on}" src="{src}" alt="{e(alt)}" style="{tile if B.get("tile") and "dark" in on else ""}width:{w}px"{" hidden" if i else ""}>' for i, (on, src, alt, w) in enumerate(L["stage"]))
    bgs = "".join(f'<button type="button" data-bg="{k}"{" aria-pressed=\"true\"" if i == 0 else ""}><i style="background:{h}"></i>{lab}</button>' for i, (k, lab, h) in enumerate(L["grounds"]))
    notes = "".join(f'<div class="bk-card" data-in style="{d(i, 260, 60)}"><h3>{h}</h3><p>{p}</p></div>' for i, (h, p) in enumerate(L["notes"]))
    return slide("logo", "Logo", head("02 · logo", L["title"]) + f"""
  <div class="kit-2" style="grid-template-columns:1.45fr 1fr;margin-top:22px;height:570px">
    <div class="lg-wrap" data-in style="--d:200ms">
      <div class="lg-stage" data-cs-label="{e(L['cs_label'])}" style="--cs:{L['cs']}px;--photo:url({L.get('photo', '')})">{imgs}</div>
      <div class="lg-bgs">{bgs}<span class="sp"></span><button type="button" data-guide aria-pressed="false">Show clear space</button></div>
    </div>
    <div style="display:flex;flex-direction:column;gap:12px">{notes}</div>
  </div>""", "Switch the grounds to see which file goes where. Show clear space draws the minimum margin.")


def logo_files(B):
    cards = []
    for i, f in enumerate(B["logo_files"]):
        cards.append(f"""<div class="kit-file" data-in style="{d(i, 180, 40)}">
      <div class="kit-file-v" style="background:{f['bg']}"><img src="{f['img']}" alt="" style="max-height:{f.get('h', 70)}px{';background:#fff;padding:12px 16px;border-radius:12px' if f.get('tile') else ''}"></div>
      <div class="kit-file-t"><b>{e(f['name'])}</b><small>{f['use']}</small><code>{e(f['master'])}</code>{dl(f['img'], f.get('dl', 'PNG'))}</div>
    </div>""")
    return slide("logo-files", "Logo files", head("logo files", f'Every lock-up, <span class="hl">ready to download.</span>') +
                 f'\n  <div class="kit-files" style="--n:{B.get("files_cols", 3)}">' + "".join(cards) + "</div>" +
                 (f'\n  <p class="bk-src">{B["logo_files_note"]}</p>' if B.get("logo_files_note") else ""),
                 "The download buttons give the web copy in this kit. For print, go back to the master path under each file.")


def logo_rules(B):
    R = B["logo_rules"]
    specs = "".join(f"<tr><th>{e(k)}</th><td>{v}</td></tr>" for k, v in R["specs"])
    mis = "".join(f'<div class="dn {"ok" if ok else "no"}" data-in style="{d(i, 240, 30)}"><div class="dn-v" style="{bg}">{v}</div><div class="dn-t">{t}</div></div>'
                  for i, (ok, bg, v, t) in enumerate(R["misuse"]))
    return slide("logo-rules", "Logo rules", head("logo rules", R["title"]) + f"""
  <div class="kit-2" style="grid-template-columns:.8fr 1.6fr;margin-top:22px;align-items:start">
    <table class="kit-tbl" data-in style="--d:200ms"><tbody>{specs}</tbody></table>
    <div class="bk-grid bk-g4" style="gap:12px">{mis}</div>
  </div>""", "The sizes and the common mistakes.")


def sw(name, hx, role, i, big=False, base=200):
    return (f'<div class="sw{" sw-big" if big else ""}" data-hex="{hx}" data-in style="{d(i, base, 40)}"><div class="sw-chip">{"" if not big else e(big)}</div>'
            f'<div class="sw-t"><b>{e(name)}</b><code>{hx}</code><span class="sw-rgb"></span><span class="sw-role">{role}</span><span class="sw-c"></span></div></div>')


def colour(B):
    C = B["colours"]
    n = len(C["primary"])
    cols = " ".join(["1.4fr"] * min(2, n) + ["1fr"] * max(0, n - 2))
    sws = "".join(sw(nm, hx, rl, i, big=("PRIMARY" if i == 0 else "ACCENT" if i == 1 else False)) for i, (nm, hx, rl) in enumerate(C["primary"]))
    ratio = "".join(f'<i style="--w:{w};--c:{c}"{" class=\"lt\"" if lt else ""}>{t}</i>' for t, w, c, lt in C["ratio"])
    return slide("colour", "Colour", head("03 · colour", C["title"]) + f"""
  <p class="kit-src" data-in style="--d:140ms;margin-top:10px">Click a colour to copy its hex. Contrast is measured live against white and the brand's own ink ({C['ink']}).</p>
  <div class="bk-grid" data-ink="{C['ink']}" style="grid-template-columns:{cols};margin-top:16px">{sws}</div>
  <p class="kit-sub" data-in style="--d:440ms;margin-top:18px">Proportion in use</p>
  <div class="bk-ratio" data-in style="--d:460ms;height:44px">{ratio}</div>""", C.get("notes", "Primary colours and their roles."))


def colour2(B):
    C = B["colours"]
    sws = "".join(sw(nm, hx, rl, i, base=180) for i, (nm, hx, rl) in enumerate(C["more"]))
    grads = "".join(f'<div class="bk-grad" style="height:64px;background:{css};{"color:" + fg if fg else ""}">{lab}</div>' for css, lab, fg in C.get("gradients", []))
    gr = f'<div class="bk-grid bk-g{len(C.get("gradients", [])) or 1}" data-in style="--d:560ms;margin-top:16px;gap:12px">{grads}</div>' if grads else ""
    return slide("colour-2", "Colour tokens", head("colour tokens", C["title2"]) + f"""
  <div class="bk-grid bk-g6 kit-sw-sm" data-ink="{C['ink']}" style="margin-top:20px;gap:12px">{sws}</div>{gr}""", C.get("notes2", "Every supporting value, with its role."))


def type_(B):
    out = []
    for i, f in enumerate(B["fonts"]):
        ws = "".join(f'<button type="button" data-w="{w}"{(" data-style=\"" + st + "\"") if st else ""}{" aria-pressed=\"true\"" if j == f.get("on", 0) else ""}>{lab}</button>'
                     for j, (w, st, lab) in enumerate(f["weights"]))
        lo, hi, v = f["size"]
        out.append(f"""<div class="ts" data-in style="{d(i, 200, 60)}">
      <div class="ts-head"><div class="ts-name" style="font-family:{f['css']}">{e(f['name'])}<small style="font-family:var(--f-body)">{f['role']}</small></div><div class="ts-glyph" style="font-family:{f['css']};{f.get('glyph', '')}">Aa</div></div>
      <div class="ts-line" style="font-family:{f['css']};{f.get('line', '')}">{f['sample']}</div>
      <div class="ts-ctl"><div class="bk-seg">{ws}</div><input type="range" min="{lo}" max="{hi}" value="{v}" data-size aria-label="Size"><span class="ts-px"></span></div>
      <p class="kit-src">{f['src']}</p>
    </div>""")
    cols = "1fr 1fr" if len(out) != 3 else "1fr 1fr 1fr"
    return slide("type", "Typography", head("04 · typography", B["type_title"], "Type into any sample, switch the weight, drag the size.") +
                 f'\n  <div class="bk-grid" style="grid-template-columns:{cols};margin-top:20px;gap:18px">' + "".join(out) + "</div>",
                 B.get("type_notes", "The families, weights and where the font files come from."))


def type_scale(B):
    rows = "".join(f'<div class="sc-row"><span class="k">{e(k)}</span><span class="s" style="{css}">{sample}</span><span class="m">{meta}</span></div>' for k, css, sample, meta in B["scale"])
    side = "".join(f'<div class="bk-card" data-in style="{d(i, 260, 60)}"><h3>{h}</h3><p class="bk-mini">{p}</p></div>' for i, (h, p) in enumerate(B["scale_side"]))
    return slide("type-scale", "Type scale", head("type scale", B["scale_title"]) + f"""
  <div class="kit-2" style="grid-template-columns:1.55fr 1fr;margin-top:20px;align-items:start">
    <div class="bk-card" data-in style="--d:200ms;padding:8px 24px">{rows}</div>
    <div style="display:flex;flex-direction:column;gap:14px">{side}</div>
  </div>""", "Sizes and settings as used on the website and in print.")


def ui(B):
    U = B["ui"]
    toks = "".join(f"<tr><th>{e(k)}</th><td><code>{e(v)}</code></td></tr>" for k, v in U["tokens"])
    ez = "".join(f'<div class="ez" data-in style="{d(i, 300, 40)};--fn:{c};--dur:{ms}ms"><div><b>{e(n)}</b><code>{e(c.replace("cubic-bezier", ""))} · {ms}ms</code></div><div class="ez-t"><i></i></div></div>' for i, (n, c, ms) in enumerate(U["eases"]))
    return slide("ui", "UI tokens", head("05 · ui tokens", U["title"], U["lead"]) + f"""
  <div class="kit-2" style="grid-template-columns:1.1fr 1fr;margin-top:20px;align-items:start">
    <div style="display:flex;flex-direction:column;gap:14px">
      <div class="bk-card" data-in style="--d:200ms"><p class="kit-sub">Buttons, live</p>{U['buttons']}</div>
      {ez}
    </div>
    <table class="kit-tbl" data-in style="--d:260ms"><tbody>{toks}</tbody></table>
  </div>""", "Values from the live site's stylesheet. Hover the buttons to see the real states.")


def imagery(B):
    I = B["imagery"]
    rules = "".join(f"<li>{r}</li>" for r in I["rules"])
    pics = "".join(f'<figure class="bk-pic bk-zoom" data-cap="{e(c)} · {e(p)}" data-in style="{d(i, 240, 30)};margin:0"><img src="{img}" alt="{e(c)}" loading="lazy"><figcaption>{e(c)}</figcaption></figure>'
                   for i, (img, c, p) in enumerate(I["photos"]))
    return slide("imagery", "Imagery", head("06 · imagery", I["title"]) + f"""
  <div class="kit-2" style="grid-template-columns:.75fr 1.6fr;margin-top:20px;align-items:start">
    <div class="bk-card" data-in style="--d:200ms"><p class="kit-sub">Style</p><ul class="kit-ul">{rules}</ul><p class="kit-src">{I['src']}</p></div>
    <div class="kit-lib">{pics}</div>
  </div>""", "The approved photo library. Click a picture for its source file.")


def formats(B):
    rows = "".join(f'<tr><td>{"<img src=" + chr(34) + t + chr(34) + " alt=" + chr(34) + chr(34) + " class=" + chr(34) + "bk-zoom kit-th" + chr(34) + ">" if t else ""}</td><th>{a}</th><td>{s}</td><td>{sp}</td></tr>' for a, s, sp, t in B["formats"])
    return slide("formats", "Formats", head("07 · formats", B["formats_title"]) + f"""
  <table class="kit-tbl kit-fmt" data-in style="--d:200ms;margin-top:20px"><thead><tr><th></th><th>Application</th><th>Size</th><th>Spec</th></tr></thead><tbody>{rows}</tbody></table>""",
                 "The sizes and layout rules for each application. Click a reference thumbnail to see it large.")


def words(B):
    W = B["words"]
    traits = "".join(f'<span class="kit-trait">{t}</span>' for t in W["traits"])
    use = "".join(f"<li>{x}</li>" for x in W["use"])
    avoid = "".join(f"<li>{x}</li>" for x in W["avoid"])
    sp = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in W["spelling"])
    return slide("words", "Wording", head("08 · wording", W["title"]) + f"""
  <div class="kit-traits" data-in style="--d:180ms">{traits}</div>
  <div class="kit-3" style="margin-top:18px">
    <div class="bk-dd" style="grid-template-columns:1fr 1fr;grid-column:span 2">
      <div class="bk-card" data-in style="--d:220ms"><h3>Words we use</h3><ul>{use}</ul></div>
      <div class="bk-card no" data-in style="--d:280ms"><h3>Avoid</h3><ul>{avoid}</ul></div>
    </div>
    <table class="kit-tbl" data-in style="--d:320ms"><tbody>{sp}</tbody></table>
  </div>""", "Voice in a line, and the spellings that must never change.")


def dodont(B):
    do = "".join(f"<li>{x}</li>" for x in B["do"])
    dont = "".join(f"<li>{x}</li>" for x in B["dont"])
    return slide("dodont", "Do's and don'ts", head("09 · do's and don'ts", 'The kit <span class="hl">on one page.</span>') + f"""
  <div class="bk-dd" style="margin-top:24px">
    <div class="bk-card" data-in style="--d:200ms"><h3>Do</h3><ul>{do}</ul></div>
    <div class="bk-card no" data-in style="--d:280ms"><h3>Don't</h3><ul>{dont}</ul></div>
  </div>""", "The summary to keep beside you.")


def masters(B):
    M = B["masters"]
    rows = "".join(f"<tr><th>{e(k)}</th><td><code>{e(v)}</code></td></tr>" for k, v in M["paths"])
    opens = "".join(f"<li>{x}</li>" for x in M["open"])
    return slide("masters", "Where the masters live", f"""  <div class="kit-close">
    <div>
      <span class="kicker" data-in style="--d:40ms">10 · masters</span>
      <h2 class="h-m" data-in style="--d:80ms">Where the <span class="hl">masters live.</span></h2>
      <table class="kit-tbl kit-tbl--dark" data-in style="--d:180ms;margin-top:22px"><tbody>{rows}</tbody></table>
      <p class="kit-src" data-in style="--d:240ms;color:rgba(255,255,255,.6)">{M['sources']}</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:18px;align-items:flex-end">
      <div class="bk-qr" data-in data-fx="scale" style="--d:260ms">{{{{qr:{M['qr']}:{M.get('qr_c', '#1F1F3D')}}}}}<b>{e(B['site'])}</b><small>The live site</small></div>
      <div class="kit-open" data-in style="--d:320ms"><b>Open items</b><ul>{opens}</ul></div>
    </div>
  </div>""", "Masters and sources. The open items need the brand owner's answer before print.", "dark", ' data-chrome="foot"')


def expand_kit(slug):
    import re
    B = KD.BRANDS[slug]
    out = "".join(f(B) for f in (cover, index, basics, logo, logo_files, logo_rules, colour, colour2, type_, type_scale, ui, imagery, formats, words, dodont, masters))
    return re.sub(r"\{\{dl:([^}]+)\}\}", lambda m: dl(m.group(1)), out)
