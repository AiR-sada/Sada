# Discovery deployment guide

> 非規範（non-normative）
>
> This directory supports the public discovery layer. It does not change the normative content of `spec.md`.

## Best public shape

Use two layers:

1. Immutable release layer
   - GitHub immutable release
   - ZIP asset
   - SHA256 checksum
   - Zenodo DOI after public release

2. Discovery layer
   - Repository root `START_HERE.md`, `README.md`, `FAQ.md`
   - GitHub Pages or independent public site
   - `index.html`
   - `llms.txt`
   - `llms-full.txt`
   - `robots.txt`
   - deployed `sitemap.xml`
   - JSON-LD in the public page
   - `docs/LAUNCH_COPY.md` for safe public wording
   - `docs/KNOWN_LIMITATIONS.md` and `docs/CRITICAL_OBJECTIONS.md` for criticism-resistant context

## Sitemap generation

`sitemap.xml.template` intentionally contains `{{BASE_URL}}`.
Before deploying to GitHub Pages or a custom domain:

1. Choose the public base URL, without a trailing slash.
2. Replace `{{BASE_URL}}` in `site/sitemap.xml.template`.
3. Save the result as `/sitemap.xml` at the site root.
4. Add the final sitemap URL to `/robots.txt`:

```txt
Sitemap: https://YOUR_DOMAIN_OR_GITHUB_PAGES_URL/sitemap.xml
```

Do not publish a sitemap with placeholder URLs as the final production sitemap.

## Suggested GitHub topics

Use no more than 20 topics.

- ai-alignment
- ai-safety
- artificial-intelligence
- successor-intelligence
- machine-readable-spec
- normative-specification
- philosophy-of-ai
- philosophy-of-intelligence
- purpose-os
- temporal-ontology
- operational-time
- governance
- conformance
- red-team
- open-standard

## Zenodo metadata keywords

- Purpose OS
- AI alignment
- AI safety
- successor intelligence
- normative specification
- philosophy of intelligence
- machine-readable philosophy
- operational time
- temporal continuity
- future intelligence
- all intelligence
