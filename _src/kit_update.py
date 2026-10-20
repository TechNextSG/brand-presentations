# -*- coding: utf-8 -*-
"""15 Oct 2026 live check: corrections and added detail for every kit (source: brand-presentations-research/update-2026-10-15.md).
Imported by site_build after kit_data; edits BRANDS in place."""
from kit_data import BRANDS


def setrow(rows, key, val):
    for i, (k, v) in enumerate(rows):
        if k == key:
            rows[i] = (k, val); return
    rows.append((key, val))


def setcol(lst, name, role=None, hx=None):
    for i, (n, h, r) in enumerate(lst):
        if n == name:
            lst[i] = (n, hx or h, role if role is not None else r); return


# ======================================================================================== TechNext
T = BRANDS["technext"]
T["updated"] = "Checked against technext.asia on 15 Oct 2026 (deployed branch origin/master ce82483b)."
setcol(T["colours"]["more"], "Sky", "Chip hover borders (the focus ring is Brand Blue).")
setcol(T["colours"]["more"], "Muted", "Captions; 5.9:1 on white.")
T["fonts"][0]["weights"] = [("500", "", "500"), ("600", "", "600"), ("700", "", "700"), ("800", "", "800")]; T["fonts"][0]["on"] = 3
T["fonts"][0]["role"] = "Display · loads 500/600/700/800 · h1 800 −0.025em, h2–h4 700 −0.015em"
T["fonts"][2]["role"] = "Hand · 600 1.55rem · lowercase kicker or one word · −1.2° on the site (−1.5° in decks)"
T["fonts"][2]["line"] = "color:#3167CA;transform:rotate(-1.2deg);transform-origin:0 50%"
for i, row in enumerate(T["scale"]):
    if row[0] == "Eyebrow":
        T["scale"][i] = ("Eyebrow", "font:700 12px/1 var(--f-body);letter-spacing:.12em;text-transform:uppercase;color:#62627A", "Odoo Ready Partner", "site 12 / 700 / .12em caps")
T["ui"]["buttons"] = ('<div class="isa-btnrow"><button type="button" class="tn-b p">Get a quotation {{icon:arrow}}</button><button type="button" class="tn-b g">Let\'s talk</button>'
                      '<button type="button" class="tn-b l">How we work</button></div>'
                      '<div class="tn-darkband"><button type="button" class="tn-b w">Get your free website {{icon:arrow}}</button><button type="button" class="tn-b ow">Talk to us</button></div>')
T["ui"]["tokens"] += [("Sizes", ".btn-lg 52 · pad 0 24 · 16px; .btn-sm 38 · pad 0 14 · 14px · r 10"),
                      ("Button motion", "hover −2px + white sheen (.7s) · press scale(.96) .12s · ripple from click · busy spinner"),
                      ("Focus", "outline 2px solid #3167CA · offset 2px · r 4"),
                      ("Links", "#3167CA, no underline; hover underline offset 3px · .btn-link 1.5px underline grows from left (.28s)"),
                      ("Form fields", "label Inter 600 13 ink · input 15/1.4 · 1px #E7E4E9 · r 8 · pad 10×12 · min-h 44 · focus blue border + 3px #DDE7F8 · invalid #D93A30"),
                      ("Header", "sticky 72 (64 ≤960) · rgba(255,255,255,.96) · hairline once scrolled · logo 170×34"),
                      ("Mega menu", "white · 0 28px 40px -36px rgba(31,31,61,.35) · .18s fade + 6px drop"),
                      ("Side tabs", "Set up meeting · Let's Talk · Ask Nexi · blue, r 0 12 12 0, Jakarta 700 14 (50 px circles ≤960)"),
                      ("Reveals", "translateY(14px) · .38s ease-out · 70ms apart"),
                      ("Breakpoints", "1100 · 960 · 640 · 420 (section 56, gutter 18 at ≤640)"),
                      ("Extra tokens", "--glass rgba(255,255,255,.72) · --gold #D69A00 · ::selection #CFDDF7")]
