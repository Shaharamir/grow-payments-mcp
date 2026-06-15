import json, re, os

recs=json.load(open('raw/records_meta.json',encoding='utf-8'))
DATA='data'
def mdrel(r):  # relative to data/ root
    return f"pages/{r['section']}/{r['slug']}.md"

def finalize_index_pages(recs):
    """The site's home + changelog landing pages have no body in ssr-props;
    synthesise useful index content for them so the corpus has no dead pages."""
    cl=[r for r in recs if r['section']=='changelog' and r['slug']!='changelog']
    lines=["---",'title: "Changelog"',"slug: changelog","type: changelog","section: changelog",
           "source_url: https://grow-il.readme.io/changelog","---","","# Changelog","",
           "Release notes and product updates for Grow Payments. Entries:",""]
    for c in sorted(cl,key=lambda x:x['title'].lower()):
        desc=(c.get('excerpt') or '').strip().replace('\n',' ')
        lines.append(f"- [{c['title']}]({c['slug']}.md)"+(f" — {desc}" if desc else ""))
        lines.append(f"  - source: {c['url']}")
    os.makedirs(f"{DATA}/pages/changelog",exist_ok=True)
    open(f"{DATA}/pages/changelog/changelog.md","w",encoding='utf-8').write("\n".join(lines)+"\n")

    home=["---",'title: "Grow Payments"',"slug: _home","type: home","section: home",
          "source_url: https://grow-il.readme.io/","---","","# Grow Payments — Documentation Center","",
          "Grow Payments (grow-il / Meshulam) is an Israeli payment service provider (PSP). This documentation",
          "center covers integrating Grow's payment products: hosted payment pages, the Light Server REST API,",
          "webhooks, SDKs, 3DS, NFC and POS devices.","",
          "## Main sections","",
          "- **Guides** — product overviews & integration guides (payment pages, Light API, app, WordPress/Make, NFC, POS, 3DS).",
          "- **API Reference** — the Light Server REST API: regular & token payments, payment links, refunds, direct debit, transaction/payment-process info, plus authentication, errors and IP allow-list.",
          "- **Changelog** — release notes.","",
          "## Key integration facts","",
          "- Server endpoints: `/api/light/server/1.0/...`; Android/POS: `/api/light/andriod/1.0/...`.",
          "- Sandbox host: `https://sandbox.meshulam.co.il` (alias `https://sandboxapi.grow.link`). Production hosts issued by Grow support.",
          "- Auth per business via `userId` + `pageCode` (and/or API key); the values in docs are examples only.",
          "- Requests are server-to-server, usually `multipart/form-data`; client-side calls are blocked.",
          "","See `../../llms.txt` for the full page index.",""]
    os.makedirs(f"{DATA}/pages/home",exist_ok=True)
    open(f"{DATA}/pages/home/_home.md","w",encoding='utf-8').write("\n".join(home)+"\n")

finalize_index_pages(recs)

pages=[]
for r in recs:
    rel=mdrel(r); full=f"{DATA}/{rel}"
    if not os.path.exists(full): continue
    raw=open(full,encoding='utf-8').read()
    body=re.sub(r'^---.*?---\s*','',raw,count=1,flags=re.S)
    pages.append({**r,'rel':rel,'full':full,'md':raw,'body':body})

def first_desc(p):
    if p.get('excerpt'): return p['excerpt'].strip().replace('\n',' ')
    for line in p['body'].splitlines():
        l=line.strip()
        if not l or l[0] in '#>|*-' or l.startswith('**') or l.startswith('<'): continue
        l=re.sub(r'[`*_]','',l)
        if len(l)>15: return (l[:160]+'…') if len(l)>160 else l
    return ''

def group_of(p):
    if p['section']=='home': return ('Overview',-1)
    if p['section']=='docs': return ('Guides',0)
    if p['section']=='changelog': return ('Changelog',9)
    if p['section']=='discuss': return (None,99)
    if p['type']=='endpoint': return ('API Endpoints',5)
    return ('API Reference — Concepts',4)

groups={}
for p in pages:
    g,o=group_of(p)
    if g is None: continue
    groups.setdefault(g,{'order':o,'items':[]})['items'] if False else None
    groups.setdefault(g,{'order':o,'items':[]})
    groups[g]['items'].append(p)

SITE="https://grow-il.readme.io"
out=["# Grow Payments — Developer Documentation",""]
out.append("> Grow Payments (grow-il / Meshulam) is an Israeli payment service provider. "
           "Full developer documentation: integration guides, the Light Server REST API "
           "(regular & token payments, payment links, refunds, direct debit, transaction & payment-process info), "
           "webhooks, server-to-server callbacks, SDKs (Apple/Bit), 3DS, NFC and POS. "
           "Sandbox API host: https://sandbox.meshulam.co.il (production hosts issued by Grow support). "
           "Auth is via per-business identifiers (userId + pageCode / API key). Content is mixed English and Hebrew.")
out.append("")
out.append(f"Source: {SITE} • Each link is a bundled Markdown file (path relative to this file); the live URL follows on the next line.")
out.append("")
for g in sorted(groups,key=lambda x:groups[x]['order']):
    out.append(f"## {g}\n")
    for p in sorted(groups[g]['items'],key=lambda p:p['title'].lower()):
        d=first_desc(p)
        out.append(f"- [{p['title']}]({p['rel']})"+(f": {d}" if d else ""))
        out.append(f"  - source: {p['url']}")
    out.append("")
open(f'{DATA}/llms.txt','w',encoding='utf-8').write("\n".join(out))

# llms-full.txt
def sec_rank(p):
    base={'home':0,'docs':1,'reference':2,'changelog':3,'discuss':4}.get(p['section'],5)
    sub=0 if p['type']!='endpoint' else 1
    return (base,sub,p['title'].lower())
full=["# Grow Payments — Full Documentation (llms-full.txt)","",
      f"All pages scraped from {SITE}. Generated for LLM consumption.","",("="*80),""]
for p in sorted(pages,key=sec_rank):
    if p['section']=='discuss': continue
    full.append(p['md'].strip()); full.append("\n"+("="*80)+"\n")
open(f'{DATA}/llms-full.txt','w',encoding='utf-8').write("\n".join(full))

# index.json for MCP
idx=[]
for p in pages:
    g,_=group_of(p)
    idx.append(dict(slug=p['slug'],title=p['title'],section=p['section'],type=p['type'],
                    group=g,url=p['url'],path=p['rel'],description=first_desc(p),
                    is_endpoint=(p['type']=='endpoint'),
                    method=p.get('api_method'),api_path=p.get('api_path'),
                    openapi=(f"openapi/{p['slug']}.json" if os.path.exists(f"{DATA}/openapi/{p['slug']}.json") else None)))
json.dump(idx, open(f'{DATA}/index.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print("OK groups:", {g:len(groups[g]['items']) for g in groups})
print("llms-full bytes:", os.path.getsize(f'{DATA}/llms-full.txt'), "| index entries:", len(idx))
