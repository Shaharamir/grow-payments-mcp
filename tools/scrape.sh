#!/usr/bin/env bash
# Reproducible scrape + build of the Grow Payments docs corpus.
# Usage:  ./scrape.sh        (re-downloads only missing pages, then rebuilds)
#         FORCE=1 ./scrape.sh (wipe raw page cache and re-download everything)
set -euo pipefail
cd "$(dirname "$0")/.."   # repo root (data/, raw/ live here)
TOOLS="tools"

SITE="https://grow-il.readme.io"
mkdir -p raw raw/pages

echo "==> 1/5 sitemap"
curl -fsSL -A "Mozilla/5.0" "$SITE/sitemap.xml" -o raw/sitemap.xml
grep -o '<loc>[^<]*</loc>' raw/sitemap.xml | sed 's/<loc>//;s/<\/loc>//' > raw/urls.txt
echo "    $(wc -l < raw/urls.txt) urls"

if [ "${FORCE:-0}" = "1" ]; then rm -f raw/pages/*.html; fi

echo "==> 2/5 download pages"
python3 - <<'PY'
import urllib.request, urllib.parse, os, concurrent.futures, hashlib, json
urls=[l.strip() for l in open('raw/urls.txt') if l.strip()]
def safe(u):
    path=urllib.parse.urlparse(u).path.strip('/')
    if not path: return '_home'
    dec=urllib.parse.unquote(path); name=dec.replace('/','__')
    try: name.encode('ascii'); return name[:120]
    except UnicodeEncodeError:
        return (path.replace('/','__')[:80]+'_'+hashlib.md5(u.encode()).hexdigest()[:8])[:120]
def fetch(u):
    fn=safe(u); out=f'raw/pages/{fn}.html'
    if os.path.exists(out) and os.path.getsize(out)>1000: return (u,fn,'cached')
    req=urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req,timeout=40) as r: open(out,'wb').write(r.read())
        return (u,fn,'ok')
    except Exception as e: return (u,fn,'ERR:'+str(e)[:60])
m={}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    for u,fn,st in ex.map(fetch,urls):
        m[u]=fn
        if st.startswith('ERR'): print("   ",st,u)
json.dump(m, open('raw/url_to_file.json','w'), ensure_ascii=False, indent=1)
print("   ",len(os.listdir('raw/pages')),"pages cached")
PY

echo "==> 3/5 extract markdown + openapi"
rm -rf data/pages data/openapi
python3 "$TOOLS/extract.py"

echo "==> 4/5 download images"
mkdir -p data/assets
python3 - <<'PY'
import json, urllib.request, os, hashlib, concurrent.futures
imgs=json.load(open('raw/images.json',encoding='utf-8'))
def fetch(u):
    base=os.path.basename(u.split('?')[0]); name=base[-80:] if len(base)>80 else base
    if not name: name=hashlib.md5(u.encode()).hexdigest()
    out=f'data/assets/{name}'
    if os.path.exists(out) and os.path.getsize(out)>0: return (u,name)
    try:
        req=urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=40) as r: open(out,'wb').write(r.read())
    except Exception as e: print("   ERR",str(e)[:50],u); return (u,None)
    return (u,name)
man={}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    for u,name in ex.map(fetch,imgs):
        if name: man[u]=name
json.dump(man, open('data/assets/manifest.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print("   ",len([f for f in os.listdir('data/assets') if f!='manifest.json']),"images")
PY

echo "==> 5/6 build llms.txt / llms-full.txt / index.json"
python3 "$TOOLS/build_corpus.py"

echo "==> 6/6 merge unified OpenAPI + Postman collection"
python3 "$TOOLS/build_api.py"
echo "DONE."