T["ui"]["lead"] = "Hover and press: lift 2 px, a sheen sweeps, press 0.96. Labels are the ones used most on the live site."
T["web"] = [("Page title", "Odoo Partner in Singapore &amp; the Philippines | TechNext"),
            ("Meta description", "TechNext is your Odoo, website and brand team in Singapore and the Philippines. You don't need to hire your own: we set it up and stay on after go-live."),
            ("H1 tag", "Odoo Ready Partner in Singapore &amp; the Philippines"),
            ("Navigation", "Solution ▾ · Industries ▾ · Odoo ▾ · Company ▾ · Nexi Explains · <b>Free website</b> (primary button)"),
            ("Solution menu", "ERP: Odoo ERP Implementation · CRM Development · Enterprise Solution — AI Solution: RAG Knowledge Assistants · Odoo + AI integrations · Workflow Automation · AI Chatbots — Marketing: Web Design &amp; Development · Social Media Management · Graphic &amp; Brand Assets — Technology: IoT Solutions · App Development · Networks"),
            ("Industries", "Medical · Travel · Retail · Ecommerce · Construction · F&amp;B · Manufacturing · Health &amp; Wellness"),
            ("Company menu", "About TechNext · Employee Hub · Careers · Blog · Events · Life at TechNext · Singapore HQ · Philippines · Vietnam"),
            ("Footer", "© 2026 TechNext Pte. Ltd. All rights reserved. · About · Careers · Blog · Privacy Policy · Terms of Service"),
            ("Contacts", "sales@technext.asia (site-wide, never hello@) · career@technext.asia · WhatsApp +65 8839 6998 · meetings technext.odoo.com/book/c82cf8a9"),
            ("Offices", "Singapore HQ, 261 Waterloo Street #03-36, Singapore 180261 · Main development and consulting hub, Taguig City · AI engineering hub, Ho Chi Minh City"),
            ("Social", "Facebook, Instagram, X, TikTok /technextasia · YouTube @technextasia · LinkedIn /company/technextasia"),
            ("Favicons", "favicon.ico (16/32/48) · favicon-32/48/96/192.png · apple-touch-icon 180×180"),
            ("Share image", "og-image.png 1200×630 · twitter summary_large_image · og:site_name TechNext"),
            ("Partner proof", "odoo.com/partners/technext-pte-ltd-28073844 · “Claude Partner” on the AI practice")]
T["tone"] = ["No need to hire your own team for Odoo, websites, branding or tech.", "From lead to reconciled cash, across five departments.", "Four practices. One team.",
             "Every Odoo app, one database.", "Tell us what slows you down.", "Configure. Migrate. Go live. Keep going.",
             "Where Odoo runs is a scoping decision, not a default.",
             "A short discovery call is enough to say which Odoo apps you need, in what order, and what it will take. No pitch before we understand the problem."]
T["ctas"] = [("Most used", ["Get a quotation (~270)", "Let's talk (125)", "Get your free website (99)", "Talk to us (82)", "Start with discovery (51)", "Book a discovery call (~11)"]),
             ("Also", ["Subscribe on YouTube", "How we work", "Browse all apps", "Watch Nexi Explains", "Ask Nexi", "See it run", "Free website"]),
             ("Forms and /get-started", ["Send inquiry", "Need a written quotation?", "Claim my free design", "Message us now", "Set a schedule"])]
T["a11y"] = [("Brand Blue #3167CA on white", "5.35", "AA"), ("White on Brand Blue", "5.35", "AA"), ("Body #4C4C63 on white", "8.33", "AAA"),
             ("Muted #62627A on white", "5.92", "AA"), ("Navy #1E4691 on Wash #EAF0FB", "7.84", "AAA"), ("Retired #8888A0 on white", "3.46", "fails (chevron stroke only)")]
T["a11y_notes"] = "Skip link “Skip to content” (blue pill) · prefers-reduced-motion respected · focus ring 2 px Brand Blue."
T["anatomy"] = [("Email signature", "Table layout, Arial/Helvetica. Name 20/900 #111 · 1px #ccc divider · logo sig/logo-h.png 110×22. Role “JOB TITLE • TECHNEXT PTE LTD.” 11/500 #888 +1.2px. Phone · email · technext.asia 12px #444 with icons. “Odoo ERP Solution and AI Automation” 12/700 #3167CA, “IoT • Apps • Networks” 11/600 #666. Social icons 26 px (FB, IG, LinkedIn, X, YouTube, TikTok). Banner sig/banner.png at 520×104, r 12. Confidentiality 10px #999. Copy for Gmail / Odoo / Export HTML. Never move sig/ (signatures hot-link it)."),
                ("Business card", "3.5 × 2 in (+1/8 in bleed = 3.75 × 2.25 in PDF). Front: contact side with a vCard QR. Back: brand side, white logo, signature line, “IoT · Apps · Networks”. Exports 600 dpi 2100×1200 and 1200 dpi 4200×2400, print PDF front + back. Fields: name, title, phone, email, website, address (optional)."),
                ("Staff ID card", "CR80 2.125 × 3.375 in with photo + barcode. Photo ground: Brand blue / Light / White, auto-frame. Office: Singapore HQ / Taguig City, Metro Manila / Ho Chi Minh City."),
                ("Call backgrounds and animated logo", "4 designs × Normal + Mirrored, 1920×1080. Animated logo GIF 512 px (slides, email) and 256 px (Gmail profile, light and blue).")]
T["masters"]["open"] = ["Original logo folder not found after the 10 Oct Drive reorganisation.", "No exact colour spec for Nexi.", "Deck-only values (−1.5° kicker, 13 px eyebrow) differ from the site (−1.2°, 12 px)."]
setrow(T["basics"], "Email", "sales@technext.asia (all site forms reply from it) · career@technext.asia for careers")

