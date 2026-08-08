# Global Tax Guide - Site Maintenance & Operations Manual

**Site:** globaltaxguide.com
**GitHub Repo:** https://github.com/tk-cpa/globaltaxguide
**Branch:** main (deploys via GitHub Pages)
**Owner:** tk.cpa AI Lab

---

## 1. Deployment architecture

Plain static HTML/CSS/JS. No build step, no npm, no server-side rendering. Push to `main`, GitHub Pages serves it.

## 2. Header and footer: single source of truth (as of August 8, 2026)

**Do not hand-edit `<header class="site-header">` or `<footer class="site-footer">` blocks in individual page files.** Every page's header and footer is generated from two canonical files:

- `partials/header.html`
- `partials/footer.html`

Each contains `{{HOME}}` and `{{BASE}}` tokens, substituted per-file depending on directory depth:

| File location | HOME | BASE |
|---|---|---|
| Root pages (`index.html`, `about.html`, `map.html`, `zones.html`, `unions.html`, `trusted-resources.html`, `mission.html`, `disclaimer.html`) | `./` | `` (empty) |
| `countries/*.html` | `../` | `../` |

### To change the header or footer sitewide

1. Edit `partials/header.html` and/or `partials/footer.html` only.
2. Run `tools/apply_partials.py` (requires `GH_TOKEN` in the environment).
3. It rewrites the `<header>`/`<footer>` block in every HTML file on the site and pushes the result as **one atomic git tree commit** (not 230 separate commits).

This was deliberately built as a build-time propagation script rather than a client-side JS include (the pattern cpavalidated.com's `shared.js` uses for nav only). Reasoning: crawlers and LLMs that don't execute JavaScript need the real header/footer markup present in the HTML that's actually served, not injected after page load. A JS-injected header/footer would be invisible to any non-JS-executing crawler and would also risk the layout-shift issues `shared.js` has on cpavalidated.com.

### If you add a new root-level page

Add its filename to the `ROOT_PAGES` list at the top of `tools/apply_partials.py` before running it, or it won't get the header/footer treatment automatically.

### Why this exists

Prior to August 8, 2026, header and footer HTML was hand-duplicated into every one of 229+ country pages plus the hub pages, with no single source of truth - the same weakness cpavalidated.com still has today (documented "canonical snippet to copy-paste" in its own MAINTENANCE.md, no propagation script). This was flagged as unacceptable for a site aiming for full consistency and AI/crawler-friendliness, and fixed the same session it was raised. If a future session is tempted to hand-edit a header or footer in a single file "just this once," don't - fix the partial and run the script instead, or the drift comes back.

## 3. Footer structure (current)

The footer has three parts:
1. Tagline + link row (`tk.cpa`, `cpavalidated.com`, `About`) - `tk.cpa` links to the parent practice, `cpavalidated.com` to the sister US-tax-focused resource, `About` stays in-site.
2. A full disclaimer paragraph, present on every page (previously this only existed as an easy-to-miss low-opacity line on the homepage and about page - now sitewide).
3. A "Full disclaimer" link to `disclaimer.html`, a dedicated page (mirrors cpavalidated.com's `disclaimer.html`, which GTG didn't have until this was built).

## 4. Country page content build

See `QUEUE.md` for the live work queue, verification standard, and session-by-session history of which countries have full Residency/CFC/Thin Cap/Foreign Account Reporting/Treaty Network narrative content versus placeholder-only pages.

## 5. Things that break the site

- Editing a header/footer directly inside a single page file instead of through the partials + script. Causes drift, defeats the entire point of section 2.
- Adding a new root-level page without adding it to `ROOT_PAGES` in `tools/apply_partials.py`.
- Forgetting that `raw.githubusercontent.com` caches for a few minutes - always verify recent pushes via the Contents API (`gh.fetch()`), not the raw CDN URL, when checking whether a push actually landed.
