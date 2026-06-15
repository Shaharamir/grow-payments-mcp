---
name: grow-payments-mcp
description: >-
  Runs a local Model Context Protocol (MCP) server that exposes the Grow Payments
  (grow-il / Meshulam) developer documentation as searchable tools — search_docs,
  get_doc, list_docs, list_endpoints, get_openapi — plus llms.txt resources. Use this
  skill when the user wants to query Grow / Meshulam payment docs through MCP, wire the
  Grow docs into an MCP-capable client (Claude Code / Claude Desktop), or get exact
  OpenAPI schemas for Grow API endpoints (payments, tokens, payment links, refunds,
  direct debit, transactions, webhooks, SDKs, 3DS, NFC, POS).
---

# Grow Payments Docs — MCP Server

A stdio MCP server that serves the bundled Grow Payments documentation corpus
(`data/`) as tools and resources. Same content as the `grow-payments-docs`
llms.txt skill, but queryable over MCP so any MCP client can search and fetch it.

## Files

| Path | Purpose |
|---|---|
| `server.py` | The MCP server (Python, `FastMCP`). Resolves the corpus from `$GROW_DOCS_DATA`, else `<repo>/data`, else `./data`. |
| `requirements.txt` | Single dependency: `mcp>=1.2.0`. |
| `mcp.json` | Example client registration block. |

## Tools exposed

| Tool | Description |
|---|---|
| `search_docs(query, limit=8, endpoints_only=False)` | Ranked full-text search over titles, descriptions, bodies and API paths; returns snippets. |
| `get_doc(slug)` | Full Markdown of one page (accepts slug, path, or URL). |
| `list_docs(section="", group="")` | List/browse pages by section (`home\|docs\|reference\|changelog`) or group. |
| `list_endpoints()` | All 25 API endpoints with method + path. |
| `get_openapi(slug)` | Raw OpenAPI 3.0 JSON schema for an endpoint. |

Resources: `grow://llms.txt` (curated index) and `grow://llms-full.txt` (everything).

## Setup

Requires **Python ≥ 3.10** (the `mcp` SDK does not support 3.9). Use a virtualenv
(modern macOS/Homebrew Python is PEP-668 "externally managed"):

```bash
# from the repo root
python3.12 -m venv .venv               # any python >=3.10
.venv/bin/pip install -r skills/grow-payments-mcp/requirements.txt
.venv/bin/python skills/grow-payments-mcp/server.py   # stdio server (Ctrl-C to stop)
```

## Register with an MCP client

Add to the client's MCP config (e.g. Claude Code `.mcp.json` or Claude Desktop
`claude_desktop_config.json`). Use an **absolute** path to `server.py` and, if the
client's working directory differs, set `GROW_DOCS_DATA` to the absolute `data/` path:

```json
{
  "mcpServers": {
    "grow-payments-docs": {
      "command": "/ABS/PATH/grow-docs-skill/.venv/bin/python",
      "args": ["/ABS/PATH/grow-docs-skill/skills/grow-payments-mcp/server.py"],
      "env": { "GROW_DOCS_DATA": "/ABS/PATH/grow-docs-skill/data" }
    }
  }
}
```

(Point `command` at the venv's python so the `mcp` dependency is on the path.)

## Smoke test (no MCP client needed)

```bash
python3 skills/grow-payments-mcp/selftest.py
```

This imports the server module's logic and runs `search_docs`, `list_endpoints`,
`get_doc` and `get_openapi` against the corpus, printing results — confirms the data
wiring works before you connect a client.

> The server is **read-only** and fully offline. Content reflects the scrape of
> `https://grow-il.readme.io` on 2026-06-15.