# Adviser voice (owner, 20 Oct 2026): "we are solution provider/expert adviser" - website, presentations and branding.
T["updated"] = T.get("updated", "") + " Voice updated 20 Oct 2026: solution provider and expert adviser."
T["basics"][2:2] = [("Positioning", "Solution provider and expert adviser for Odoo ERP, enterprise AI, digital marketing and technology (IoT · Apps · Networks)"),
                    ("Brand line", "“We advise first, then deliver the whole solution.” (company profile cover, home page)"),
                    ("Process line", "“Listen. Advise. Implement. Stay.” (technext.asia/advisers)"),
                    ("Advisers", "Six roles: Finance &amp; accounting · Sales, CRM &amp; service · Supply chain &amp; inventory · Manufacturing &amp; projects · AI &amp; automation · Website &amp; brand adviser (technext.asia/advisers)")]
setrow(T["basics"], "Hero line", "“We advise first, then deliver the whole solution.” (the older “No need to hire your own team for Odoo, websites, branding or tech.” stays as a supporting line)")
W = T["words"]
W["title"] = 'Expert adviser, <span class="hl">plain and concrete.</span>'
W["traits"] = ["Advises first", "Owns the whole solution", "Expertise you can name", "Plain", "Concrete", "Spoken to “you”", "One idea per slide or post"]
W["use"] = ["solution provider and expert adviser", "we advise first, then deliver", "we recommend what fits, and say why", "the same advisers from start to finish",
            "discovery call with an adviser", "solve (not fix)", "solutions (services only in menus and lists)", "standard Odoo first", "Odoo Ready Partner"]
W["avoid"] = ["“trusted advisor”, “world-class”, “leading”, “one-stop shop”", "advisor (US spelling): always adviser", "vendor / agency / reseller",
              "“we build” as the lead verb", "certified / gold / silver", "“free Odoo”", "jargon: leverage, synergy, best-in-class", "invented numbers", "ODOO in caps"]
T["voice_pillars"] = [("Diagnose before we prescribe", "We ask how the business runs, then recommend: what fits, what can wait, and what not to buy."),
                      ("Own the whole solution", "One accountable team from the advice to go-live and support. No hand-offs."),
                      ("Expertise you can name", "Advisers by domain, a reason behind every recommendation, standard Odoo first.")]
T["tone"] = ["We advise first, then deliver the whole solution.", "Solution provider and expert adviser, built around Odoo.", 
             "Fourteen solutions. We advise where to start.", "Five steps, the same advisers from start to finish."] + T["tone"]
T["ctas"][0] = (T["ctas"][0][0], T["ctas"][0][1] + ["Book a discovery call with an adviser (decks)"])

# ======================================================================================== HummingBeing
H = BRANDS["hummingbeing"]
H["updated"] = "Checked against hummingbeing.com on 15 Oct 2026 (main 4d8bb1a)."
setcol(H["colours"]["primary"], "Cream", "Section grounds (the page itself is white #FFFFFF).")
setcol(H["colours"]["primary"], "Gold dark", "Hover; gold text only at large sizes (3.06:1 on cream).")
setcol(H["colours"]["more"], "Link blue", "Text links (2.75:1 on white: an accessibility debt).")
H["colours"]["more"].append(("Footer", "#1E2028", "Footer ground (charcoal navy)."))
H["fonts"][1]["role"] = "Body 400 · 17 px / 1.75 · labels and buttons 700 caps"
H["fonts"].append(dict(name="Raleway", css="Raleway, Lato, sans-serif", role="Navigation · 400 .82rem +.4px · active gold 700 · header CTA 500", glyph="", line="",
                       sample="Home · About · Isabelle · Services · Events", weights=[("400", "", "400"), ("500", "", "500")], size=(13, 30, 16), src="Google Fonts (300/400/500). SIL OFL."))
H["type_notes"] = "Four families load: Playfair Display, PT Serif, Lato and Raleway (nav). Posters pair Playfair with Jost."
for i, row in enumerate(H["scale"]):
    if row[0] == "Body":
        H["scale"][i] = ("Body", "font:400 17px/1.75 Lato", "Come as you are.", "Lato 400 · 17 / 1.75")
H["ui"]["tokens"] = [t for t in H["ui"]["tokens"] if t[0] != "On dark"] + [
    ("On dark", "primary: gold border, white label → gold fill, navy label · default: rgba(255,255,255,.62) border, white → white fill, navy"),
    ("Hover / press", "lift 2px · 0 14px 34px -14px &lt;fill&gt; · press scale(.97) · arrow .btn-arr slides 4px"),
    ("Focus", "2px solid #F5A623 · offset 3px"),
    ("Forms", ".form-group label + input · focus border #F5A623, no outline · textarea min 130px"),
    ("Event states", ".btn-soldout #C0392B outline · .btn-ended #5B6472 · thumbs “Sold Out” / “Passed”"),
    ("Layout", "--hx-max 1180 · --hx-pad clamp(16px,5vw,64px) · footer grid 1.5fr 1fr 1fr 1fr"),
    ("Header detail", "fixed 86 (76 scrolled, 72 mobile) · transparent over hero with logo-dark.webp → white with logo-light.webp · hides on scroll-down · 46 px round hamburger")]
