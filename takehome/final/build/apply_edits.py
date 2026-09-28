import json, re, sys
items=json.load(open('items.json'))
md=open('/home/user/insurance/takehome/POLICY_CHANGE_LIST.md').read()
def section(a,b): return md[md.index(a):md.index(b)]
part2=section('## Part 2','## Part 3')
part1=section('## Part 1','## Part 2')
def blocks(txt):
    for m in re.finditer(r'^### ([A-Z]-\d+)(.*?)(?=^### |^## |^#### |\Z)',txt,re.S|re.M):
        yield m.group(1),m.group(2)
def q(body,label):
    m=re.search(r'\*\*'+label+r'[^*]*:\*\*\s*"(.*?)"\s*(?:\n|$)',body,re.S)
    return m.group(1) if m else None
edits=[]
for id_,b in blocks(part2):
    if id_=='G-9': continue
    new=q(b,'Replace with') or q(b,'Fix')
    if re.search(r'Replace with:\*\*\s*""\s*\(delete\)',b): new=''
    edits.append((id_,q(b,'Current'),new,b))
A3NEW="It does not matter whether you delivered before or after the diverted payment. It does not include a diversion carried out by, or in collusion with, anyone excluded from the definition of payment fraud."
for id_,b in blocks(part1):
    if id_ in ('A-2','A-8'): edits.append((id_,q(b,'Current'),q(b,'Fix') or q(b,'Replace with'),b))
    if id_=='A-3': edits.append((id_,"It does not matter whether you delivered before or after the diverted payment.",A3NEW,b))
# containers
conts=[]
for i in items:
    if 'runs' in i and i['k'] in ('p','h1','h2','h3','h4'): conts.append(i['runs'])
    for r in i.get('rows',[]):
        for c in r: conts.append(c)
    for p in i.get('paras',[]): conts.append(p)
# markup maps
termmap={}; xrefmap={}
for rs in conts:
    for r in rs:
        if r.get('l'):
            k=r['t'].strip()
            if r['b'] and not r.get('o'): termmap.setdefault(k.lower(),r['l'])
            elif r.get('o'): xrefmap.setdefault(k,r['l'])
terms=sorted(termmap,key=len,reverse=True)
xrefs=sorted(xrefmap,key=len,reverse=True)
xrefs=[x for x in xrefs if len(x)>=4]
pat=re.compile('|'.join([r'(?<![\w-])'+re.escape(x)+r'(?![\w])' for x in xrefs]))
tpat=re.compile('|'.join([r'(?<![\w-])'+re.escape(t)+r'(?![\w])' for t in terms]),re.I)
def markup(text):
    out=[];pos=0
    ms=sorted(list(pat.finditer(text))+[m for m in tpat.finditer(text)],key=lambda m:(m.start(),-len(m.group(0))))
    kept=[];last=-1
    for m in ms:
        if m.start()>=last: kept.append(m); last=m.end()
    for m in kept:
        s=m.group(0)
        if m.start()>pos: out.append(dict(t=text[pos:m.start()],b=False,l=None,o=False))
        if s in xrefmap: out.append(dict(t=s,b=False,l=xrefmap[s],o=True))
        elif s.lower() in termmap: out.append(dict(t=s,b=True,l=termmap[s.lower()],o=False))
        else: out.append(dict(t=s,b=False,l=None,o=False))
        pos=m.end()
    if pos<len(text): out.append(dict(t=text[pos:],b=False,l=None,o=False))
    return out
def norm(s): return ' '.join(s.split())
def ctext(rs): return ''.join(r['t'] for r in rs)
def replace_in(rs,start,end,newruns):
    out=[];pos=0
    for r in rs:
        a,b=pos,pos+len(r['t']); pos=b
        if b<=start or a>=end: out.append(r); continue
        if a<start: out.append(dict(r,t=r['t'][:start-a]))
        if a<=start<b or (start<=a and not any(x is newruns for x in out)):
            if not any(x is newruns for x in out): out.append(newruns)
        if b>end: out.append(dict(r,t=r['t'][end-a:]))
    flat=[]
    for x in out:
        if isinstance(x,list): flat+=x
        else: flat.append(x)
    return flat
done=[];fail=[]
for id_,cur,new,body in edits:
    if not cur or new is None or '[' in (new or ''): fail.append((id_,'manual')); continue
    cur=norm(cur); new=norm(new)
    hit=False
    for ci,rs in enumerate(conts):
        t=ctext(rs)
        for variant in (cur, cur.replace('- ','-')):
            k=t.find(variant)
            if k>=0:
                rs[:]=replace_in(rs,k,k+len(variant),markup(new)); hit=True; break
        if hit: break
    if not hit:
        # try across consecutive containers
        for ci in range(len(conts)-1):
            for span in (2,3,4):
                seg=conts[ci:ci+span]
                if len(seg)<span: break
                joined=' '.join(ctext(r) for r in seg)
                for variant in (cur,cur.replace('- ','-')):
                    k=joined.find(variant)
                    if k>=0 and k<len(ctext(seg[0])):
                        endk=k+len(variant)
                        first=seg[0]; ft=ctext(first)
                        # text after the match in the last container
                        offs=0; tail=None
                        for j,r in enumerate(seg):
                            L=len(ctext(r))
                            if offs<=endk<=offs+L: tail=(j,endk-offs)
                            offs+=L+1
                        j,e=tail
                        lastrest=seg[j] and replace_in(seg[j],0,e,[])
                        first[:]=replace_in(first,k,len(ft),markup(new))+([dict(t=' ',b=False,l=None,o=False)]+lastrest if j>0 and ctext(lastrest).strip() else [])
                        for r in seg[1:j+1]: r[:]=[]
                        hit=True; break
                if hit: break
            if hit: break
    (done if hit else fail).append((id_,'' if hit else 'notfound'))
json.dump(items,open('items_edited.json','w'))
print('applied',len(done)); print('failed',fail)
