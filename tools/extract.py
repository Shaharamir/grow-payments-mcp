import re, json, os, urllib.parse, collections
from bs4 import BeautifulSoup
from markdownify import markdownify as md2

URLMAP=json.load(open('raw/url_to_file.json',encoding='utf-8'))
FILE2URL={v:k for k,v in URLMAP.items()}

def ssr(path):
    html=open(path,encoding='utf-8').read()
    m=re.search(r'<script id="ssr-props"[^>]*>(.*?)</script>', html, re.S)
    if not m: return None
    try: return json.loads(m.group(1))
    except Exception: return None

def section_of(url):
    p=urllib.parse.urlparse(url).path.strip('/')
    if not p: return 'home'
    return p.split('/')[0]

def html_to_md(body):
    if not body: return ""
    soup=BeautifulSoup(body,'html.parser')
    for t in soup(['style','script']): t.decompose()
    html=str(soup)
    text=md2(html, heading_style="ATX", bullets="-", strip=['style','script'], escape_asterisks=False, escape_underscores=False)
    # collapse 3+ newlines
    text=re.sub(r'\n{3,}','\n\n',text).strip()
    return text

IMG=set()
def collect_images(body, base="https://grow-il.readme.io"):
    if not body: return []
    out=[]
    for m in re.finditer(r'src="([^"]+)"', body):
        u=m.group(1)
        if u.startswith('//'): u='https:'+u
        if u.startswith('/'): u=base+u
        if any(d in u for d in ['files.readme.io','cdn.readme.io','readme.io/api/v1']):
            out.append(u); IMG.add(u)
    return out

def render_openapi(api):
    """Render document.api (method,path,schema) into structured markdown."""
    method=api.get('method','').upper(); path=api.get('path','')
    schema=api.get('schema') or {}
    lines=[f"## `{method} {path}`",""]
    servers=schema.get('servers') or []
    if servers:
        lines.append("**Servers:**")
        for s in servers: lines.append(f"- {s.get('url')}")
        lines.append("")
    paths=schema.get('paths') or {}
    want_path=api.get('path'); want_verb=api.get('method','').lower()
    if want_path in paths and want_verb in (paths.get(want_path) or {}):
        selected=[(want_path, {want_verb: paths[want_path][want_verb]})]
    else:
        selected=list(paths.items())
    for pth,ops in selected:
        for verb,op in ops.items():
            if not isinstance(op,dict): continue
            summ=op.get('summary'); desc=op.get('description')
            if summ: lines.append(f"**Summary:** {summ}")
            if desc: lines.append(f"\n{desc}\n")
            # params
            params=op.get('parameters') or []
            if params:
                lines.append("\n**Parameters:**\n")
                lines.append("| Name | In | Type | Required | Description |")
                lines.append("|---|---|---|---|---|")
                for pa in params:
                    sc=pa.get('schema') or {}
                    lines.append(f"| {pa.get('name','')} | {pa.get('in','')} | {sc.get('type','')} | {pa.get('required',False)} | {(pa.get('description') or '').replace(chr(10),' ')} |")
            # request body
            rb=op.get('requestBody') or {}
            content=rb.get('content') or {}
            for ct,cv in content.items():
                sc=cv.get('schema') or {}
                props=sc.get('properties') or {}
                req=set(sc.get('required') or [])
                if props:
                    lines.append(f"\n**Request body** (`{ct}`):\n")
                    lines.append("| Field | Type | Required | Description |")
                    lines.append("|---|---|---|---|")
                    for fn,fv in props.items():
                        fv=fv or {}
                        d=(fv.get('description') or '').replace('\n',' ')
                        ex=fv.get('example')
                        if ex is not None and not d: d=f"e.g. {ex}"
                        lines.append(f"| {fn} | {fv.get('type','')} | {fn in req} | {d} |")
            # responses
            resp=op.get('responses') or {}
            if resp:
                lines.append("\n**Responses:**\n")
                for code,rv in resp.items():
                    rv=rv or {}
                    lines.append(f"- `{code}` — {rv.get('description','')}")
            # code samples (readme extension)
            cs=op.get('x-readme',{}).get('code-samples') if isinstance(op.get('x-readme'),dict) else None
            cs=cs or op.get('x-code-samples') or op.get('x-codeSamples')
            if cs:
                lines.append("\n**Code samples:**\n")
                for s in cs:
                    lang=s.get('language','') 
                    lines.append(f"```{lang}\n{s.get('code','')}\n```")
    return "\n".join(lines)

records=[]
for fn,url in FILE2URL.items():
    path=f'raw/pages/{fn}.html'
    if not os.path.exists(path): continue
    d=ssr(path)
    if not d: 
        print("no ssr-props:", fn); continue
    doc=d.get('document') or {}
    meta=d.get('meta') or {}
    title=doc.get('title') or meta.get('title') or fn
    slug=doc.get('slug') or meta.get('slug') or fn
    dtype=doc.get('type') or meta.get('type') or 'basic'
    sect=section_of(url)
    body_html=(d.get('rdmd') or {}).get('dehydrated',{}).get('body') or ''
    excerpt=(doc.get('content') or {}).get('excerpt') or ''
    imgs=collect_images(body_html)
    body_md=html_to_md(body_html)
    api=doc.get('api')
    api_md=""; api_method=None; api_path=None
    if isinstance(api,dict) and api.get('schema'):
        api_md=render_openapi(api)
        api_method=(api.get('method') or '').upper() or None
        api_path=api.get('path')
        os.makedirs('data/openapi',exist_ok=True)
        json.dump(api['schema'], open(f'data/openapi/{slug}.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
    records.append(dict(fn=fn,url=url,title=title,slug=slug,type=dtype,section=sect,
                        excerpt=excerpt,body_md=body_md,api_md=api_md,imgs=imgs,
                        api_method=api_method,api_path=api_path))

# write per-page md
counts=collections.Counter()
for r in records:
    sect=r['section']
    if sect=='discuss': continue   # empty forum landing, no content
    counts[sect]+=1
    outdir=f"data/pages/{sect}"; os.makedirs(outdir,exist_ok=True)
    fm=["---",
        f"title: {json.dumps(r['title'],ensure_ascii=False)}",
        f"slug: {r['slug']}",
        f"type: {r['type']}",
        f"section: {sect}",
        f"source_url: {r['url']}",
        "---",""]
    parts=["\n".join(fm), f"# {r['title']}\n"]
    if r['excerpt']: parts.append(f"> {r['excerpt']}\n")
    if r['api_md']: parts.append(r['api_md']+"\n")
    if r['body_md']: parts.append(r['body_md']+"\n")
    if r['imgs']:
        parts.append("\n## Images\n")
        for i in r['imgs']: parts.append(f"- {i}")
    open(f"{outdir}/{r['slug']}.md","w",encoding='utf-8').write("\n".join(parts))

json.dump([{k:v for k,v in r.items() if k!='body_md'} for r in records],
          open('raw/records_meta.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(sorted(IMG), open('raw/images.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print("pages by section:", dict(counts))
print("total records:", len(records), "| images:", len(IMG), "| openapi files:", len(os.listdir('data/openapi')) if os.path.exists('data/openapi') else 0)
