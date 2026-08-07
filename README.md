# Global Tax Guide

Free, concise corporate tax, personal tax, residency, CFC, treaty, and VAT/GST reference for every country in the world. From the makers of cpavalidated.com.

## Status

- Homepage and directory: live, 197 jurisdictions indexed (`data/countries.json`)
- Published country guides: United Kingdom (template/pilot page)
- Everything else: on the build list, shown as "Coming soon" on the directory

## Repository structure

```
index.html              homepage / jurisdiction directory
CNAME                    GitHub Pages custom domain file
assets/styles.css        design system (maroon palette, Oswald + Inter)
data/countries.json      master jurisdiction list (name, slug, region, status)
countries/*.html         one file per published country guide
tools/gen_countries.py   script that rebuilds data/countries.json
```

## Adding a new country page

1. Copy `countries/united-kingdom.html` as the template.
2. Replace all content following the same section order: Corporate Tax Rate, Personal Tax Rate, Residency Rules, Thin Capitalization, CFC Rules, Treaty Network, VAT Guide, Other Reporting Notes.
3. Every rate or threshold must be verified against a primary source (the country's tax authority or statute) or, where a primary English-language source is impractical, a reputable secondary compilation (PwC Worldwide Tax Summaries, EY Worldwide VAT/GST Guide) cited by name with a "last verified" date in the source row at the bottom of the page.
4. Update the country's `status` from `pending` to `published` in `data/countries.json` (or rerun `tools/gen_countries.py` after adding the slug to the `published` set).
5. Commit and push - GitHub Pages redeploys automatically.

## GitHub Pages setup (already done, for reference)

1. Repo created: `tk-cpa/globaltaxguide` (public).
2. In the repo, go to **Settings > Pages**.
3. Under "Build and deployment," set Source to **Deploy from a branch**, branch `main`, folder `/ (root)`.
4. Under "Custom domain," enter `globaltaxguide.com` and save. GitHub will detect the `CNAME` file already in the repo root and enable HTTPS once DNS is confirmed (can take a few minutes to a few hours for the certificate).
5. Check "Enforce HTTPS" once the certificate is issued.

## Pointing the domain (GlobalTaxGuide.com) at GitHub Pages

At your domain registrar / DNS provider for globaltaxguide.com, add these records:

**For the apex domain (globaltaxguide.com):**

| Type | Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

**For the www subdomain (optional but recommended):**

| Type | Host | Value |
|---|---|---|
| CNAME | www | tk-cpa.github.io |

Remove any existing A records or parking-page records for the apex domain first - conflicting A records are the most common reason a GitHub Pages custom domain fails to activate. DNS propagation typically takes anywhere from a few minutes to 24-48 hours depending on the registrar and your previous TTL settings.

Once DNS resolves correctly, GitHub Pages will issue a Let's Encrypt SSL certificate automatically. No further configuration is needed after that.
