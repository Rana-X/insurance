import pymupdf, json
SRC='/root/.claude/uploads/1cd6f270-6ea2-5cc1-a978-a508b01519e4/178e78f7-01_Corgi_Cyber_Protection_Policy.pdf'
d=pymupdf.open(SRC)
ORANGE=(1.0,0.361,0.0); PALE=(1.0,0.969,0.945)
def near(a,b,t=0.01): return a and b and all(abs(x-y)<t for x,y in zip(a,b))
items=[]
anchors={}   # (page, y) -> anchor id for link targets
def span_runs(spans, links):
    runs=[]
    for s in spans:
        t=s['text']
        if not t: continue
        bold='SmBld' in s['font']
        r=pymupdf.Rect(s['bbox']); c=((r.x0+r.x1)/2,(r.y0+r.y1)/2)
        tgt=None
        for L in links:
            if L['from'].contains(pymupdf.Point(*c)) and L['kind']==1:
                tgt=(L['page'],round(L['to'].y,1))
        orange=s['color']==0xb84200
        runs.append(dict(t=t,b=bold,l=tgt,o=orange,size=round(s['size'],1)))
    return runs
def merge(runs):
    out=[]
    for r in runs:
        if out and all(out[-1][k]==r[k] for k in ('b','l','o')): out[-1]['t']+=r['t']
        else: out.append(dict(r))
    return out
def lines_to_runs(lines,links):
    runs=[]
    for i,l in enumerate(lines):
        rs=span_runs(l['spans'],links)
        if not rs: continue
        if runs:
            prev=runs[-1]['t']
            if not prev.endswith('-') and not prev.endswith(' '): runs[-1]['t']+=' '
        runs+=rs
    return merge(runs)
