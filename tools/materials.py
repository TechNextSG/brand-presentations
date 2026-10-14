# -*- coding: utf-8 -*-
"""Build the "All materials" library from an inventory JSON: {brand: [{cat, title, path, fmt, w, h, kb, official}]}.
Copies each file up to MAX_MB into downloads/<brand>/ (originals, for the Download buttons), writes a 160 px thumbnail for
pictures into assets/img/mat/<brand>/, zips each brand's files into downloads/<brand>-brand-kit.zip, and writes _src/materials.json.
Run: python tools/materials.py <inventory.json>   then   python -B _src/build.py"""
import hashlib
import json
import pathlib
import re
import shutil
import sys
import zipfile

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAX_MB = 8
PICS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
SAFE = re.compile(r"[^a-z0-9._-]+")

inv = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
out = {}
for brand, items in inv.items():
    dl_dir = ROOT / "downloads" / brand; th_dir = ROOT / "assets/img/mat" / brand
    shutil.rmtree(dl_dir, ignore_errors=True); shutil.rmtree(th_dir, ignore_errors=True)
    dl_dir.mkdir(parents=True); th_dir.mkdir(parents=True)
    seen, rows, names = set(), [], set()
    for it in items:
        src = pathlib.Path(it["path"])
        row = {k: it.get(k) for k in ("cat", "title", "path", "fmt", "w", "h", "kb", "official")}
        row["fmt"] = (row.get("fmt") or src.suffix.lstrip(".")).lower()
        if src.is_file():
            h = hashlib.md5(src.read_bytes()).hexdigest()
            if h in seen:
                continue
            seen.add(h)
            row["kb"] = row.get("kb") or round(src.stat().st_size / 1024)
            name = SAFE.sub("-", src.name.lower()).strip("-")
            base, ext = name.rsplit(".", 1) if "." in name else (name, "")
            n = 2
            while name in names:
                name = f"{base}-{n}.{ext}"; n += 1
            names.add(name)
            if src.stat().st_size <= MAX_MB * 1024 * 1024:
                shutil.copy2(src, dl_dir / name)
                row["file"] = f"downloads/{brand}/{name}"
            if src.suffix.lower() in PICS:
                try:
                    im = Image.open(src); im.seek(0); im = im.convert("RGBA")
                    row["w"], row["h"] = row.get("w") or im.width, row.get("h") or im.height
                    im.thumbnail((320, 240))
                    bg = Image.new("RGB", im.size, "#ffffff"); bg.paste(im, mask=im.split()[3])
                    tn = th_dir / (name.rsplit(".", 1)[0] + ".jpg"); bg.save(tn, quality=78, optimize=True)
                    row["thumb"] = f"assets/img/mat/{brand}/{tn.name}"
                except Exception as ex:  # a broken or odd file still gets listed
                    print("  no thumb:", src.name, ex)
        elif src.is_dir():
            row["folder"] = sum(1 for f in src.rglob("*") if f.is_file())
            row["fmt"] = "folder"
        else:
            print("  missing (listed as source only):", src)
        rows.append(row)
    out[brand] = rows
    z = ROOT / "downloads" / f"{brand}-brand-kit.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for r in rows:
            if r.get("file"):
                zf.write(ROOT / r["file"], f"{brand}-brand-kit/{SAFE.sub('-', r['cat'].lower()).strip('-')}/{pathlib.Path(r['file']).name}")
    print(f"{brand:14s} {len(rows):3d} listed · {sum(1 for r in rows if r.get('file')):3d} downloadable · zip {z.stat().st_size / 1048576:.1f} MB")
(ROOT / "_src/materials.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