H["web"] = [("Page title", "TRE™ &amp; Somatic Coaching in Singapore &amp; Online | HummingBeing"),
            ("Meta description", "TRE™ (Tension &amp; Trauma Releasing Exercises), somatic coaching and mindfulness with Isabelle Claus Teixeira — in person in Singapore and Japan, and online."),
            ("Hero", "Release. <em>Renew.</em> Restore. — “Cognitive optimization, somatic decompression, neuroscience, and energetic mastery.”"),
            ("Navigation", "Home · About · Isabelle · Services ▾ (Holistic Mastermind Ecosystem · Global Certifications · Resilience Retreats) · Socials · Gallery · Events · <b>Book a Session</b>"),
            ("Footer", "logo-dark.webp 144×48 · footer line · “Part of Business and Human Development Consulting Pte Ltd” · services, about, Isabelle, socials, gallery, events, BHD Asia · bonjour@bhdasia.com · WhatsApp Us · Powered by TechNext"),
            ("Contacts", "bonjour@bhdasia.com · WhatsApp +81 80 6515 1778 · free chat calendly.com/bhdasia/30min"),
            ("Social (shared)", "Instagram isabelleclausteixeira_bhd · LinkedIn in/isabelleclausteixeira · YouTube @IsabelleClausTeixeira (no HummingBeing-own handle)"),
            ("Logo on site", "logo-dark.webp / logo-light.webp 688×168, shown 168×56 · alt “HummingBeing — Coaching &amp; Somatics”"),
            ("Favicons", "favicon.ico · favicon-32/16.png · apple-touch-icon 180×180"),
            ("Share image", "images/isabelle-her-story.jpg — declared 1200×630 but the file is 850×1280 (crops badly: fix)"),
            ("Events page", "Filters: All events · Singapore · Online · International · Certification · Workshops · views Grid / By month · archive “Past and Sold Out Events”")]
H["tone"] = ["Like the Hummingbird, You Are Built to Thrive", "The hummingbird beats its wings 200 times a minute — yet is never depleted.", "You Don't Need a Particular Story",
             "Come as You Are", "Curious? Let's Just Talk.", "Most personal development works from the neck up. We start in the body — where real change lives.",
             "You will never be asked to relive or narrate anything difficult here.", "A Place to Come Back to Yourself"]
H["ctas"] = [("Booking", ["Start with a Free Chat", "Book a Free Chat", "Book a Free Discovery Call", "Book Your Free Call", "Book a Session"]),
             ("Explore", ["Learn More", "Explore the Certification", "Find Your Practice", "Our Full Story", "Start Your Journey", "Come Back to Yourself", "Explore the Practices", "Find Your Way Back", "Meet Isabelle", "Explore BHD Asia"]),
             ("Events", ["Register", "Register — S$88", "Register now", "View Details", "See all events", "Browse Events", "Add to calendar", "Join Waitlist"])]
H["a11y"] = [("Navy #242E42 on gold", "6.71", "AA (button label)"), ("White on gold #F5A623", "2.03", "never"), ("Gold on navy deep", "8.01", "AAA (italic word on dark)"),
             ("Body #3D4250 on white", "10.03", "AAA"), ("Gold dark #C98000 on cream", "3.06", "large text only"), ("Link blue #2EA3F2 on white", "2.75", "fails (debt)"),
             ("Text light #8A8F9E on white", "3.23", "fails as text")]
H["a11y_notes"] = "Reduced motion removes the lifts, sheen and pointer fill · hover effects off on touch."
H["anatomy"] = [("Event page (.ce-*)", ".ce-hero navy-deep #1A2030, white text, crumbs .82rem #C7D2E6, badges Lato 800 .68rem caps → .ce-facts: 4 white tiles overlapping the hero by −38 px, r 14 → .ce-layout max 1160, grid 1fr 340px, gap 3rem: .ce-main (schedule, navy .ce-person cards r 12) + sticky .ce-side (poster r 14 with lightbox, .ce-box white r 14, price tiers #F6F7FA r 9) → “Joining a session online? Prepare your space” → “Other upcoming events”. Mobile: fixed .ce-bar CTA, r 16. Edit events only in events.html."),
                ("Elegant poster", "2160×2880. Playfair Display + Jost, navy #2F3D65 + gold, hairlines, arch photo frame, one footer strip (date, price, URL, small QR). Titles verbatim. Lock-up BHD mark | HummingBeing."),
                ("Website event card", "1920×1080, light grey/white ground (10 styles), LED BY block, no QR. Keep clear: top-left 620×220, top-right x>1660 y<300, bottom-left x<720 y>900."),
                ("Podcast thumbnail", "1280×720 · “THE HUMMINGBEING PODCAST” · cream #FBF6EE, gold rings and arch, Playfair navy #1F2A4F, Jost names · logo row HB | BHD mark | guest.")]
H["masters"]["open"] = ["No vector master of the full logo.", "Share image declared 1200×630 but is 850×1280.", "ICF credits: “CCEUs” (most pages) vs “CCEs” (14 Oct wording).",
                        "The certification poster says TRE®: fix before reuse.", "/events still features the 8 Oct event (15 Oct)."]
H["masters"]["sources"] = "Compiled from hummingbeing.com (checked 15 Oct 2026), styles.css and the Isabelle brand guide. “30 years” is Isabelle's figure everywhere; “25+” is Simba's."

