#!/usr/bin/env python3
"""Builds the StoryMe static site into ./dist. Shared header/footer live here."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SITE = "StoryMe"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,600..900,100,1;1,9..144,600..900,100,1&family=Kalam:wght@400;700&family=Nunito+Sans:wght@400;600;700;800&display=swap">')

SPARK = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path fill="#F4C95D" d="M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4z"/></svg>'
SPARK_TEAL = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path fill="#0F8C7A" d="M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4z"/></svg>'
STAR_LI = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4z"/></svg>'
WAND = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 4-11 11 5 5 11-11z"/><path d="M18 2v2M22 6h-2M20 2l-1 1"/></svg>'
PLUS = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F4C95D" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>'
MOON = '<svg class="moon floaty" width="{s}" height="{s}" viewBox="0 0 70 70" aria-hidden="true"><path d="M48 8a28 28 0 1 0 14 40A24 24 0 0 1 48 8z" fill="{c}"/></svg>'


def logo(ink):
    return ('<a class="logo" href="index.html" aria-label="StoryMe home">'
            f'<svg width="40" height="40" viewBox="0 0 40 40" fill="none" stroke="{ink}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M5 11c5-2 10-2 15 2v20c-5-4-10-4-15-2z"/><path d="M35 11c-5-2-10-2-15 2v20c5-4 10-4 15-2z"/>'
            '<path d="M28 2l1.2 3 3 1.2-3 1.2L28 10.4l-1.2-3-3-1.2 3-1.2z" fill="#E0AE2C" stroke="#E0AE2C"/></svg>'
            '<span>StoryMe</span></a>')


NAV = [("how", "How the magic works", "how-it-works.html"),
       ("styles", "Art styles", "art-styles.html"),
       ("worlds", "Worlds", "worlds.html"),
       ("pricing", "Pricing", "pricing.html"),
       ("faq", "FAQ", "faq.html")]


def header(current, theme="dark"):
    ink = "#1E1B4B" if theme == "light" else "#F3F0FF"
    cur_attr = ' aria-current="page"'
    links = "\n".join(
        f'          <a href="{h}"{cur_attr if k == current else ""}>{l}</a>' for k, l, h in NAV)
    login_cur = ' aria-current="page"' if current == "login" else ""
    return f'''<header class="site-header is-{theme}">
    <div class="wrap">
      {logo(ink)}
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-menu" aria-label="Menu">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
      <div class="mobile-panel" id="site-menu">
        <nav class="nav" aria-label="Main">
{links}
        </nav>
        <div class="header-actions">
          <a class="nav-login" href="login.html"{login_cur}>Log in</a>
          <a class="btn btn-gold header-cta" href="begin.html">Begin the adventure</a>
        </div>
      </div>
    </div>
  </header>'''


FOOTER = f'''<footer class="site-footer">
    <div class="wrap">
      <div class="stack" style="gap:10px; max-width: 340px;">
        {logo("#FFFFFF")}
        <p>Picture books where the people you love are the heroes.</p>
        <p style="font-size:13px;">© <span data-year>2026</span> [COMPANY NAME] · ABN [ABN]</p>
      </div>
      <div class="footer-cols">
        <div><h2>Explore</h2><ul>
          <li><a href="how-it-works.html">How the magic works</a></li>
          <li><a href="art-styles.html">Art styles</a></li>
          <li><a href="worlds.html">Worlds</a></li>
        </ul></div>
        <div><h2>Help</h2><ul>
          <li><a href="pricing.html">Pricing</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="mailto:[SUPPORT EMAIL]">Contact</a></li>
        </ul></div>
        <div><h2>Legal</h2><ul>
          <li><a href="#privacy">Privacy</a></li>
          <li><a href="#terms">Terms</a></li>
          <li><a href="#shipping">Shipping</a></li>
        </ul></div>
      </div>
    </div>
  </footer>'''


def page(filename, title, desc, current, body, theme="dark", header_inside=False):
    head_title = f"{title} | {SITE}" if current != "home" else f"{SITE} — {title}"
    hdr = "" if header_inside else header(current, theme)
    html = f'''<!doctype html>
<html lang="en-AU">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{head_title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#14163A">
  <meta property="og:title" content="{head_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="assets/img/hero.jpg">
  <meta property="og:type" content="website">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  {FONTS}
  <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  {hdr}
  <main id="main">
{body}
  </main>
  {FOOTER}
  <script src="assets/js/main.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)


# ----------------------------------------------------------------------------- data
STEPS = [
    ("one", "#FFD9C7", "Gather your crew", "Upload a photo of your child, then invite siblings, best friends, parents and grandparents to join the story.",
     '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>'),
    ("two", "#CFEFE8", "Work the magic", "Our AI transforms each photo into a storybook character who still looks just like them.",
     '<path d="m15 4-11 11 5 5 11-11z"/><path d="M18 2v2M22 6h-2M20 2l-1 1"/>'),
    ("three", "#FFE39A", "Pick an enchantment", "See your whole crew in seven art styles, from glowing painted magic to soft watercolour.",
     '<path d="M12 3a9 9 0 1 0 9 9c0-1.7-1.3-2-2.5-2H16a2 2 0 0 1-2-2V6.5C14 4.3 13.7 3 12 3z"/><path d="M7.5 11.5h.01M10 7.5h.01M15.5 13.5h.01"/>'),
    ("four", "#E2DDF6", "Choose the quest", "Send the whole crew into a world, give everyone a role, check every page, then order it printed.",
     '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>'),
]

WORLDS = [
    ("The Moon Borrowers", "world-moon-borrowers", "#2A2470", "#FFE39A", "1–3 heroes", "3–7", 3, 7, ["Bedtime", "Space"],
     "The moon vanishes the night before a big birthday. Only one crew can bring it home.", '<path d="M20 14A8 8 0 1 1 10 4a6 6 0 0 0 10 10z"/>'),
    ("Dragon Day at School", "world-dragon-day", "#B8431F", "#FFF4E6", "1–4 heroes", "4–8", 4, 8, ["Funny", "School"],
     "Show-and-tell goes sideways when a very small dragon hatches in the classroom.", '<path d="M12 3c3 3 6 5 6 10a6 6 0 0 1-12 0c0-2 1-3 2-4 0 2 1 3 2 3 0-4 2-6 2-9z"/>'),
    ("Under the Kelp Forest", "world-kelp-forest", "#0F4C5C", "#DFF7F2", "1–3 heroes", "3–7", 3, 7, ["Ocean", "Kindness"],
     "A snorkel trip becomes a daring rescue for a lost baby sea turtle.", '<path d="M2 7c2-2 4-2 6 0s4 2 6 0 4-2 6 0M2 12c2-2 4-2 6 0s4 2 6 0 4-2 6 0M2 17c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/>'),
    ("The Great Backyard Expedition", "world-backyard-expedition", "#F4C95D", "#1E1B4B", "2–5 heroes", "4–9", 4, 9, ["Siblings", "Nature"],
     "Map, torch, snacks. The backyard turns out to be much bigger after dark.", '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/>'),
    ("Captain of the Cloud Ship", "world-cloud-ship", "#6E9BD8", "#14163A", "1–4 heroes", "5–10", 5, 10, ["Family", "Adventure"],
     "Your little one takes the helm of a flying ship, with family as the crew.", '<path d="M2 16h20l-3 5H5z"/><path d="M12 16V3l7 10h-7M12 5 6 13h6"/>'),
    ("The Birthday That Wouldn’t End", "world-endless-birthday", "#6A3E8C", "#FCE7FF", "1–6 heroes", "3–8", 3, 8, ["Birthday", "Friends"],
     "A wish goes wrong and the party repeats forever — until friends crack the clue.", '<path d="M5 21V11h14v10zM3 21h18M12 11V7"/><path d="M12 7c-1-1-1-3 0-4 1 1 1 3 0 4z"/>'),
]

PLANS = [
    ("Take a peek", "Digital book", "price-digital", False, "btn-navy", "Start free preview",
     ["Free character preview in all styles", "Full illustrated PDF, ready instantly", "Up to [MAX] heroes"]),
    ("Most loved", "Hardcover", "price-hardcover", True, "btn-gold", "Create my hardcover",
     ["Everything in Digital", "Premium printed hardcover", "Personalised dedication page", "At your door in [X] days"]),
    ("For gifting", "Treasure chest", "price-treasure-chest", False, "btn-navy", "Build a gift set",
     ["Everything in Hardcover", "Keepsake gift box", "Character poster print", "Gift message and chosen delivery date"]),
]

FAQS = [
    ("photos", "What happens to the photos I upload?", "[YOUR POLICY] — for example: photos are used only to create your characters, stored securely, and deleted after [X] days. They are never used to train AI models or shared with anyone."),
    ("photos", "What kind of photo works best?", "A recent, well-lit, front-facing photo with the whole face visible. Avoid sunglasses, hats and group shots — upload one photo per person."),
    ("photos", "Is it safe to upload photos of my children?", "[SECURITY DETAILS] — for example: uploads are encrypted, only you can see your characters, and you can delete everything from your account at any time."),
    ("creating", "How many people can join one adventure?", "Each world lists how many heroes it holds. Most take between one and [MAX] — siblings, friends, parents and grandparents are all welcome."),
    ("creating", "Can I change a character if it doesn’t look right?", "Yes. Regenerate the character or tweak details like hair, glasses and outfit before you pick a world."),
    ("creating", "Can I see the whole book before ordering?", "Yes. Flip through every page with your crew in place, and swap styles or characters before you pay."),
    ("orders", "How long does delivery take?", "Digital books are ready straight away. Printed books ship within [X] business days; delivery time depends on your location."),
    ("orders", "Do you ship outside Australia?", "[SHIPPING REGIONS]"),
    ("orders", "What if my book arrives damaged?", "[GUARANTEE] — for example: send us a photo and we’ll reprint it free."),
]

STYLE_GUIDE = [
    ("Enchanted glow", "3–10", "Choose it for maximum magic and a book that feels like a gift."),
    ("Watercolour dream", "0–5", "Choose it for babies, toddlers and wind-down bedtime reads."),
    ("Classic fable", "3–8", "Choose it for keepsakes and books meant to be passed down."),
    ("3D animated", "4–10", "Choose it for screen-loving kids who want big action."),
    ("Paper-cut", "2–8", "Choose it for crafty families and a tactile, textured look."),
    ("Clay stop-motion", "2–8", "Choose it for giggles, charm and something a bit different."),
    ("Crayon sketchbook", "2–7", "Choose it for little artists who love to draw."),
]


# ----------------------------------------------------------------------------- partials
def pic(name, alt, cls="", extra="", w=1672, h=941, lazy=True):
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return (f'<picture><source srcset="assets/img/{name}.webp" type="image/webp">'
            f'<img class="{cls}" src="assets/img/{name}.jpg" alt="{alt}" width="{w}" height="{h}"{load}{extra}></picture>')


def steps_html():
    items = ""
    for i, (n, bg, t, b, icon) in enumerate(STEPS):
        items += f'''
          <li class="step reveal reveal-d{i}">
            <div class="step-badge" style="background:{bg}"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#1E1B4B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{icon}</svg></div>
            <span class="step-num">Step {n}</span>
            <h3>{t}</h3>
            <p>{b}</p>
          </li>'''
    return f'''<div class="map">
        <svg class="map-trail" viewBox="0 0 1280 120" preserveAspectRatio="none" fill="none" aria-hidden="true">
          <path class="trail" d="M120 60 C260 -10 380 130 480 60 S700 -10 800 60 S1040 130 1160 60" stroke="#F4C95D" stroke-opacity=".7" stroke-width="3" stroke-linecap="round"/>
          <path d="M1150 48l14 12-14 12" stroke="#F4C95D" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <ol class="steps">{items}
        </ol>
      </div>'''


def style_viewer(heading_level="h3", with_meta=False):
    meta = '''
            <div class="style-meta">
              <span><strong>Best for ages:</strong> <span class="muted" data-style-ages>3–10</span></span>
              <span><strong>Feels like:</strong> <span class="muted" data-style-mood>A premium modern picture book</span></span>
            </div>''' if with_meta else '''
            <p class="muted" style="font-weight:800;">Best for ages <span data-style-ages>3–10</span></p>'''
    return f'''<div data-style-viewer>
        <div class="style-viewer">
          <div class="style-stage" id="style-stage-{heading_level}" aria-live="polite">
            {pic("style-enchanted-glow", "A young wizard on a hilltop above a river valley and castle, painted in the Enchanted glow style", w=1448, h=1086)}
            <div class="style-soon"><strong style="color:#fff;" data-soon-file>[IMAGE]</strong><span>Coming soon</span></div>
          </div>
          <div class="style-info">
            <span class="kicker" style="color:var(--text-mute)">Now showing</span>
            <{heading_level} class="h3" data-style-name>Enchanted glow</{heading_level}>
            <p class="muted" data-style-desc>Our signature look. Rich painted light, golden sparkles and starry skies — pure bedtime wonder.</p>{meta}
            <a class="btn btn-gold" href="begin.html" style="align-self:flex-start;">See my child in this style</a>
          </div>
        </div>
        <div class="style-tabs" role="group" aria-label="Choose an art style"></div>
      </div>'''


def world_card(w, idx, link_text="Enter this world"):
    title, file, cover, ink, cast, ages, mn, mx, tags, blurb, motif = w
    tag_html = "".join(f"<li>{t}</li>" for t in tags)
    return f'''
        <article class="world reveal reveal-d{idx % 3}" data-min="{mn}" data-max="{mx}">
          <div class="world-cover" style="--cover:{cover}; --cover-ink:{ink};">
            <!-- Add a cover: <img src="assets/img/{file}.jpg" alt=""> + <span class="scrim"></span> and class="world-cover has-img" -->
            <svg class="motif" viewBox="0 0 24 24" fill="none" stroke="{ink}" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{motif}</svg>
            <span class="pill">{cast}</span>
            <h3>{title}</h3>
          </div>
          <div class="world-body">
            <p>{blurb}</p>
            <ul class="tags" aria-label="Themes">{tag_html}</ul>
            <div class="world-foot"><span>Ages {ages} · [PAGES] pages</span><a href="begin.html">{link_text}<span class="sr-only">: {title}</span></a></div>
          </div>
        </article>'''


def plans_html():
    out = ""
    for tag, name, file, featured, btn, cta, items in PLANS:
        feats = "".join(f"<li>{STAR_LI}<span>{i}</span></li>" for i in items)
        out += f'''
        <article class="plan{' is-featured' if featured else ''}">
          <div class="plan-img"><!-- Replace with: <img src="assets/img/{file}.jpg" alt="" loading="lazy"> -->[IMAGE: {file}.jpg]</div>
          <div class="plan-body">
            <span class="plan-tag">{tag}</span>
            <h3>{name}</h3>
            <p class="price">[YOUR PRICE]</p>
            <ul class="feature-list">{feats}</ul>
            <a class="btn {btn} btn-block" href="begin.html">{cta}</a>
          </div>
        </article>'''
    return f'<div class="plans">{out}\n      </div>'


def faq_items(items, with_cat=False):
    out = ""
    for i, (cat, q, a) in enumerate(items):
        cat_attr = f' data-cat="{cat}"' if with_cat else ""
        out += f'''
          <div class="faq-item{' is-open' if i == 0 else ''}"{cat_attr}>
            <button class="faq-q" type="button" aria-expanded="{'true' if i == 0 else 'false'}" aria-controls="faq-a-{i}" id="faq-q-{i}"><span>{q}</span>{PLUS}</button>
            <div class="faq-a" id="faq-a-{i}" role="region" aria-labelledby="faq-q-{i}"><div><p>{a}</p></div></div>
          </div>'''
    return out


def crew_card(tilt=True):
    return f'''<div class="crew-card"{'' if tilt else ' style="transform:none"'}>
          <header><strong>The crew</strong><span>3 of [MAX] aboard</span></header>
          <div class="crew-row"><span class="crew-avatar c-peach">M</span><div><strong>Mia</strong><small>Age 8 · Photo uploaded</small></div><span class="crew-tag c-peach">Hero</span></div>
          <div class="crew-row"><span class="crew-avatar c-mint">L</span><div><strong>Leo</strong><small>Age 5 · Brother</small></div><span class="crew-tag c-mint">Sidekick</span></div>
          <div class="crew-row"><span class="crew-avatar c-lilac">N</span><div><strong>Nan</strong><small>Grandma</small></div><span class="crew-tag c-lilac">Wise wizard</span></div>
          <a class="crew-add" href="begin.html" style="text-align:center; text-decoration:none;">+ Recruit another adventurer</a>
        </div>'''


# ----------------------------------------------------------------------------- pages
def build_home():
    worlds = "".join(world_card(w, i) for i, w in enumerate(WORLDS))
    body = f'''
    <section class="hero" aria-labelledby="hero-title">
      <div class="hero-art" data-sparkles>
        {pic("hero", "A smiling boy steps out of a photo and becomes an illustrated young wizard, walking into a glowing storybook with his family, a flying ship, a dragon and a castle", lazy=False)}
        <div class="hero-glow" aria-hidden="true"></div>
        <canvas class="sparkle-canvas" aria-hidden="true"></canvas>
      </div>
      {header("home", "light")}
      <div class="hero-body">
        <div class="wrap">
          <div class="hero-copy intro">
            <span class="kicker">Once upon a time, starring…</span>
            <h1 id="hero-title">Your child, <em>the hero</em> of their very own tale.</h1>
            <p class="lede">Upload a photo and watch them become a storybook character. Gather siblings, friends and grandparents — then send the whole crew off on an adventure.</p>
            <div class="hero-actions">
              <a class="btn btn-gold" href="begin.html">{WAND} Cast the first spell</a>
              <a class="btn btn-ghost-ink" href="worlds.html">Explore worlds</a>
            </div>
            <ul class="checks">
              <li>{SPARK_TEAL} Free character preview · Up to [MAX] heroes per book</li>
              <li>{SPARK_TEAL} Printed and at your door in [X] days</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section on-deep" aria-labelledby="how-title">
      <div class="wrap">
        <div class="stack center reveal">
          <span class="kicker">Chapter one</span>
          <h2 class="h2" id="how-title">How the magic works</h2>
        </div>
        {steps_html()}
        <p class="center" style="margin-top:48px; text-align:center;"><a href="how-it-works.html" style="font-weight:800;">See the full journey</a></p>
      </div>
    </section>

    <section class="section on-indigo" aria-labelledby="styles-title">
      <div class="wrap">
        <div class="stack reveal" style="max-width:760px;">
          <span class="kicker">Chapter two</span>
          <h2 class="h2" id="styles-title">Try on a different kind of magic</h2>
          <p class="lede">One photo, seven enchantments. Pick a style and watch the same adventure transform before your eyes.</p>
        </div>
        {style_viewer("h3")}
      </div>
    </section>

    <section class="section on-teal" aria-labelledby="crew-title" style="overflow:hidden;">
      <svg class="compass-bg" viewBox="0 0 24 24" fill="none" stroke="#5FC8B4" stroke-width=".4" aria-hidden="true"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="7"/><path d="M12 1v22M1 12h22M16 8l-2.5 5.5L8 16l2.5-5.5z"/></svg>
      <div class="wrap split">
        <div class="stack reveal">
          <span class="kicker" style="color:#9FE3D6">Chapter three</span>
          <h2 class="h2" id="crew-title">Every great quest needs a crew.</h2>
          <p class="lede" style="color:#CDE6E2">Siblings, best mates, Nan and even the dog. Choose one hero, then hand out the parts — trusty sidekick, ship’s navigator, dragon-whisperer — and watch them turn up on every page that matters.</p>
          <a class="btn btn-gold" href="begin.html" style="align-self:flex-start">Assemble my crew</a>
        </div>
        <div class="reveal reveal-d2">{crew_card()}</div>
      </div>
    </section>

    <section class="section" aria-labelledby="worlds-title">
      <div class="wrap">
        <div class="reveal" style="display:flex; justify-content:space-between; align-items:flex-end; gap:24px; flex-wrap:wrap; margin-bottom:48px;">
          <div class="stack"><span class="kicker">Chapter four</span><h2 class="h2" id="worlds-title">Choose a world to explore</h2></div>
          <a href="worlds.html" style="font-weight:800;">See every world</a>
        </div>
        <div class="grid-3">{worlds}
        </div>
      </div>
    </section>

    <section class="section on-cream" aria-labelledby="pricing-title">
      <div class="wrap">
        <div class="stack center reveal" style="margin-bottom:56px;">
          <span class="kicker">Chapter five</span>
          <h2 class="h2" id="pricing-title">Peek for free. Pay when you’re spellbound.</h2>
        </div>
        {plans_html()}
      </div>
    </section>

    <section class="section on-cream" aria-labelledby="faq-title" style="padding-top:0;">
      <div class="wrap faq-layout wide-left">
        <div class="stack"><span class="kicker">Before you set sail</span><h2 class="h2" id="faq-title">Questions from fellow adventurers</h2><a href="faq.html" style="font-weight:800;">All questions</a></div>
        <div class="faq-list">{faq_items([FAQS[0], FAQS[1], FAQS[3], FAQS[5], FAQS[6]])}
        </div>
      </div>
    </section>

    <section class="section final-cta" aria-labelledby="cta-title">
      <div class="starfield" data-stars="60" aria-hidden="true"></div>
      <div class="wrap inner">
        {MOON.format(s=64, c="#F4C95D")}
        <h2 id="cta-title">Tonight’s bedtime story could star <em>them.</em></h2>
        <p class="lede">Upload one photo. The first glimpse of magic is on us.</p>
        <a class="btn btn-gold btn-lg" href="begin.html">Turn the first page</a>
      </div>
    </section>'''
    page("index.html", "Personalised picture books starring your child",
         "Turn your child, siblings, friends and family into storybook characters with AI, then send them on a printed picture-book adventure.",
         "home", body, header_inside=True)


def build_how():
    body = f'''
    <section class="page-intro center" aria-labelledby="t">
      <div class="starfield" data-stars="50" aria-hidden="true"></div>
      <div class="wrap"><div class="stack center intro">
        <span class="kicker">Four steps to a storybook</span>
        <h1 class="h1" id="t">How the magic works</h1>
        <p class="lede" style="max-width:52ch">From a photo on your phone to a book on their pillow. You stay in control at every step, and nothing is printed until you love every page.</p>
      </div></div>
    </section>

    <section class="section" style="padding-top:32px;">
      <div class="wrap how-rows">
        <div class="how-row split">
          <div class="copy reveal">
            <span class="kicker">Step one</span>
            <h2 class="h2">Gather your crew</h2>
            <p>Upload one clear photo of your child — they’re the hero. Then add anyone who belongs in the story: brothers and sisters, best friends, cousins, parents and grandparents.</p>
            <p>Give each person a name and a role, like trusty sidekick or wise wizard. Most worlds hold up to [MAX] characters.</p>
          </div>
          <div class="reveal reveal-d2">{crew_card(tilt=False)}</div>
        </div>
        <div class="how-row split reverse">
          <div class="copy reveal">
            <span class="kicker">Step two</span>
            <h2 class="h2">Work the magic</h2>
            <p>Our AI turns each photo into an illustrated character that still looks unmistakably like them — same smile, same hair, same sparkle.</p>
            <p>Not quite right? Regenerate or tweak details like hair, glasses or outfit before you move on.</p>
          </div>
          <div class="media-frame reveal reveal-d2">{pic("hero", "A boy’s photo transforming into an illustrated wizard character", extra=' style="object-position:45% 50%"')}</div>
        </div>
        <div class="how-row split">
          <div class="copy reveal">
            <span class="kicker">Step three</span>
            <h2 class="h2">Pick an enchantment</h2>
            <p>Preview your whole crew in seven art styles — from glowing painted magic to soft watercolour and heirloom ink. Switch as often as you like.</p>
            <a href="art-styles.html" style="font-weight:800; align-self:flex-start;">See all art styles</a>
          </div>
          <div class="fan reveal reveal-d2">
            <img src="assets/img/style-classic-fable.jpg" alt="Classic fable style example" loading="lazy" width="1448" height="1086">
            <img src="assets/img/style-watercolour.jpg" alt="Watercolour style example" loading="lazy" width="1448" height="1086">
            <img src="assets/img/style-enchanted-glow.jpg" alt="Enchanted glow style example" loading="lazy" width="1448" height="1086">
          </div>
        </div>
        <div class="how-row split reverse">
          <div class="copy reveal">
            <span class="kicker">Step four</span>
            <h2 class="h2">Choose the quest</h2>
            <p>Send the whole crew into a world — lost moons, cloud ships, kelp forests. Flip through every page with your characters in place, add a dedication, then order.</p>
            <p>Digital books arrive instantly. Printed hardcovers are at your door in [X] days.</p>
          </div>
          <div class="mini-covers reveal reveal-d2">
            <a class="mini-cover" href="worlds.html" style="background:#2A2470; color:#FFE39A; text-decoration:none;">The Moon Borrowers</a>
            <a class="mini-cover" href="worlds.html" style="background:#B8431F; color:#FFF4E6; text-decoration:none;">Dragon Day at School</a>
            <a class="mini-cover" href="worlds.html" style="background:#0F4C5C; color:#DFF7F2; text-decoration:none;">Under the Kelp Forest</a>
            <a class="mini-cover" href="worlds.html" style="background:#6E9BD8; color:#14163A; text-decoration:none;">Captain of the Cloud Ship</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section on-cream" aria-labelledby="tips">
      <div class="wrap">
        <div class="stack" style="margin-bottom:36px;"><span class="kicker">A little wizard’s advice</span><h2 class="h2" id="tips">Photos that make the best characters</h2></div>
        <div class="tips">
          <div class="tip-card tip-do"><h3>Do</h3><ul>
            <li>Face the camera with a natural smile</li><li>Use bright, even light — near a window is perfect</li>
            <li>Show the whole face and hairline</li><li>Use a recent photo, one per person</li></ul></div>
          <div class="tip-card tip-avoid"><h3>Avoid</h3><ul>
            <li>Sunglasses, hats or face paint</li><li>Blurry, dark or heavily filtered shots</li>
            <li>Group photos — upload each person separately</li><li>Faces turned sideways or partly covered</li></ul></div>
        </div>
      </div>
    </section>

    <section class="section final-cta">
      <div class="starfield" data-stars="40" aria-hidden="true"></div>
      <div class="wrap inner">
        <h2 style="font-size:clamp(36px,4.2vw,56px)">Ready to meet their character?</h2>
        <p class="lede">Join the shortlist and be first through the door.</p>
        <a class="btn btn-gold btn-lg" href="begin.html">Begin the adventure</a>
      </div>
    </section>'''
    page("how-it-works.html", "How the magic works", "Upload photos, turn your crew into storybook characters, pick an art style and choose a world — here’s how StoryMe works.", "how", body)


def build_styles():
    guide = "".join(f'<div class="guide-card reveal reveal-d{i % 3}"><h3>{n}</h3><span class="ages">Ages {a}</span><p>{p}</p></div>' for i, (n, a, p) in enumerate(STYLE_GUIDE))
    body = f'''
    <section class="page-intro" aria-labelledby="t">
      <div class="starfield" data-stars="40" aria-hidden="true"></div>
      <div class="wrap"><div class="stack intro">
        <span class="kicker">Seven enchantments</span>
        <h1 class="h1" id="t">Art styles</h1>
        <p class="lede" style="max-width:52ch">The same hero, the same adventure — seven completely different looks. Tap a style to see how it changes the story.</p>
      </div></div>
    </section>
    <section class="section" style="padding-top:0;">
      <div class="wrap">{style_viewer("h2", with_meta=True)}</div>
    </section>
    <section class="section on-cream" aria-labelledby="g">
      <div class="wrap">
        <div class="stack" style="margin-bottom:40px;"><span class="kicker">Not sure which to pick?</span><h2 class="h2" id="g">Find the right style for your reader</h2></div>
        <div class="guide-grid">{guide}
          <div class="guide-card is-dark"><h3>Still torn?</h3><p>Preview your crew in every style for free before you choose.</p><a href="begin.html">Join the shortlist</a></div>
        </div>
      </div>
    </section>'''
    page("art-styles.html", "Art styles", "Preview your child as a character in seven art styles — enchanted glow, watercolour, classic fable, 3D animated, paper-cut, clay and crayon.", "styles", body)


def build_worlds():
    cards = "".join(world_card(w, i) for i, w in enumerate(WORLDS))
    body = f'''
    <section class="page-intro" aria-labelledby="t">
      <div class="starfield" data-stars="40" aria-hidden="true"></div>
      <div class="wrap"><div class="stack intro">
        <span class="kicker">Where to next?</span>
        <h1 class="h1" id="t">Choose a world to explore</h1>
        <p class="lede" style="max-width:56ch">Every world is written so your crew are the heroes — not background extras. Pick one that matches their age and their wildest daydreams.</p>
      </div></div>
    </section>
    <section class="section" style="padding-top:0;">
      <div class="wrap">
        <div class="chips" data-world-filter role="group" aria-label="Filter worlds by age" style="margin-bottom:32px;">
          <span style="font-weight:800; color:var(--text-mute); margin-right:6px;">Ages</span>
          <button class="chip" type="button" aria-pressed="true" data-age="all">All</button>
          <button class="chip" type="button" aria-pressed="false" data-age="3">Under 4</button>
          <button class="chip" type="button" aria-pressed="false" data-age="5">4–6</button>
          <button class="chip" type="button" aria-pressed="false" data-age="8">7 and up</button>
          <span style="margin-left:auto; color:var(--text-mute);" data-world-count aria-live="polite">6 worlds</span>
        </div>
        <div class="grid-3">{cards}
        </div>
      </div>
    </section>
    <section class="section" style="padding-top:0;">
      <div class="wrap">
        <div class="banner reveal">
          <div class="stack" style="gap:10px; max-width:760px;">
            <span class="kicker">New worlds are being written</span>
            <h2 class="h2" style="font-size:clamp(30px,3.2vw,44px)">Got a world your kids would love?</h2>
            <p>Dinosaurs, space stations, footy grand finals — tell us what they’re obsessed with and we’ll add it to the list.</p>
          </div>
          <a class="btn btn-navy" href="begin.html">Suggest a world</a>
        </div>
      </div>
    </section>'''
    page("worlds.html", "Worlds", "Pick a story world for your crew — lost moons, classroom dragons, kelp forests, cloud ships and more.", "worlds", body)


def build_pricing():
    rows = [("Free preview in every art style", "Yes", "Yes", "Yes"), ("Characters per book", "Up to [MAX]", "Up to [MAX]", "Up to [MAX]"),
            ("Illustrated PDF", "Yes", "Yes", "Yes"), ("Printed hardcover", "—", "Yes", "Yes"), ("Dedication page", "—", "Yes", "Yes"),
            ("Keepsake gift box", "—", "—", "Yes"), ("Character poster print", "—", "—", "Yes"), ("Delivery", "Instant", "[X] days", "[X] days")]
    trs = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in rows)
    body = f'''
    <section class="page-intro center" aria-labelledby="t">
      <div class="starfield" data-stars="40" aria-hidden="true"></div>
      <div class="wrap"><div class="stack center intro">
        <span class="kicker">Peek for free</span>
        <h1 class="h1" id="t">Pay when you’re spellbound</h1>
        <p class="lede" style="max-width:50ch">Create your crew and preview every page for free. Only choose a format when you’re sure it’s perfect.</p>
      </div></div>
    </section>
    <section class="section" style="padding-top:24px;">
      <div class="wrap">{plans_html()}</div>
    </section>
    <section class="section on-cream" aria-labelledby="c">
      <div class="wrap">
        <h2 class="h2" id="c" style="margin-bottom:36px;">Compare formats</h2>
        <div class="table-scroll">
          <table class="compare">
            <caption class="sr-only">What each format includes</caption>
            <thead><tr><th scope="col">What’s included</th><th scope="col">Digital</th><th scope="col" class="hl">Hardcover</th><th scope="col">Treasure chest</th></tr></thead>
            <tbody>{trs}</tbody>
          </table>
        </div>
        <div class="info-grid" style="margin-top:32px;">
          <div class="info-card"><h3>Extra copies</h3><p>One for Nan’s house? Add more hardcovers at [PRICE] each.</p></div>
          <div class="info-card"><h3>Shipping</h3><p>[SHIPPING POLICY] — for example: flat-rate Australia-wide, free over [AMOUNT].</p></div>
          <div class="info-card"><h3>Happiness promise</h3><p>[GUARANTEE] — for example: printing fault? We’ll reprint it free.</p></div>
        </div>
      </div>
    </section>'''
    page("pricing.html", "Pricing", "Preview your personalised picture book free, then choose a digital book, hardcover or keepsake gift set.", "pricing", body)


def build_faq():
    body = f'''
    <section class="page-intro" aria-labelledby="t">
      <div class="starfield" data-stars="40" aria-hidden="true"></div>
      <div class="wrap"><div class="stack intro">
        <span class="kicker">Before you set sail</span>
        <h1 class="h1" id="t">Questions from fellow adventurers</h1>
      </div></div>
    </section>
    <section class="section" style="padding-top:0;">
      <div class="wrap faq-layout">
        <div class="faq-cats" data-faq-cats role="group" aria-label="Question topics">
          <button class="faq-cat" type="button" aria-pressed="true" data-cat="all">All questions</button>
          <button class="faq-cat" type="button" aria-pressed="false" data-cat="photos">Photos &amp; privacy</button>
          <button class="faq-cat" type="button" aria-pressed="false" data-cat="creating">Creating your book</button>
          <button class="faq-cat" type="button" aria-pressed="false" data-cat="orders">Orders &amp; delivery</button>
        </div>
        <div class="faq-list">{faq_items(FAQS, with_cat=True)}
        </div>
      </div>
    </section>
    <section class="section" style="padding-top:0;">
      <div class="wrap">
        <div class="banner">
          <div class="stack" style="gap:8px;"><h2 class="h3">Still wondering?</h2><p>Email us at [SUPPORT EMAIL]. We reply within [X] hours.</p></div>
          <a class="btn btn-navy" href="mailto:[SUPPORT EMAIL]">Email us</a>
        </div>
      </div>
    </section>'''
    page("faq.html", "FAQ", "Answers about photo privacy, creating characters, art styles, delivery and more.", "faq", body)


def build_login():
    body = f'''
    <section class="section" style="padding-top:24px;">
      <div class="wrap">
        <div class="login">
          <div class="login-art">
            {pic("style-enchanted-glow", "A young wizard casting golden sparkles over a magical valley", w=1448, h=1086, lazy=False)}
            <div class="login-note"><span class="kicker">Welcome back, adventurer.</span><p style="color:#E9E6FF">Your crew and saved stories are waiting.</p></div>
          </div>
          <form class="login-form" data-login novalidate>
            <h1 class="h2">Log in</h1>
            <button class="btn btn-white btn-block" type="button" data-google style="border:1.5px solid var(--ink);">
              <svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M22.5 12.3c0-.8-.1-1.5-.2-2.2H12v4.2h5.9a5 5 0 0 1-2.2 3.3v2.7h3.5c2.1-1.9 3.3-4.7 3.3-8z"/><path fill="#34A853" d="M12 23c3 0 5.5-1 7.2-2.7l-3.5-2.7c-1 .7-2.2 1.1-3.7 1.1-2.9 0-5.3-1.9-6.2-4.6H2.2v2.8A11 11 0 0 0 12 23z"/><path fill="#FBBC05" d="M5.8 14.1a6.6 6.6 0 0 1 0-4.2V7.1H2.2a11 11 0 0 0 0 9.8z"/><path fill="#EA4335" d="M12 5.4c1.6 0 3.1.6 4.2 1.7l3.1-3.1A11 11 0 0 0 2.2 7.1l3.6 2.8C6.7 7.3 9.1 5.4 12 5.4z"/></svg>
              Continue with Google
            </button>
            <div class="divider">or</div>
            <div class="field"><label for="li-email">Email</label><input id="li-email" name="email" type="email" autocomplete="email" placeholder="you@example.com"></div>
            <div class="field">
              <div style="display:flex; justify-content:space-between; gap:12px;"><label for="li-pass">Password</label><a href="#forgot" style="font-size:15px; font-weight:700; color:var(--ember-ink);">Forgot password?</a></div>
              <input id="li-pass" name="password" type="password" autocomplete="current-password" placeholder="••••••••">
            </div>
            <button class="btn btn-navy btn-block" type="submit">Log in</button>
            <p class="form-status" role="status" aria-live="polite"></p>
            <p style="text-align:center; color:var(--ink-soft);">New to StoryMe? <a href="begin.html" style="font-weight:800; color:var(--ember-ink);">Join the shortlist</a></p>
          </form>
        </div>
      </div>
    </section>'''
    page("login.html", "Log in", "Log in to StoryMe to see your crew and saved stories.", "login", body)


def build_begin():
    ages = "".join(f'<button class="chip chip-solid" type="button" aria-pressed="{"true" if a == "4–7" else "false"}" data-value="{a}">{a}</button>' for a in ["0–3", "4–7", "8–10", "10+"])
    styles = "".join(f'<button class="chip" type="button" aria-pressed="{"true" if i == 0 else "false"}" data-value="{n}">{n}</button>' for i, (n, _, _) in enumerate(STYLE_GUIDE))
    perks = [("First in line", "Early access before public launch."),
             ("Founding family pricing", "[LAUNCH OFFER] on your first book."),
             ("Shape the stories", "Vote on the next worlds and art styles we create.")]
    perk_html = "".join(f'<li><span class="perk-icon">{SPARK}</span><div><strong>{t}</strong><span>{b}</span></div></li>' for t, b in perks)
    body = f'''
    <section class="section" style="overflow:hidden; padding-top:clamp(48px,7vw,88px);">
      <div class="starfield" data-stars="50" aria-hidden="true"></div>
      <img class="bg-hero-faint" src="assets/img/hero.jpg" alt="" width="1672" height="941">
      <div class="wrap shortlist">
        <div class="stack intro" style="gap:22px; padding-top:12px;">
          <span class="kicker">The first chapter opens soon</span>
          <h1 class="h1">Join the shortlist</h1>
          <p class="lede">StoryMe is almost ready. Add your name and you’ll be among the first families to turn their kids into storybook heroes.</p>
          <ul class="perks">{perk_html}</ul>
        </div>

        <div class="form-card">
          <!--
            FORM SETUP — choose one:
            • Netlify: keep data-netlify="true" and set data-endpoint="netlify".
            • Formspree / Basin / your API: set data-endpoint="https://formspree.io/f/XXXX".
            • Leave data-endpoint empty for demo mode (shows success, sends nothing).
          -->
          <form name="shortlist" method="POST" data-netlify="true" netlify-honeypot="bot-field" data-shortlist data-endpoint="" novalidate class="stack" style="gap:20px;">
            <input type="hidden" name="form-name" value="shortlist">
            <p hidden><label>Leave this empty <input name="bot-field"></label></p>
            <h2 class="h3" style="font-size:32px;">Save your spot</h2>
            <div class="form-grid">
              <div class="field"><label for="sl-name">Your first name</label><input id="sl-name" name="parent_name" type="text" autocomplete="given-name" placeholder="Sam" aria-describedby="sl-name-error" required><span class="field-error" id="sl-name-error"></span></div>
              <div class="field"><label for="sl-hero">Your hero’s name <span style="font-weight:600; color:#6B6585;">(optional)</span></label><input id="sl-hero" name="hero_name" type="text" placeholder="Mia"></div>
            </div>
            <div class="field"><label for="sl-email">Email</label><input id="sl-email" name="email" type="email" autocomplete="email" placeholder="you@example.com" aria-describedby="sl-email-error" required><span class="field-error" id="sl-email-error"></span></div>
            <div class="field">
              <span class="field-label" id="age-label">Hero’s age</span>
              <div class="chips" data-chip-group="single" role="group" aria-labelledby="age-label">{ages}<input type="hidden" name="hero_age" value="4–7"></div>
            </div>
            <div class="field">
              <span class="field-label" id="style-label">Styles you love <span style="font-weight:600; color:#6B6585;">(pick any)</span></span>
              <div class="chips" data-chip-group="multi" role="group" aria-labelledby="style-label" style="gap:8px;">{styles}<input type="hidden" name="styles" value="Enchanted glow"></div>
            </div>
            <label class="consent"><input type="checkbox" name="updates" value="yes"> <span>Send me launch updates. Unsubscribe anytime. See our <a href="#privacy">privacy policy</a>.</span></label>
            <button class="btn btn-navy btn-lg btn-block" type="submit"><span style="color:var(--gold); display:inline-flex;">{WAND}</span> Add me to the shortlist</button>
            <p class="form-status" role="alert"></p>
          </form>

          <div class="success" data-shortlist-success hidden>
            {MOON.format(s=84, c="#E0AE2C")}
            <span class="kicker" style="color:var(--ember-ink)">The spell is cast!</span>
            <h2 class="h3" tabindex="-1" style="font-size:40px;">You’re on the shortlist</h2>
            <p style="color:var(--ink-soft); max-width:40ch;">We’ll email you the moment the first chapter opens. Want to jump the queue? Share your link with friends.</p>
            <div class="copy-row">
              <label class="sr-only" for="ref-link">Your referral link</label>
              <input id="ref-link" type="text" readonly value="[YOUR REFERRAL LINK]">
              <button class="btn btn-navy" type="button" data-copy="ref-link">Copy</button>
            </div>
            <button class="link-btn" type="button" data-shortlist-again>Add another hero</button>
            <a href="worlds.html" style="font-weight:800; color:var(--ink);">Explore the worlds while you wait</a>
          </div>
        </div>
      </div>
    </section>'''
    page("begin.html", "Join the shortlist", "Join the StoryMe shortlist for early access to personalised picture books starring your child.", "begin", body)


def build_404():
    body = '''
    <section class="section final-cta" style="min-height:60vh; display:flex; align-items:center;">
      <div class="starfield" data-stars="60" aria-hidden="true"></div>
      <div class="wrap inner">
        <span class="kicker">Lost in the woods?</span>
        <h1 class="h1" style="color:#fff">This page wandered off the map</h1>
        <p class="lede">The link may be old or mistyped.</p>
        <a class="btn btn-gold btn-lg" href="index.html">Back to the start</a>
      </div>
    </section>'''
    page("404.html", "Page not found", "This page could not be found.", "404", body)


FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#14163A"/><g fill="none" stroke="#F3F0FF" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 20c7-3 14-3 22 3v28c-8-6-15-6-22-3z"/><path d="M54 20c-7-3-14-3-22 3v28c8-6 15-6 22-3z"/></g><path d="M46 7l1.8 4.5 4.5 1.8-4.5 1.8L46 19.6l-1.8-4.5-4.5-1.8 4.5-1.8z" fill="#F4C95D"/></svg>'''

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "assets/img/favicon.svg"), "w") as f:
        f.write(FAVICON)
    for fn in (build_home, build_how, build_styles, build_worlds, build_pricing, build_faq, build_login, build_begin, build_404):
        fn()
    print("built")
