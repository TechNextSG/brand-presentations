# Brand kits

Brand kit compilations in TechNext branding, unlisted (`noindex`): https://technextsg.github.io/brand-presentations/

| Page | Brand |
|---|---|
| [technext.html](technext.html) | TechNext |
| [hummingbeing.html](hummingbeing.html) | HummingBeing |
| [bhdasia.html](bhdasia.html) | BHD Asia |
| [tre-singapore.html](tre-singapore.html) | TRE™ in Singapore |

Each page has the same ten sections: basics, logo (viewer, files with downloads, rules), colour (tokens with live contrast), typography,
UI tokens, imagery, formats, wording, do's and don'ts, masters and sources.

## Build

Edit `_src/kit_data.py` (all content) or `assets/kit.css|js`, then `python -B _src/build.py`. The root `*.html` files are generated
by `_src/site_build.py`. Bump `V` in `_src/site_build.py` when anything under `assets/` changes. Print / PDF from the browser (print styles included).
Research notes: `~/ClaudeWork/brand-presentations-research/`.
