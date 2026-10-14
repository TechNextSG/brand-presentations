# Brand kits

Brand kit compilations, presentation style,, unlisted (`noindex`), on the TechNext deck engine (copied from `technext-presentations`).
Live: https://technextsg.github.io/brand-presentations/

| Deck | Brand | Slides |
|---|---|---|
| [technext.html](technext.html) | TechNext | 16 |
| [hummingbeing.html](hummingbeing.html) | HummingBeing | 16 |
| [bhdasia.html](bhdasia.html) | BHD Asia | 16 |
| [tre-singapore.html](tre-singapore.html) | TRE™ in Singapore | 16 |

## Build

Every deck is generated from `_src/kit_data.py` by `_src/kit.py` (same 16 sections per brand). Edit the data, `assets/`, then `python -B _src/build.py`. Root `*.html` and `s-*.html` are generated.
Bump `ASSET_V` in `_src/build.py` whenever a file under `assets/` changes.

- `assets/brand.css|js`: the shared kit (swatches that copy and measure contrast, logo grounds and clear space, type tester, flip cards, zoom, motion curves).
- `assets/b-<brand>.css`: each brand's tokens and slides; the deck itself is dressed in that brand.
- QA: `TN_DECKS=~/ClaudeWork/brand-presentations python ~/.claude/skills/technext-presentations/scripts/deck_check.py <deck> --shots`.
- Preview: launch config `brand-books`, port 3971.

Facts come from the live sites and the brands' own repos (research notes in `~/ClaudeWork/brand-presentations-research/`).
