#!/usr/bin/env python3
"""
Pure (dependency-free) access layer over the Grow Payments docs corpus.

server.py wraps these functions as MCP tools; selftest.py calls them directly.
Resolves the corpus from $GROW_DOCS_DATA -> <repo-root>/data -> ./data.
"""
from __future__ import annotations
import json, os, re
from pathlib import Path


def resolve_data_dir() -> Path:
    env = os.environ.get("GROW_DOCS_DATA")
    candidates = []
    if env:
        candidates.append(Path(env))
    here = Path(__file__).resolve()
    candidates.append(here.parent.parent.parent / "data")  # repo-root/data
    candidates.append(Path.cwd() / "data")
    for c in candidates:
        if (c / "index.json").exists():
            return c
    raise FileNotFoundError(
        "Could not locate the Grow docs 'data/' dir (need data/index.json). "
        "Set GROW_DOCS_DATA to its absolute path."
    )


DATA = resolve_data_dir()
INDEX = json.loads((DATA / "index.json").read_text(encoding="utf-8"))
BY_SLUG = {e["slug"]: e for e in INDEX}

_BODIES: dict[str, str] = {}
for _e in INDEX:
    _p = DATA / _e["path"]
    if _p.exists():
        _BODIES[_e["slug"]] = _p.read_text(encoding="utf-8")


def strip_frontmatter(md: str) -> str:
    return re.sub(r"^---.*?---\s*", "", md, count=1, flags=re.S)


def _snippet(text: str, query: str, width: int = 220) -> str:
    low = text.lower()
    i = low.find(query.lower())
    if i < 0:
        return text[:width].replace("\n", " ").strip()
    start = max(0, i - width // 2)
    seg = text[start : start + width].replace("\n", " ").strip()
    return ("…" if start > 0 else "") + seg + "…"


def search_docs(query: str, limit: int = 8, endpoints_only: bool = False) -> str:
    q = query.strip().lower()
    terms = [t for t in re.split(r"\s+", q) if t]
    results = []
    for e in INDEX:
        if endpoints_only and not e["is_endpoint"]:
            continue
        body = _BODIES.get(e["slug"], "")
        hay = "\n".join([e["title"], e.get("description", ""), e.get("url", ""), body]).lower()
        if not terms:
            continue
        score = 0
        for t in terms:
            c = hay.count(t)
            if c == 0:
                score = -1
                break
            score += c
            if t in e["title"].lower():
                score += 50
            if t in (e.get("description") or "").lower():
                score += 10
        if score <= 0:
            continue
        results.append((score, e, _snippet(strip_frontmatter(body), terms[0])))
    results.sort(key=lambda r: r[0], reverse=True)
    if not results:
        return f"No matches for {query!r}. Try list_docs() or broader terms."
    out = [f"{len(results)} match(es) for {query!r} (showing {min(limit, len(results))}):", ""]
    for score, e, snip in results[:limit]:
        tag = f" [{e['type']}]" if e["is_endpoint"] else ""
        out.append(f"### {e['title']}{tag}")
        out.append(f"- slug: `{e['slug']}`  | group: {e['group']}")
        out.append(f"- source: {e['url']}")
        if e.get("openapi"):
            out.append(f"- openapi: `{e['slug']}` (use get_openapi)")
        out.append(f"- {snip}")
        out.append("")
    return "\n".join(out)


def get_doc(slug: str) -> str:
    e = BY_SLUG.get(slug)
    if not e:
        for cand in INDEX:
            if slug in (cand["path"], cand["url"]) or slug.rstrip("/").endswith(cand["slug"]):
                e = cand
                break
    if not e:
        return f"Unknown slug {slug!r}. Use list_docs() or search_docs() to find valid slugs."
    return _BODIES.get(e["slug"], "(content unavailable)")


def list_docs(section: str = "", group: str = "") -> str:
    rows = INDEX
    if section:
        rows = [e for e in rows if e["section"] == section]
    if group:
        rows = [e for e in rows if (e.get("group") or "").lower() == group.lower()]
    if not rows:
        return "No pages match that filter."
    rows = sorted(rows, key=lambda e: (e.get("group") or "", e["title"].lower()))
    out = [f"{len(rows)} page(s):", ""]
    cur = None
    for e in rows:
        if e.get("group") != cur:
            cur = e.get("group")
            out.append(f"\n## {cur}")
        out.append(f"- `{e['slug']}` — {e['title']}")
    return "\n".join(out)


def list_endpoints() -> str:
    out = ["Grow Payments API endpoints:", ""]
    n = 0
    for e in INDEX:
        if not e.get("openapi"):
            continue
        # the canonical operation this page documents
        if e.get("method") and e.get("api_path"):
            line = f"{e['method']} {e['api_path']}"
        else:
            try:
                schema = json.loads((DATA / e["openapi"]).read_text(encoding="utf-8"))
                paths = schema.get("paths", {})
                line = "; ".join(
                    f"{verb.upper()} {path}"
                    for path, ops in paths.items()
                    for verb in ops
                    if isinstance(ops[verb], dict)
                )
            except Exception:
                line = "(schema unreadable)"
        n += 1
        out.append(f"- `{e['slug']}` — {e['title']}  →  {line}")
    out.insert(1, f"{n} endpoints\n")
    return "\n".join(out)


def get_openapi(slug: str) -> str:
    e = BY_SLUG.get(slug)
    if not e or not e.get("openapi"):
        return f"No OpenAPI schema for slug {slug!r}. Use list_endpoints() for valid slugs."
    return (DATA / e["openapi"]).read_text(encoding="utf-8")


def llms_txt() -> str:
    return (DATA / "llms.txt").read_text(encoding="utf-8")


def llms_full_txt() -> str:
    return (DATA / "llms-full.txt").read_text(encoding="utf-8")
