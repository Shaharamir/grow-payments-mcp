#!/usr/bin/env python3
"""
Merge the per-endpoint OpenAPI specs (data/openapi/*.json) — each of which embeds a
multi-path collection — into ONE clean OpenAPI 3.0 document plus a Postman v2.1
collection for the whole Grow Payments "Light" API.

Output:
    data/openapi/_grow-payments-light-api.openapi.json
    data/postman/grow-payments-light-api.postman_collection.json

Run from repo root:  python3 tools/build_api.py
"""
import json, os, glob

SRC = sorted(glob.glob("data/openapi/*.json"))
SRC = [f for f in SRC if not os.path.basename(f).startswith("_")]

servers, schemes = {}, {}
# op key (METHOD path) -> (score, path, method, op)
best = {}

def score(op):
    s = 0
    s += len(op.get("parameters") or [])
    for ct in (op.get("requestBody") or {}).get("content", {}).values():
        s += len((ct.get("schema") or {}).get("properties") or {})
    s += len(op.get("responses") or {})
    s += 1 if op.get("description") else 0
    return s

for f in SRC:
    try:
        spec = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    for srv in spec.get("servers") or []:
        if srv.get("url"):
            servers[srv["url"]] = srv
    for k, v in ((spec.get("components") or {}).get("securitySchemes") or {}).items():
        schemes[k] = v
    for path, ops in (spec.get("paths") or {}).items():
        if not isinstance(ops, dict):
            continue
        for method, op in ops.items():
            if not isinstance(op, dict):
                continue
            key = f"{method.upper()} {path}"
            sc = score(op)
            if key not in best or sc > best[key][0]:
                best[key] = (sc, path, method, op)

# assemble merged OpenAPI
paths = {}
for sc, path, method, op in best.values():
    paths.setdefault(path, {})[method] = op

merged = {
    "openapi": "3.0.0",
    "info": {
        "title": "Grow Payments — Light API (unofficial, merged)",
        "version": "1.0.0",
        "description": (
            "Unofficial merged OpenAPI spec for the Grow Payments (Meshulam) Light API, "
            "assembled from https://grow-il.readme.io. Not affiliated with Grow/Meshulam. "
            "Identifiers (userId/pageCode) are per-business and issued by Grow support."
        ),
    },
    "servers": list(servers.values()) or [{"url": "https://sandbox.meshulam.co.il"}],
    "paths": dict(sorted(paths.items())),
}
if schemes:
    merged["components"] = {"securitySchemes": schemes}

os.makedirs("data/openapi", exist_ok=True)
out_oas = "data/openapi/_grow-payments-light-api.openapi.json"
json.dump(merged, open(out_oas, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# Postman collection
base = (list(servers) or ["https://sandbox.meshulam.co.il"])[0]
items = []
for path in sorted(paths):
    for method, op in paths[path].items():
        url = base.rstrip("/") + path
        seg = [s for s in path.strip("/").split("/") if s]
        req = {
            "method": method.upper(),
            "header": [],
            "url": {"raw": url, "host": [base], "path": seg},
        }
        # multipart/form-data body
        rb = (op.get("requestBody") or {}).get("content", {})
        form = rb.get("multipart/form-data") or rb.get("application/x-www-form-urlencoded")
        if form:
            props = (form.get("schema") or {}).get("properties") or {}
            req["body"] = {
                "mode": "formdata",
                "formdata": [
                    {"key": k, "value": str((v or {}).get("example", "")),
                     "type": "text", "description": (v or {}).get("description", "")}
                    for k, v in props.items()
                ],
            }
            req["header"].append({"key": "Content-Type", "value": "multipart/form-data"})
        items.append({"name": f"{method.upper()} {op.get('summary') or path}", "request": req})

collection = {
    "info": {
        "name": "Grow Payments — Light API (unofficial)",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
        "description": "Unofficial Postman collection for the Grow Payments (Meshulam) Light API. Not affiliated with Grow/Meshulam.",
    },
    "item": items,
    "variable": [{"key": "baseUrl", "value": base}],
}
os.makedirs("data/postman", exist_ok=True)
out_pm = "data/postman/grow-payments-light-api.postman_collection.json"
json.dump(collection, open(out_pm, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print(f"source specs        : {len(SRC)}")
print(f"unique operations   : {len(best)}")
print(f"unique paths        : {len(paths)}")
print(f"servers             : {len(servers)}")
print(f"-> {out_oas}")
print(f"-> {out_pm}")
