---
name: grow-payments-docs
description: >-
  Offline llms.txt knowledge base of the Grow Payments (grow-il / Meshulam) developer
  documentation — the Light Server REST API (regular & token payments, payment links,
  refunds, direct debit, transaction/payment-process info), webhooks, server-to-server
  callbacks, SDKs (Apple/Bit), 3DS, NFC and POS. Use this skill whenever the user asks
  how to integrate Grow / Meshulam payments, build a payment page, charge a card, create
  or refund a transaction, use tokens, set up webhooks, or understand any Grow API field,
  endpoint or error. Mixed English/Hebrew content.
---

# Grow Payments Documentation (llms.txt)

This skill bundles the **complete** scraped developer documentation of Grow Payments
(`https://grow-il.readme.io`) as a local, offline `llms.txt` corpus. Use it as the
source of truth instead of guessing or fetching the live site.

## What's here

All paths are relative to the repository root (`grow-docs-skill/`):

| Path | Contents |
|---|---|
| `data/llms.txt` | **Start here.** Curated index — every page grouped (Overview, Guides, API Reference Concepts, API Endpoints, Changelog) with a one-line description, a relative link to the page Markdown, and the live source URL. |
| `data/llms-full.txt` | The entire documentation concatenated into one file (~310 KB). Use when you want everything in context at once. |
| `data/index.json` | Machine-readable index of all 100 pages: `slug`, `title`, `section`, `type`, `group`, `url`, `path`, `description`, `is_endpoint`, `openapi`. |
| `data/pages/<section>/<slug>.md` | One Markdown file per page (sections: `home`, `docs`, `reference`, `changelog`). Each has YAML frontmatter (title/slug/type/source_url) and the rendered content, including code blocks, tables and image URLs. |
| `data/openapi/<slug>.json` | Raw OpenAPI 3.0 schema for each of the 25 API **endpoint** pages (method, path, request body, parameters, responses). |
| `data/assets/` | All 59 referenced images, plus `manifest.json` mapping original URL → local filename. |

## How to use this skill

1. **Read `data/llms.txt` first** to locate the right page(s) for the question.
2. **Open the specific `data/pages/.../<slug>.md`** file(s) the index points to. For API
   questions about an endpoint, also read the matching `data/openapi/<slug>.json` for the
   exact field-level schema.
3. For broad questions ("explain the whole payment flow") you may read `data/llms-full.txt`.
4. Cite the `source_url` from the page frontmatter when you give the user a reference link.

### Quick lookups

```bash
# search the corpus for a term (case-insensitive), list matching pages
grep -rIl -i "createPaymentProcess" data/pages

# show the index entry for endpoints only
python3 -c "import json;[print(x['title'],'->',x['path']) for x in json.load(open('data/index.json')) if x['is_endpoint']]"
```

## Key facts about the Grow API (load-bearing context)

- **Product line:** "Light" API. Server-side endpoints live under `/api/light/server/1.0/...`;
  Android/POS endpoints under `/api/light/andriod/1.0/...` (note the vendor's `andriod` spelling).
- **Sandbox host:** `https://sandbox.meshulam.co.il` (aliases: `https://sandboxapi.grow.link`).
  Production hosts are issued by Grow support — never hard-code a guessed production host.
- **Identity:** each business authenticates with its own `userId` + `pageCode` (and/or API key).
  The values shown in the docs are **examples only**; real ones come from Grow support.
- **Requests are server-to-server**, typically `multipart/form-data`. Client-side/browser
  calls to server endpoints are blocked. Do not put special characters in parameter values.
- **Core flows:** create payment process → redirect/iframe to payment page → approve
  transaction → server-to-server callback / webhook. Tokens enable repeat charges without
  re-entering card data; payment links are shareable hosted payments.

## Regenerating / updating

The corpus was produced by the scraper in `tools/` (`tools/scrape.sh`, which runs
`tools/extract.py` + `tools/build_corpus.py`). Re-run `./tools/scrape.sh` against a
fresh download of `https://grow-il.readme.io/sitemap.xml` to refresh. See the repo `README.md`.

> Content reflects the site as scraped on 2026-06-15. Verify anything security- or
> money-critical against the live site or Grow support before relying on it in production.
