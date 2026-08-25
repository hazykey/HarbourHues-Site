# Harbour Hues Media — Photography Site

## Project Overview
Photography portfolio and business site for Harbour Hues Media.

- **Live URL:** https://harbourhues.ca
- **GitHub Repo:** https://github.com/hazykey/HarbourHues-Site
- **Project Path:** `/Users/iankehayes/Developer/Projects/Claude Code Photography Site`

## Local Development
```bash
python3 -m http.server 3000
```
Port is auto-assigned if 3000 is busy.

## Deployment
```bash
git add <files>
git commit -m "message"
git push origin main
```
GitHub Pages serves from `main` branch with CNAME `harbourhues.ca`.

## Site Structure
```
index.html             Homepage
portraits/index.html   Portrait gallery
maternity-events/      Maternity & events
landscapes/            Landscape gallery
restoration/           Photo restoration
design/                Design work
img/                   All images
client-downloads/      Client photo-delivery pages (unlisted, noindex)
studio/                Client page generator (unlisted, noindex)
robots.txt             Allows crawling; noindex tags do the excluding
sitemap.xml            Public pages only
CNAME                  → harbourhues.ca
og-image.png           Social share image (1200×630)
```

## Client Downloads (private)
Lightweight landing pages that hand a client their Dropover link. Not in the
nav, not in `sitemap.xml`, `noindex, nofollow` on every page. `robots.txt`
deliberately has no `Disallow` rule: blocking the crawl would stop Google
reading the noindex tag, and would advertise the paths to anyone curious.

- `studio/index.html` — the generator, live at `harbourhues.ca/studio/`.
  Unlisted and noindexed, but readable by anyone who finds the URL. It holds
  no client data and talks to no server, so there is nothing there to leak.
- `studio/_template.html` — the page template the generator fills in. The
  generator carries an embedded copy (no server, and it must also work from
  `file://`), so run `python3 studio/_sync.py` after editing the template.
- Slug format: `firstname-firstname2-monyyyy`, plus a random 6-character
  suffix by default (e.g. `chris-cintia-aug2025-sg94xu`) so the URL cannot be
  guessed from the client's names and the month.
- Publish a page as `client-downloads/<slug>/index.html`. From a phone, use
  the generator's **Copy HTML** button and GitHub's *Create new file*.

**This repo is public.** Anything committed under `client-downloads/` is
world-readable on GitHub and stays in git history after deletion. Never put a
gallery password on a client page; send it by email or text. Treat the Dropover
link itself as published the moment it is committed, so keep Dropover expiry
short and rely on a password Dropover enforces rather than on the URL being
secret.

## OG Image Generation
Use headless Brave Browser:
```bash
"/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" \
  --headless=new --screenshot="/tmp/og-final.png" \
  --window-size=1200,630 --hide-scrollbars \
  --force-color-profile=srgb --disable-gpu \
  "http://localhost:3000/"
```

## Tech Notes
- Pure HTML/CSS, no frameworks
- Images in `img/` — use optimized/compressed versions
- Use `gh` CLI for GitHub operations (not raw git where possible)

## Ian's Preferences
- Ask yes/no questions with suggestions, not open-ended questions
- Keep HTML clean and semantic
- Projects live at `/Users/iankehayes/Developer/Projects/`