# ======================================================================================== BHD Asia
B = BRANDS["bhdasia"]
B["updated"] = "Checked against bhdasia.com on 15 Oct 2026 (master 58607ff)."
setrow(B["basics"], "Legal name", "Business &amp; Human Development Consulting Pte Ltd (footer, schema) · “Business and Human Development…” on /about — pick one")
setrow(B["basics"], "Address", "50 Raffles Place, Singapore Land Tower #30-00, Singapore 048623")
B["fonts"][0]["role"] = "Web loads 400–800 · display 800 −2% · headings 700 · 900 is for social posts only"
B["fonts"][0]["weights"] = [("400", "", "400"), ("700", "", "700"), ("800", "", "800"), ("900", "", "900 (posts)")]
B["fonts"][0]["sample"] = 'Build <span style="color:#8F5A00">Stronger</span> Leaders.'
B["fonts"][0]["src"] = "Google Fonts Figtree 400–800. Sora and DM Sans still load but are overridden (cleanup debt). SIL OFL."
B["scale_title"] = 'Title Case, <span class="hl">one amber-ink word.</span>'
B["scale"] = [("Display", "font:800 40px/1.05 Figtree;letter-spacing:-.02em", 'Build <span style="color:#8F5A00">Stronger</span> Leaders.', "Figtree 800 · −2% · accent amber-ink #8F5A00"),
              ("Heading", "font:700 26px/1.15 Figtree;letter-spacing:-.02em", "Three Pillars of Human Development", "700 · −.02em · Title Case"),
              ("Social", "font:900 30px/1.05 Figtree", 'Build <span style="color:#F2A100">stronger</span> leaders.', "posts: 80–92 px · 900 · marigold word"),
              ("Event H1", "font:700 26px/1.1 Figtree;letter-spacing:-.02em", "Become a Certified TRE™ Provider", ".evt-hero 38 / 700"),
              ("Body", "font:400 17px/1.65 Figtree", "All engagements start with a conversation.", "17 / 1.65"),
              ("Badge", "font:700 11px/1 Figtree;letter-spacing:.12em;text-transform:uppercase;color:#14244A", "Singapore · Certification", ".evt-badge 11 / 700 / .12em"),
              ("Nav", "font:600 15px/1 Figtree;color:#14244A;text-decoration:underline;text-decoration-color:#FFB21A;text-decoration-thickness:2px;text-underline-offset:6px", "Services", "15 / 600 · marigold underline")]
B["scale_side"] = [("Title Case, never uppercase", "Live headings and buttons are Title Case (“Book a Discovery Call”, “Our Services”); text-transform none."),
                   ("Accent colour", "On the site the highlighted hero word is amber-ink #8F5A00 (5.6:1). Marigold text is for posts (large or on dark) only."),
                   ("Icons", "Inline SVG, stroke 1.6–2, round caps, amber ink on peach tiles. No emoji.")]
B["words"]["traits"] = ["Confident", "Warm", "Specific", "People, not products", "Title Case, never uppercase"]
B["do"] = ["Warm light surfaces; marigold is the action colour.", "Ink text on marigold; amber-ink #8F5A00 for orange text and the accent word.", "Figtree everywhere; Title Case, never uppercase.",
           "The two-bar accent once per layout.", "The mark on a white tile over dark or photos.", "TRE™ in every visible line."]
B["dont"] = ["Marigold or sun as text on light.", "The full-colour mark straight on navy.", "Recolour or shadow the bars.", "Uppercase buttons.", "Stock boardrooms.", "The superseded navy/amber + Sora palette."]
B["ui"]["tokens"] = [t for t in B["ui"]["tokens"] if t[0] not in ("Primary", "Secondary", "Header")] + [
    ("Primary", "#FFB21A · ink · 1.5px #FFB21A · r 999 · hover bloom to #F2A100 (.8s) · −2px · 0 14px 30px -14px rgba(214,140,0,.7) · press .98"),
    ("Secondary", "border rgba(20,36,74,.18) · bg rgba(255,251,244,.7) → #FDECCF + marigold border; in heroes/dark cards: white outline → white fill, ink"),
    ("Header", "rgba(255,251,244,.88) + blur(12px) · border rgba(239,227,208,.9) · logo bhd-logo.svg 42 px + “BHD Asia” · CTA pill “Contact”"),
    ("Footer", "#FBF3E6 · text #4F4A45 · top border #EFE3D0"),
    ("Focus", ":focus-visible outline #F2A100"),
    ("Forms", "border #A38B66 (3.16:1 on ivory) · Figtree · marigold pill submit"),
    ("Dark CTA cards", "links sun #EECB36 · buttons fill to sun"),
    ("Breakpoints", "375 · 480 · 600 · 767/768 · 900 · 980")]
