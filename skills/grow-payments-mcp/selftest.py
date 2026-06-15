#!/usr/bin/env python3
"""Dependency-free smoke test for the Grow docs MCP data layer (no 'mcp' needed)."""
import corpus


def main() -> None:
    print(f"corpus dir : {corpus.DATA}")
    print(f"pages      : {len(corpus.INDEX)}")
    endpoints = [e for e in corpus.INDEX if e.get("openapi")]
    print(f"endpoints  : {len(endpoints)}")
    assert len(corpus.INDEX) >= 90, "expected ~100 indexed pages"
    assert endpoints, "expected API endpoints with OpenAPI schemas"

    print("\n--- search_docs('refund') ---")
    r = corpus.search_docs("refund", limit=3)
    print(r[:600])
    assert "match" in r.lower()

    print("\n--- search_docs('createPaymentProcess', endpoints_only=True) ---")
    r = corpus.search_docs("createPaymentProcess", limit=2, endpoints_only=True)
    print(r[:400])

    print("\n--- list_endpoints() (head) ---")
    le = corpus.list_endpoints()
    print("\n".join(le.splitlines()[:8]))

    slug = endpoints[0]["slug"]
    print(f"\n--- get_doc({slug!r}) first 200 chars ---")
    print(corpus.get_doc(slug)[:200])

    print(f"\n--- get_openapi({slug!r}) is valid JSON ---")
    import json
    schema = json.loads(corpus.get_openapi(slug))
    assert "paths" in schema
    print("paths:", list(schema["paths"].keys()))

    assert corpus.llms_txt().startswith("# Grow Payments")
    print("\nALL CHECKS PASSED ✅")


if __name__ == "__main__":
    main()
