"""Full-page shots of the brand kit pages (desktop 1440 and phone 390), plus console errors and horizontal overflow."""
import base64, contextlib, pathlib, sys
sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/technext-presentations/scripts"))
from _cdp import serve, Chrome  # noqa: E402

R = pathlib.Path.home() / "ClaudeWork/brand-presentations"
OUT = pathlib.Path.home() / "ClaudeWork/qa/brand-kits"; OUT.mkdir(parents=True, exist_ok=True)
pages = sys.argv[1:] or ["index", "technext", "hummingbeing", "bhdasia", "tre-singapore"]
with serve(R) as base:
    for w, h, tag in [(1440, 900, "d"), (390, 844, "m")]:
        with Chrome(w=w, h=h, mobile=(tag == "m")) as c:
            for p in pages:
                c.errors.clear()
                c.open(base + p + ".html", settle=1.0); c.images_loaded()
                H = c.ev("document.documentElement.scrollHeight"); over = c.ev("document.documentElement.scrollWidth > innerWidth")
                c.call("Emulation.setDeviceMetricsOverride", width=w, height=min(H, 16000), deviceScaleFactor=1, mobile=(tag == "m"))
                c.sleep(.6)
                data = c.call("Page.captureScreenshot", format="jpeg", quality=70, captureBeyondViewport=True)["data"]
                (OUT / f"{p}-{tag}.jpg").write_bytes(base64.b64decode(data))
                c.call("Emulation.setDeviceMetricsOverride", width=w, height=h, deviceScaleFactor=1, mobile=(tag == "m"))
                print(f"{p:14s} {tag} h={H} overflow={over} errors={c.errors[:3]}")
