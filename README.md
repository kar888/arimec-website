# ARIMEC Industries — Website

Production site for **ARIMEC INDUSTRIES**. Pure static HTML, CSS and JavaScript, auto-deployed to Cloudflare Pages on every push to `main`.

## Stack

- Static HTML/CSS/JS — no framework, no build step for the site itself
- Inter (Google Fonts) for typography
- GitHub Actions + Cloudflare Pages (Wrangler) for continuous deployment
- Optional: a small Python build script (`.build/build.py`) for DRY regeneration of shared nav/footer across About, Platforms, Projects and Contact

## Live

- **Production:** https://arimec-live.pages.dev
- **Custom domain:** (to be pointed to the Pages project)

## Structure

```
arimec-website/
├── .github/workflows/deploy.yml    # Auto-deploy to Cloudflare Pages
├── .build/                         # Python helpers (optional, regenerate pages from partials)
│   ├── partials.py                 # Shared HEAD / NAV / FOOTER constants
│   └── build.py                    # Regenerates about/platforms/projects/contact.html
└── website/                        # Everything here is deployed
    ├── index.html
    ├── about.html
    ├── platforms.html
    ├── projects.html
    ├── contact.html
    ├── style.css
    ├── app.js
    ├── favicon.svg
    └── images/
```

## Pages

| Page | Purpose |
|------|---------|
| `index.html` | Home — hero, four platforms, selected projects, approach, CTA |
| `about.html` | About — positioning, approach, site facts |
| `platforms.html` | The four platforms with detail sections |
| `projects.html` | Selected projects and pipeline initiatives |
| `contact.html` | Contact form (mailto fallback) and enquiry details |

## Design System

| Element | Value |
|---------|-------|
| Background | `#FFFFFF` (white) |
| Primary ink | `#0B1F3B` (navy) |
| Graphite | `#3B4252` |
| Line / border | `#E5E7EB` |
| Soft surface | `#F5F6F8` |
| Accent | `#C69A4B` (amber, used sparingly) |
| Font | Inter (Google Fonts) |
| Max width | 1200px |
| Voice | Institutional British English — restrained, credible |

## Editing the site

Any change to files under `website/` is auto-deployed on push to `main`. Typical workflow:

```bash
# Edit a page
# e.g. change a headline in website/index.html

# Preview locally
cd website && python3 -m http.server 5000
# open http://localhost:5000

# Ship
git add -A
git commit -m "Update homepage headline"
git push origin main

# Wait ~30 seconds, then reload arimec-live.pages.dev
```

### Using the optional Python build step

If you edit the shared nav or footer, update the strings in `.build/partials.py`, then:

```bash
python3 .build/build.py
```

This regenerates `about.html`, `platforms.html`, `projects.html` and `contact.html`. The homepage (`index.html`) is hand-authored and not touched by the builder.

## Content rules

1. **British English** throughout (authorised, recognised, practitioner, defence, analyse, colour)
2. **No defence/military/weapons language** — ADI is about *applied engineering, infrastructure resilience, performance-driven technologies*
3. **No startup clichés** — no "revolutionising", no "cutting-edge", no smiling corporate photography
4. **Concise institutional tone** — short, declarative sentences; no exaggerated claims
5. **Footer disclaimer must remain verbatim** on every page
6. **Infrastructure-only imagery** — solar farms, construction sites, data-centre cabling, clean infrastructure photography

## Deployment

Pushes to `main` trigger `.github/workflows/deploy.yml`, which uses `cloudflare/wrangler-action@v3` to deploy the `website/` directory to the `arimec-live` Cloudflare Pages project.

Required GitHub secrets:

- `CLOUDFLARE_API_TOKEN` — scoped to Pages:Edit + Account:Read on the ARIMEC Cloudflare account
- `CLOUDFLARE_ACCOUNT_ID` — the ARIMEC Cloudflare account ID

Verify the latest run:

```bash
gh run list --limit 1 --json status,conclusion,name
```

## Contact

- **Enquiries:** contact@arimec.com
- **Location:** London | International