for pn,p in enumerate(d):
    links=p.get_links()
    drs=p.get_drawings()
    # tables: orange top rule full width
    tops=[dr['rect'] for dr in drs if near(dr.get('color'),ORANGE) and dr['rect'].width>400 and dr['rect'].height<1.5]
    greys=sorted(set(round(dr['rect'].y0,1) for dr in drs if dr.get('color') and abs(dr['color'][0]-0.847)<0.01 and dr['rect'].width>400 and 70<dr['rect'].y0<740))
    vlines=[dr['rect'] for dr in drs if near(dr.get('color'),ORANGE) and dr['rect'].width<1.5 and dr['rect'].height>5]
    callouts=[dr['rect'] for dr in drs if near(dr.get('fill'),PALE) and any(abs(v.x0-dr['rect'].x0)<2 and abs(v.y0-dr['rect'].y0)<2 for v in vlines)]
    tables=[]
    for t in tops:
        ys=[t.y0]; 
        for g in greys:
            if g>ys[-1] and g-ys[-1]<120: ys.append(g)
            elif g>ys[-1]: break
        tables.append(ys)
    blocks=[b for b in p.get_text('dict')['blocks'] if b['type']==0]
    img=[b for b in p.get_text('dict')['blocks'] if b['type']==1]
    if pn==0: items.append(dict(k='img',page=pn,y=100))
    body=[]
    for b in blocks:
        y0=b['bbox'][1]
        if y0<66 or y0>740: continue
        body.append(b)
    used=set()
    events=[]
    for ys in tables:
        # collect lines (not blocks) per row; stop when a row holds body-size text
        allines=[]
        for bi,b in enumerate(body):
            for l in b['lines']:
                if l['spans'] and ''.join(s['text'] for s in l['spans']).strip(): allines.append((bi,l))
        rows=[];rowlines=[]
        for a,z in zip(ys,ys[1:]):
            ls=[(bi,l) for bi,l in allines if a<(l['bbox'][1]+l['bbox'][3])/2<z]
            if any(round(l['spans'][0]['size'],1)>=10.0 for bi,l in ls): break
            rowlines.append(ls)
        if not rowlines: continue
        hdr=rowlines[0]
        colx=sorted(set(round(s['bbox'][0]) for bi,l in hdr for s in l['spans'] if s['text'].strip()))
        cl=[]
        for x in colx:
            if cl and x-cl[-1]<40: continue
            cl.append(x)
        # a header label made of several spans on same line: keep only span starts that begin after a gap
        R=[]
        for ls in rowlines:
            cells=[[] for _ in cl]
            for bi,l in ls:
                used.add(bi)
                for sp in l['spans']:
                    if not sp['text']: continue
                    ci=max([i for i,c in enumerate(cl) if c<=sp['bbox'][0]+4] or [0])
                    cells[ci].append((round(l['bbox'][1],1),sp))
            cellruns=[]
            for c in cells:
                lines_={}
                for y,sp in c: lines_.setdefault(y,[]).append(sp)
                fake=[dict(spans=v) for k,v in sorted(lines_.items())]
                cellruns.append(lines_to_runs(fake,links))
            R.append(cellruns)
        events.append((ys[0],dict(k='table',page=pn,y=ys[0],rows=R,colx=cl)))
    for c in callouts:
        paras=[]
        for bi,b in enumerate(body):
            if bi in used: continue
            cy=(b['bbox'][1]+b['bbox'][3])/2
            if c.y0<cy<c.y1:
                used.add(bi); paras.append(lines_to_runs(b['lines'],links))
        events.append((c.y0,dict(k='callout',page=pn,y=c.y0,paras=paras)))
    def kindof(l):
        s0=l['spans'][0]; size=round(s0['size'],1); bold='SmBld' in s0['font']
        if size>=30: return 'title'
        if size>=19: return 'h1'
        if size==11.0 and bold: return 'h2'
        if size==10.8 and bold: return 'h3'
        if size==10.6 and bold: return 'h4'
        return 'p'
    for bi,b in enumerate(body):
        if bi in used: continue
        groups=[]
        for l in b['lines']:
            if not l['spans'] or not ''.join(s['text'] for s in l['spans']).strip(): continue
            k=kindof(l)
            if groups and groups[-1][0]==k and k=='p': groups[-1][1].append(l)
            elif groups and groups[-1][0]==k and k!='p' and abs(l['bbox'][1]-groups[-1][1][-1]['bbox'][3])<4: groups[-1][1].append(l)
            else: groups.append([k,[l]])
        for k,ls in groups:
            x0=round(ls[0]['bbox'][0]); x1=round(ls[1]['bbox'][0]) if len(ls)>1 else x0
            events.append((ls[0]['bbox'][1],dict(k=k,page=pn,y=round(ls[0]['bbox'][1],1),y_last=round(ls[-1]['bbox'][1],1),x0=x0,x1=x1,runs=lines_to_runs(ls,links))))
    events.sort(key=lambda e:e[0])
    items+= [e[1] for e in events]
# merge paragraphs split across a page break
merged=[]
for i in items:
    if merged and i['k']=='p' and merged[-1]['k']=='p' and i['page']==merged[-1]['page']+1:
        prev=merged[-1]; t0=''.join(r['t'] for r in i['runs']).lstrip()
        # first item on its page and starts lowercase / continuation
        firsts=[j for j in items if j['page']==i['page']]
        if firsts and firsts[0] is i and t0 and (t0[0].islower() or t0[0] in '($'):
            if not prev['runs'][-1]['t'].endswith(' '): prev['runs'][-1]['t']+=' '
            prev['runs']+=i['runs']; continue
    if merged and i['k']=='p' and merged[-1]['k']=='p' and i['page']==merged[-1]['page']:
        prev=merged[-1]; t0=''.join(r['t'] for r in i['runs']).lstrip()
        if t0 and t0[0].islower() and not t0[:3].rstrip().endswith('.') and 0<i['y']-prev['y_last']<=15.5 and i['x0']>=prev['x0'] and not (len(t0)>2 and t0[1]=='.'):
            if not prev['runs'][-1]['t'].endswith(' '): prev['runs'][-1]['t']+=' '
            prev['runs']+=i['runs']; prev['y_last']=i['y_last']; continue
    merged.append(i)
items=merged
json.dump(items,open('items.json','w'),indent=0)
import collections
print(collections.Counter(i['k'] for i in items))
print(collections.Counter((i['x0'],i['x1']) for i in items if i['k']=='p').most_common(20))