B["web"] = [("Page title", "Executive Coaching &amp; HR Consulting in Singapore | BHD Asia"),
            ("Meta description", "Executive coaching, HR consulting and TRE™ resilience programmes from Singapore since 2012. Co-designed leadership development for organisations worldwide."),
            ("Hero", "Build Stronger Leaders. Develop Resilient Organisations. — “Boutique HR consulting, executive coaching, and resilience building — co-designed around your people, worldwide.”"),
            ("Page H1s", "/about “Built on Diversity. Driven by People.” · /services “Coaching &amp; Leadership Services, Tailored for You” · /events “TRE™ Events &amp; Workshops”"),
            ("Navigation", "Home · Services · About · Events · Partners · Contact · <b>Contact</b> (pill)"),
            ("Footer", "brand line · legal name · nav · Privacy Statement · Terms &amp; Conditions · Code of Practice · Inclusivity Statement · address · phone · bonjour@ · “Book a Discovery Call →” · TechNext"),
            ("Contacts", "bonjour@bhdasia.com · +81 806515 1778 (footer grouping) · calendly.com/bhdasia/tre-certification-intake-call"),
            ("Social", "Facebook /bhdasia · Instagram isabelleclausteixeira_bhd · LinkedIn in/isabelleclausteixeira · YouTube @IsabelleClausTeixeira"),
            ("Team (as shown)", "Isabelle Claus Teixeira, Co-Founder and Director · Dr. Jasmine Low, Organisational Psychologist &amp; Systems Coach · Simba Stenqvist, Somatic Practitioner &amp; TRE™ Specialist · Rina Ho, Executive Coach &amp; TRE™ Practitioner"),
            ("Favicons", "favicon.ico · favicon-192.png · apple-touch-icon 180×180 (favicon.svg in repo, not linked)"),
            ("Share image", "isagrey.jpg — declared 700×467 but the file is 800×800"),
            ("Events page", "Views Grid / By month · pills All Events · Singapore · Romania · Certification · “All ticket sales are final — tickets are non-refundable and non-cancellable.”")]
B["tone"] = ["Build Stronger Leaders. Develop Resilient Organisations.", "Co-designed, bespoke solutions built around your people — not off-the-shelf programmes.",
             "No off-the-shelf programmes. Everything is co-designed.", "We begin every engagement with a discovery conversation — no obligation, no pitch decks.",
             "Book a free 30-minute discovery call. We listen to your challenges and, only if there is a genuine fit, propose a programme design.",
             "Built on Diversity. Driven by People.", "With our partners and clients, we role model collaboration versus competition.", "All engagements start with a conversation. No commitment required."]
B["ctas"] = [("Booking", ["Book a Discovery Call", "Book a Free Discovery Call", "Schedule a Free 1:1", "Enquire About Org Dev", "Enquire About Resilience", "Enquire About Coaching", "Book a Call", "Email Us"]),
             ("Explore", ["Our Services", "Explore Our Services", "View All Services", "Meet Isabelle →", "Explore Org Development", "Explore Resilience Building", "Explore Individual Coaching", "Show all clients", "View Upcoming Events"]),
             ("Events", ["View All Event Details →", "Register →", "Register Now →", "Details →", "Browse Events", "Add to calendar", "Join Waitlist", "View Event"])]
B["a11y"] = [("Ink on marigold", "8.43", "AAA (button label)"), ("Amber-ink #8F5A00 on ivory", "5.61", "AA"), ("Warm body on ivory", "8.49", "AAA"),
             ("Warm muted on ivory", "5.19", "AA"), ("Marigold on white", "1.80", "never as text"), ("Form border #A38B66 on ivory", "3.16", "passes 3:1 non-text")]
B["a11y_notes"] = "Focus outline #F2A100 · reveals ≤ 20 px, hover lift ≤ 3 px, tilt ≤ 2° · reduced motion respected."
B["anatomy"] = [("Event page (.evt-*)", ".evt-hero min-h 480, poster as cover under an ivory wash (90°, .96 → .08), H1 38/700 −.02em ink · badges .evt-badge 11/700 caps pill (-loc marigold + ink, -type white 15%) · .evt-hero-sub 16/1.75 + CTAs → .evt-facts on sand #FBF3E6 → .evt-layout: .evt-main sections + .evt-sidebar .evt-reg-card (head, body, form, refund note, alt). The event layer reads window.BHD_EVENTS (status chip, related grid, past notice, phone booking bar)."),
                ("Social post", "2160×2880. BHD logo + name top-left; partner top-right in a white pill; two-bar eyebrow; Figtree 900 headline with one marigold word; numbered cards (1 marigold, 2 red, 3 navy); URL bottom-left with a red/navy dash; “Singapore · since 2012” bottom-right. Logo shapes can become the scene."),
                ("Website event card", "Shared HummingBeing card design (1920×1080, light, no QR) as card-*.webp, live since 12 Oct.")]
B["masters"]["open"] = ["Original logo vector missing; the SVG is a trace.", "Legal name written with “&amp;” and “and”.", "Share image declared 700×467 but is 800×800.",
                        "ICF credits: “CCEUs” vs “CCEs”.", "Home countdown still shows 26–27 Sep Module 2 (15 Oct)."]
B["masters"]["sources"] = "Compiled from bhdasia.com (checked 15 Oct 2026), style.css (warm light theme, v13) and the Isabelle brand guide."

