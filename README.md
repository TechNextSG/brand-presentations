# TechNext brand guidelines

Unlisted (`noindex`, robots Disallow): https://technextsg.github.io/brand-presentations/brand/index.html

Since 9 Nov 2026 this site shows the **TechNext** brand only, as one brand book in the XXVIII brand-book format
(fixed chapter rail with Roman numerals, live colour contrast, type tester, downloads). The other kits moved to their own books:

| Old page | Now |
|---|---|
| `index.html`, `technext.html` | redirect to `brand/index.html` |
| `hummingbeing.html` | https://technextmarketing.github.io/hummingbeing/brand/index.html |
| `bhdasia.html` | https://technextmarketing.github.io/bhdasia/brand/index.html |
| `tre-singapore.html` | https://technextmarketing.github.io/tre-in-singapore/brand/index.html |

## The book

`brand/index.html` + `brand.css` + `brand.js`, hand-written (no build step). Assets: `brand/img` (display WebP/PNG),
`brand/logo` (master SVG/PNG + favicons), `brand/fonts` (woff2), `brand/exports` (tokens CSS, palette JSON, call background).
Bump `?v=` on brand.css / brand.js when they change.

Facts come from technext.asia (site.css tokens, live copy) and the owner's brand rules. Retired: `_src/build.py` / `site_build.py`
(the old four-kit generator) - do not re-run it, it would bring the old list back.
