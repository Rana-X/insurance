import markdown, re, weasyprint
md=open('/home/user/insurance/takehome/rationale_v3.md').read()
# drop top title block lines (we render our own title)
md=re.sub(r'^# Decision Rationale\s*\n','',md)
md=re.sub(r'^\*\*Corgi Cyber Protection Policy[^\n]*\n','',md,flags=re.M)
md=re.sub(r'^---\s*$','',md,flags=re.M)
lines=md.split('\n'); out=[]
for l in lines:
    if l.startswith(('- ','1. ','2. ','3. ')) and out and out[-1].strip() and not out[-1].startswith(('- ','1. ','2. ','3. ','4. ','5. ','6. ','7. ','8. ','9. ','10. ','11. ','12. ')): out.append('')
    out.append(l)
md='\n'.join(out)
body=markdown.markdown(md,extensions=['tables'])
def cite(m):
    inner=m.group(1)
    parts=re.split(r';\s*',inner)
    out=[]
    for p in parts:
        n=re.match(r'(\d+)',p).group(1)
        out.append(f'<a class="cite" href="#ref-{n}">{p}</a>')
    return '['+'; '.join(out)+']'
ri=body.find('<h2>References</h2>')
head,tail=body[:ri],body[ri:]
head=re.sub(r'\[(\d[^\]]*)\]',cite,head)
k=[0]
def lid(m):
    k[0]+=1; return f'<li id="ref-{k[0]}">'
tail=re.sub(r'<li>',lid,tail)
body=head+tail
css=open('policy.css').read()
css=css.replace('content:"Page " counter(page) " of " counter(pages)','content:counter(page) " of " counter(pages)')
css+='''
a.cite{color:#b84200;text-decoration:none}

.cover-art{string-set:formno "Decision rationale | Cedar Ridge Accounting Group | September 2026"}
h2{font-weight:600;font-size:15pt;margin:18pt 0 8pt;break-after:avoid}
h2:first-of-type{margin-top:0}
ul,ol{margin:0 0 8pt;padding-left:16pt}
li{margin:0 0 4pt}
table{font-size:8.9pt;margin:4pt 0 12pt;break-inside:auto}
td,th{padding:4pt 6pt}
blockquote{margin:0 0 8pt;padding:6pt 10pt;background:#fff7f1;border-left:1pt solid #ff5c00}
.meta{color:#5b5b5b;font-size:9.6pt;margin:-6pt 0 16pt}
@page{@bottom-left{width:60%}@bottom-center{width:15%}@bottom-right{width:25%}}
'''
doc=f'''<!doctype html><html><head><meta charset="utf-8"><title>Corgi | Decision Rationale</title><style>{css}</style></head><body>
<div class="runhead"><div class="logo">corgi</div><div class="rh">DECISION RATIONALE</div></div>
<div class="cover-art" style="height:0;margin:0"></div>
<h1 style="margin-top:0">Decision Rationale</h1>
<p class="meta">Corgi Cyber Protection Policy (CORG-CY-0200) · Sample insured: Cedar Ridge Accounting Group, LLC · September 2026</p>
{body}</body></html>'''
open('rationale.html','w').write(doc)
weasyprint.HTML(string=doc,base_url='.').write_pdf('rationale_v3.pdf')