# ======================================================================================== TRE in Singapore
R = BRANDS["tre-singapore"]
R["updated"] = "Checked against tre-in-singapore.com on 15 Oct 2026 (main 1d3466d)."
R["fonts"][0]["role"] = "H1 700 upright −.025em, accent em italic · headings 700 −.015em · stats 800 · self-hosted 700/800 + italics"
R["fonts"][0]["weights"] = [("700", "", "700"), ("800", "", "800"), ("700", "italic", "700 italic"), ("800", "italic", "800 italic")]; R["fonts"][0]["on"] = 0
R["fonts"][0]["sample"] = 'Strengthen Resilience. <em style="color:#8B6B45">Improve Wellbeing.</em>'
R["scale_title"] = 'Upright 700, <span class="hl">italic accent.</span>'
R["scale"] = [("Hero H1", "font:700 34px/1.05 'Plus Jakarta Sans';letter-spacing:-.025em;color:#1C3D7A", 'Release Stress. <em style="color:#8B6B45">Improve Wellbeing.</em>', "clamp(2.2rem,4.6vw,3.5rem) · 700 · em gold on navy, bronze on light"),
              ("Heading", "font:700 26px/1.15 'Plus Jakarta Sans';letter-spacing:-.015em;color:#1C3D7A", "One hub for TRE™ in Singapore", "700 · −.015em"),
              ("Stat", "font:800 34px/1 'Plus Jakarta Sans';letter-spacing:-.03em;color:#1C3D7A", "7", "40 / 800 · navy"),
              ("Body", "font:400 16px/1.65 Inter", "Seven exercises, one natural reflex.", "Inter 16 / 1.65"),
              ("Badge", "font:700 11.5px/1 'Plus Jakarta Sans';letter-spacing:.04em;text-transform:uppercase;color:#8B6B45", "Certified provider", ".72rem caps .04em"),
              ("Link arrow", "font:700 14.5px/1 'Plus Jakarta Sans';color:#1C3D7A", "Explore the pathway →", ".92rem 700 · bronze arrow slides 5 px"),
              ("Button", "font:700 15px/1 'Plus Jakarta Sans'", "See how TRE™ works", ".93rem / 700")]
R["do"] = ["Navy fields, cream grounds, bronze and gold lines.", "One orange CTA in view, navy-ink label.", "Upright 700 headlines; the accent italic: gold on navy, bronze on light.",
           "The logo on white or a white panel; keep “Singapore” attached.", "TRE™ in every visible line.", "Offer both paths: provider or event, and the intake call."]
R["ui"]["buttons"] = (f'<div class="isa-btnrow"><button type="button" class="tre-btn p">See how TRE™ works {{{{icon:arrow}}}}</button><button type="button" class="tre-btn n">Book a call</button><button type="button" class="tre-btn o">Explore the pathway</button></div>'
                      '<div class="tre-field" style="height:120px;margin-top:12px;background-image:url(assets/img/tre/photo-hero.jpg)"><p class="cap"><b>Release, made visible.</b>charge → release → settle</p></div>')
R["ui"]["eases"] = [("--ease", "cubic-bezier(.2,.7,.2,1)", 320), ("--ease-out", "cubic-bezier(.16,1,.3,1)", 600)]
R["ui"]["tokens"] = [t for t in R["ui"]["tokens"] if t[0] not in ("Primary",)] + [
    ("Primary", "orange #E08A2E · navy-ink label (6.1:1; white 2.7:1 never ships) · sheen .6s · arrow 4 px"),
    ("Small / light / ghost", "small 38 · .65rem 1.05rem · .84rem; light = white fill navy text; ghost-light = white text rgba(255,255,255,.55)"),
    ("Hover / press", "lift 2 px 320ms · press .98 180ms"),
    ("Focus", "3px solid gold #C9A45C · offset 3px"),
    ("Forms", "Inter 1rem · pad .85rem 1rem · min-h 48 · 1px #E4DFD6 · r 10 · orange caret · label Jakarta 700 .8rem navy → bronze · focus navy + 4px gold 30% · error #B9412F"),
    ("Header", "sticky white 94% (98% scrolled) · nav Jakarta 600 .92rem, 2 px gold underline · logo 214 webp at 107×58 (46 scrolled) · CTA “Book a call”"),
    ("Footer", "navy-ink #0F1F3D · text #B9C5DA · social 38 px circles fill gold"),
    ("Extra tokens", "--brown #5F4630 (“Singapore”) · --cream-2 #F2E9DB · --green #2F8F5B · --red #B9412F · --on-navy #DBE3F1 · shadow-cta 0 14px 26px -14px rgba(15,31,61,.6)"),
    ("Breakpoints", "380 · 480 · 520 · 560 · 600 · 640 · 760 · 900 · 980")]
