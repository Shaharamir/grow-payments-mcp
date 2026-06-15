#!/usr/bin/env python3
"""
Grow Payments documentation MCP server (stdio).

Exposes the scraped Grow Payments (grow-il / Meshulam) developer docs over the
Model Context Protocol as searchable tools + llms.txt resources. All data access
lives in corpus.py (dependency-free); this file only wires it to FastMCP.

Run:
    pip install "mcp>=1.2.0"
    python server.py

The corpus dir is resolved as $GROW_DOCS_DATA -> <repo-root>/data -> ./data.
"""
from __future__ import annotations
import sys

try:
    from mcp.server.fastmcp import FastMCP
except ModuleNotFoundError:
    sys.stderr.write(
        "ERROR: the 'mcp' package is required. Install with:  pip install 'mcp>=1.2.0'\n"
        "(For a dependency-free smoke test of the data layer, run selftest.py instead.)\n"
    )
    raise

import corpus

mcp = FastMCP(
    "grow-payments-docs",
    instructions=(
        "Searchable knowledge base for the Grow Payments (grow-il / Meshulam) developer "
        "documentation: Light Server REST API (payments, tokens, payment links, refunds, "
        "direct debit, transaction info), webhooks, SDKs, 3DS, NFC, POS. "
        "Use search_docs to find pages, get_doc to read one, list_endpoints + get_openapi "
        "for exact API schemas. Sandbox host: https://sandbox.meshulam.co.il."
    ),
)


@mcp.tool()
def search_docs(query: str, limit: int = 8, endpoints_only: bool = False) -> str:
    """Ranked full-text search across all Grow Payments docs (titles, descriptions, body, API paths)."""
    return corpus.search_docs(query, limit, endpoints_only)


@mcp.tool()
def get_doc(slug: str) -> str:
    """Return the full Markdown of one doc page by slug (also accepts a path or URL)."""
    return corpus.get_doc(slug)


@mcp.tool()
def list_docs(section: str = "", group: str = "") -> str:
    """List pages, optionally filtered by section (home|docs|reference|changelog) or group."""
    return corpus.list_docs(section, group)


@mcp.tool()
def list_endpoints() -> str:
    """List all Grow API endpoints (method + path) that have an OpenAPI schema."""
    return corpus.list_endpoints()


@mcp.tool()
def get_openapi(slug: str) -> str:
    """Return the raw OpenAPI 3.0 JSON schema for an API endpoint page (by slug)."""
    return corpus.get_openapi(slug)


@mcp.resource("grow://llms.txt")
def llms_txt() -> str:
    """The curated llms.txt index of the whole documentation set."""
    return corpus.llms_txt()


@mcp.resource("grow://llms-full.txt")
def llms_full_txt() -> str:
    """The entire documentation concatenated into one file."""
    return corpus.llms_full_txt()


if __name__ == "__main__":
    mcp.run()
