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
CNAME                  → harbourhues.ca
og-image.png           Social share image (1200×630)
```

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