R["logo_files"][0]["use"] = "The master (715×389). The header uses logo-tre-singapore-214.webp (214×116) at 107×58."
R["web"] = [("Page title", "TRE™ Singapore — Tension &amp; Trauma Releasing Exercises"),
            ("Meta description", "Learn TRE™ (Tension &amp; Trauma Releasing Exercises) in Singapore: find a certified provider, join a workshop or train to become a Global TRE™ Certified Provider."),
            ("Hero", "Release Stress. Strengthen Resilience. <em>Improve Wellbeing.</em> — “Learn TRE™ — Tension &amp; Trauma Releasing Exercises — with certified providers in Singapore, or train to become one.”"),
            ("Page H1s", "/about “A community hub for TRE™ practitioners in Singapore” · /education “Learn TRE™ — and learn to teach it”"),
            ("Navigation", "Home · About · Education · Providers · Events · Blog · Contact · <b>Book a call</b> · phone sheet ≤980 px full-screen navy-ink"),
            ("Footer", "Explore: Home · Events · About · Blog · Education · Contact · Online session guide · Providers · Get listed · Certification · HummingBeing — Contact: bonjour@bhdasia.com · +81 80 6515 1778 (WhatsApp) — “© 2026 Business &amp; Human Development Consulting Pte Ltd · TRE™ in Singapore” + trademark line · Powered by TechNext"),
            ("Social (shared)", "Facebook /bhdasia · Instagram isabelleclausteixeira_bhd · LinkedIn in/isabelleclausteixeira · YouTube @IsabelleClausTeixeira"),
            ("Schema", "alternateName “TRE Singapore” · parent “Business &amp; Human Development Consulting Pte Ltd” (BHD Asia) · 50 Raffles Place #30-00, 048623"),
            ("Favicon", "favicon.svg only (a drawn globe, not from the official artwork) · no PNG or apple-touch icon"),
            ("Share images", "og-cover.jpg 1200×630 (home) · assets/img/og/&lt;page&gt;.jpg 1200×630 per page, with provenance sidecars"),
            ("Certification", "Module 1 “2-day workshop + 4 online sessions · 21 ICF CCEUs · Singapore 27–28 Feb 2027” · Module 2 3–4 Jul 2027 · Module 3 30–31 Oct 2027 · early-bird until 31 Dec 2026")]
R["tone"] = ["Your body already knows how to let go", "One hub for TRE™ in Singapore",
             "Whether you want to try TRE™ for the first time, book a provider for your team, or train to teach it yourself — start here.",
             "You never need to talk about what happened. You control the intensity, and you can stop at any moment.",
             "Fight, flight — and the reset the body was designed for", "From Fortune 100 boardrooms to the mat", "Science-backed, body-first, people-centred",
             "I don't do this work from a distance. I've walked through it myself."]
R["ctas"] = [("Primary routes", ["See how TRE™ works", "Find a certified provider", "Book a call", "Book a free call", "Book a certification intake call", "Certification pathway", "Start with the basics", "Meet the providers", "Get listed"]),
             ("Secondary links", ["Browse providers", "See upcoming events", "Explore the pathway", "How TRE™ works", "Read the beginner's guide", "All providers", "All events", "Practice circles", "All articles"]),
             ("Contact", ["Contact us", "Visit HummingBeing", "Email bonjour@bhdasia.com"])]
R["a11y"] = [("Navy-ink on orange", "6.11", "AA (button label)"), ("White on orange", "2.68", "banned"), ("Bronze on white", "4.90", "AA"),
             ("Gold on navy-ink", "6.97", "AA (accent on dark)"), ("Gold on white", "2.35", "never text on light"), ("Muted #5F6B7D on white", "5.40", "lightest text allowed"), ("Ink on white", "15.4", "AAA")]
R["a11y_notes"] = "Site-wide motion pause switch · reduced motion respected · every “TRE™” in text opens an explainer bubble."
R["anatomy"] = [("Hero (.hx, six layers)", "1 real session photo, 32 s push-in 1.04 → 1.12 · 2 wordmark-navy grade 42% · 3 navy-ink wash (92% left → 10% right) · 4 tremor field · 5 copy settles from a 6 px blur + 14 px rise over .95 s, 90 ms apart · 6 photo credit .74rem white 78% after a 22 px gold hairline. Min-height clamp(500px,68vh,720px)."),
                ("Record pages", "events/* and facilitators/*: split hero with the poster (16:9) or portrait (1:1) in a 16 px window on the right. Event sections: Who it is for · Programme · What is included · Fees · Facilitators. Provider: Highlights · Sessions and services · Contact. Record cards: paper, 1px line-2, r 16, 24 px, navy primary (never orange), at most 2 badges."),
                ("Named rules (DESIGN.md)", "The One Orange Rule · The Navy-Ink Label Rule · The Drawn Gold Rule · The Tinted Ink Rule · The Window Rule · The Charge-Release-Settle Rule · The Clear Faces Rule.")]
R["masters"]["open"] = ["TRE® in the logo vs TRE™ in text.", "No vector or white logo; favicon is not from the artwork.", "ICF credits: “CCEUs” vs “CCEs”.", "“Licensee” status undocumented."]
R["masters"]["sources"] = "Compiled from tre-in-singapore.com (checked 15 Oct 2026), style.css, layer.css, DESIGN.md and the Isabelle brand guide."
