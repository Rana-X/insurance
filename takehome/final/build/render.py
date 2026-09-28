import json, html, re, sys
items=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'items.json'))
# anchors for link targets
targets=set()
def walk_runs(i):
    if 'runs' in i: yield i['runs']
    for r in i.get('rows',[]):
        for c in r: yield c
    for p in i.get('paras',[]): yield p
for i in items:
    for rs in walk_runs(i):
        for r in rs:
            if r.get('l'): targets.add(tuple(r['l']))
anchor_of={}
bypage={}
for n,i in enumerate(items):
    if 'page' in i: bypage.setdefault(i['page'],[]).append((i['y'],n))
for (pg,y) in targets:
    cands=sorted(bypage.get(pg,[]))
    best=None
    for iy,n in cands:
        if iy>=y-6: best=n; break
    if best is None and cands: best=cands[-1][1]
    if best is not None: anchor_of[(pg,y)]=f"t{best}"
ids={v for v in anchor_of.values()}
def runs_html(rs):
    out=[]
    for r in rs:
        t=html.escape(r['t'])
        if r['b']: t=f"<b>{t}</b>"
        if r.get('l'):
            a=anchor_of.get(tuple(r['l']))
            cls='' if r['b'] and not r.get('o') else ' class="x"'
            if a: t=f'<a href="#{a}"{cls}>{t}</a>'
        elif r.get('o'): t=f'<span class="x">{t}</span>'
        out.append(t)
    return ''.join(out).strip()
def pstyle(i):
    x0,x1=i.get('x0',54),i.get('x1',i.get('x0',54))
    ml=x1-54; ti=x0-x1
    return f' style="margin-left:{ml}pt;text-indent:{ti}pt"' if (ml or ti) else ''
body=[]
prev_page=-1
for n,i in enumerate(items):
    k=i['k']; idattr=f' id="t{n}"' if f"t{n}" in ids else ''
    newpage = i.get('page',0)!=prev_page
    brk=''
    if newpage and k in ('h1','h2') and n>0:
        # forced break if previous page ended early
        prev=[j for j in items[:n] if j.get('page')==prev_page]
        if k=='h1' or (prev and prev[-1]['y']<560): brk=' class="pb"' if k!='h2' else ' pb'
    prev_page=i.get('page',prev_page)
    if k=='img':
        body.append('<div class="cover-art"><img src="dog.png"></div>'); continue
    if k=='title':
        body.append(f'<h1 class="title"{idattr}>Cyber Protection Policy</h1>'); continue
    if k=='h1':
        if i['runs'] and ''.join(r['t'] for r in i['runs']).strip()=='Contents':
            body.append('<h1 class="pb" id="contents">Contents</h1><!--TOC-->'); continue
        body.append(f'<h1{brk}{idattr}>{html.escape("".join(r["t"] for r in i["runs"]).strip())}</h1>'); continue
    if k in('h2','h3','h4'):
        cls=[k]
        if all(r.get('o') for r in i['runs']): cls=['h2','lc']
        if brk: cls.append('pb')
        body.append(f'<div class="{" ".join(cls)}"{idattr}{pstyle(i) if k!="h2" else ""}>{html.escape("".join(r["t"] for r in i["runs"]).strip())}</div>'); continue
    if k=='p':
        if i['page']==1: continue  # old contents rows
        body.append(f'<p{idattr}{pstyle(i)}>{runs_html(i["runs"])}</p>'); continue
    if k=='callout':
        body.append(f'<div class="callout"{idattr}>'+''.join(f'<p>{runs_html(p)}</p>' for p in i['paras'])+'</div>'); continue
    if k=='table':
        rows=i['rows']; ncol=max(len(r) for r in rows)
        cx=i['colx']+[558]; W=558-cx[0]+7
        h=['<table'+idattr+'><colgroup>'+''.join(f'<col style="width:{(cx[j+1]-cx[j])/W*100:.1f}%">' for j in range(len(i['colx'])))+'</colgroup>']
        for ri,r in enumerate(rows):
            tag='th' if ri==0 else 'td'
            h.append('<tr>'+''.join(f'<{tag}>{runs_html(c)}</{tag}>' for c in r)+'</tr>')
        h.append('</table>'); body.append(''.join(h)); continue
toc_entries=[]
# keep each coverage block (h3 .. next heading) together
out=[];open_=False
for el in body:
    is_h3=el.startswith('<div class="h3')
    is_break=el.startswith(('<div class="h2','<h1','<div class="h4'))
    if open_ and (is_h3 or is_break): out.append('</div>'); open_=False
    if is_h3: out.append('<div class="blk">'); open_=True
    out.append(el)
if open_: out.append('</div>')
body=out
html_body='\n'.join(body)
open('body.html','w').write(html_body)
print(len(body),'elements',len(ids),'anchors')
