<div align="center">

<img src="media/grow-logo.png" alt="Grow Payments logo" width="84" height="84" />

# Grow Payments — LLM-ready API knowledge base (`llms.txt` + MCP)

🌐 **Bilingual content — English & Hebrew (עברית)** &nbsp;·&nbsp; 🇮🇱 Israeli payment gateway

### ⚠️ UNOFFICIAL — WE ARE NOT GROW / Meshulam. Not affiliated. Not endorsed.

בסיס ידע **לא רשמי** לתיעוד המפתחים של **Grow / משולם** — מותאם ל‑LLM: קורפוס `llms.txt` ושרת MCP.
התוכן **דו‑לשוני** (אנגלית + עברית). זהו פרויקט עצמאי — **איננו Grow / משולם ואיננו מסונפים אליהם.**

</div>

---

> **Unofficial, LLM-ready knowledge base of the [Grow Payments](https://grow-il.readme.io) (Meshulam / grow.link) developer documentation** — the complete **Light API** reference, OpenAPI schemas, integration guides and changelog, packaged as an [`llms.txt`](https://llmstxt.org) corpus **and** a [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server.

Built for developers and AI agents (Claude, Cursor, etc.) that need accurate, grep-able
answers about **Grow / Meshulam payment integration** without crawling a JavaScript
documentation site every time. The original docs — and therefore much of this corpus — are
written in a **mix of English and Hebrew (עברית)**.

<!-- keywords: grow payments api, meshulam api, grow.link, israel payment gateway,
     light api, createPaymentProcess, payment page, token payment, payment link, refund,
     direct debit, webhooks, llms.txt, mcp, model context protocol, openapi, claude, llm -->

---

## Why

The official docs at `grow-il.readme.io` are a client-rendered SPA — hard for LLMs and
scripts to consume, and mixed English/Hebrew. This repo turns the **entire site** into:

- 📄 **`data/llms.txt`** — a clean, grouped index of every page (the [llms.txt standard](https://llmstxt.org)).
- 📚 **`data/llms-full.txt`** — the whole documentation set in one ~310 KB file.
- 🗂️ **`data/pages/**.md`** — one Markdown file per page (guides + API reference).
- 🔌 **`data/openapi/*.json`** — OpenAPI 3.0 schema for each API endpoint.
- 🤖 **`skills/grow-payments-mcp`** — an MCP server exposing it all as search tools.

## What's inside

| | Count |
|---|---|
| Documentation pages | **100** |
| Integration guides | 10 |
| API reference pages | 84 |
| API endpoints with OpenAPI schemas | **25** |
| Changelog entries | 5 |

Covers: hosted **payment pages**, the **Light Server REST API** (regular & **token**
payments, **payment links**, **refunds**, **direct debit**, transaction & payment-process
info), **webhooks** / server-to-server callbacks, **3DS**, **NFC**, **POS** devices, and
the Apple / Bit **SDKs**.

```
.
├── data/                       # the corpus (single source of truth)
│   ├── llms.txt                #   grouped index  (start here)
│   ├── llms-full.txt           #   everything, one file
│   ├── index.json              #   machine-readable index
│   ├── pages/{home,docs,reference,changelog}/*.md
│   └── openapi/*.json          #   per-endpoint OpenAPI 3.0
├── skills/
│   ├── grow-payments-docs/     #   llms.txt skill  (read files directly)
│   └── grow-payments-mcp/      #   MCP server      (search via tools)
└── tools/                      # reproducible scraper (scrape.sh, extract.py, build_corpus.py)
```

---

## Quick start

### Option A — just read it (no install)

Point your LLM / agent / script at [`data/llms.txt`](data/llms.txt) and open the pages it
links to. For example:

```bash
git clone https://github.com/Shaharamir/grow-payments-mcp.git
cd grow-payments-mcp
grep -rIl -i "refund" data/pages        # find pages
cat data/pages/reference/post_api-light-server-1-0-refundtransaction-1.md
```

### Option B — MCP server (search tools for Claude / any MCP client)

Requires **Python ≥ 3.10**.

```bash
python3 -m venv .venv
.venv/bin/pip install -r skills/grow-payments-mcp/requirements.txt
.venv/bin/python skills/grow-payments-mcp/selftest.py     # offline smoke test
```

Register with your MCP client (copy [`.mcp.json.example`](.mcp.json.example) →
`.mcp.json` and set absolute paths):

```json
{
  "mcpServers": {
    "grow-payments-docs": {
      "command": "/abs/path/grow-payments-mcp/.venv/bin/python",
      "args": ["/abs/path/grow-payments-mcp/skills/grow-payments-mcp/server.py"],
      "env": { "GROW_DOCS_DATA": "/abs/path/grow-payments-mcp/data" }
    }
  }
}
```

**Tools:** `search_docs`, `get_doc`, `list_docs`, `list_endpoints`, `get_openapi`.
**Resources:** `grow://llms.txt`, `grow://llms-full.txt`.

> Example prompt once connected: *"Using grow-payments-docs, show the request fields for
> `createPaymentProcess` and the refund endpoint's OpenAPI schema."*

---

## Grow API cheat-sheet

- **Endpoints:** server → `/api/light/server/1.0/...`; Android/POS → `/api/light/andriod/1.0/...` (vendor spelling).
- **Sandbox host:** `https://sandbox.meshulam.co.il` (alias `https://sandboxapi.grow.link`). Production hosts are issued by Grow support.
- **Auth:** per-business `userId` + `pageCode` (and/or API key). Values shown in the docs are examples only.
- **Calls** are server-to-server, usually `multipart/form-data`; client-side requests are blocked.

---

## Keeping it fresh

The corpus is regenerated from the live site (ReadMe.io embeds page content + OpenAPI in a
`ssr-props` JSON blob, which the scraper parses):

```bash
python3 -m pip install markdownify beautifulsoup4
./tools/scrape.sh            # incremental;  FORCE=1 ./tools/scrape.sh  re-downloads all
```

---

## ⚠️ Disclaimer — this is NOT official

**We are not Grow Payments / Meshulam.** This is an independent, community-made,
**unofficial** mirror. It is **not affiliated with, authorized by, sponsored by, or endorsed
by** Grow Payments, Meshulam, or grow.link in any way.

All product names, trademarks, logos and brands — including the **Grow logo** shown above —
are the property of their respective owners and are used here purely to identify the
documentation this project mirrors (nominative use), not to imply any affiliation.

Documentation content under `data/` is © Grow Payments and reproduced here for developer
convenience; the repository **code** is MIT-licensed (see [LICENSE](LICENSE)). Always verify
money- or security-critical details against the [official docs](https://grow-il.readme.io)
or Grow support before using in production. **Rights holders:** open an issue and any
content will be amended or removed promptly.

> בעברית: זהו פרויקט **לא רשמי** ועצמאי. **איננו Grow / משולם** ואיננו מסונפים אליהם, מורשים
> או נתמכים על ידם. כל הסימנים המסחריים והלוגו שייכים לבעליהם. לבעלי הזכויות: פתחו issue
> ונסיר/נתקן כל תוכן לפי בקשה.

_Snapshot: 2026-06-15._
