# StoryMe — static website

Plain HTML, CSS and JavaScript. No build step or framework needed to deploy.

## Pages
| File | Page |
|---|---|
| `index.html` | Home |
| `how-it-works.html` | How the magic works |
| `art-styles.html` | Art styles |
| `worlds.html` | Worlds |
| `pricing.html` | Pricing |
| `faq.html` | FAQ |
| `login.html` | Log in (placeholder until accounts exist) |
| `begin.html` | Begin the adventure — shortlist sign-up |
| `404.html` | Not found |

## Deploy (pick one)
- **Netlify:** drag this folder onto app.netlify.com/drop.
- **Vercel:** `npx vercel` inside this folder.
- **Cloudflare Pages / GitHub Pages:** upload the folder as-is, with no build command.

## Make the shortlist form collect sign-ups
Open `begin.html` and find `data-endpoint=""` on the form.
- **Netlify:** set `data-endpoint="netlify"`. Sign-ups appear under Site → Forms.
- **Formspree (any host):** create a form, then set `data-endpoint="https://formspree.io/f/XXXXXXX"`.
- **Left empty:** demo mode. The form shows the success message but sends nothing.

Fields sent: `parent_name`, `hero_name`, `email`, `hero_age`, `styles`, `updates`.

## Add more images
Save the files in `assets/img/`. Each has a `.jpg` and, optionally, a `.webp` version.
- **New art style:** in `assets/js/main.js`, find `STYLES` and set `img: 'assets/img/style-clay'` for that style (no extension).
- **World covers and pricing tier images:** each card has an HTML comment showing exactly where the `<img>` tag goes.

## Placeholders to replace
Search the files for `[` to find them all: `[YOUR PRICE]`, `[MAX]`, `[X]`, `[PAGES]`, `[YOUR POLICY]`, `[SUPPORT EMAIL]`, `[COMPANY NAME]`, `[ABN]`, `[LAUNCH OFFER]`, `[SHIPPING POLICY]`, `[GUARANTEE]`, `[SHIPPING REGIONS]`, `[SECURITY DETAILS]`, `[YOUR REFERRAL LINK]`.
The Privacy, Terms and Shipping footer links point to `#privacy` etc. Create those pages before launch.

## Editing the shared header and footer
The header and footer are repeated in every page. To change them in one place, edit `_source/build.py` and run `python3 _source/build.py`. It regenerates all pages into this folder (it overwrites the HTML files, not the assets).

## Animations
- A sparkle layer around the glowing child in the hero (canvas, in `main.js`), plus a soft pulsing glow.
- A page-load text sequence, twinkling stars, a moving treasure-map trail, a slowly spinning compass, scroll reveals, style crossfades, and a sparkle burst on shortlist sign-up.
- All motion switches off for visitors with "reduce motion" turned on. The sparkles pause when the hero is off screen or the tab is hidden.
