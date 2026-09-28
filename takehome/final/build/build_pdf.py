import re, sys, weasyprint
body=open('body.html').read()
TOC=[("How to read this policy",r'<h1[^>]*>How to read this policy'),("Declarations",r'<h1[^>]*>Declarations'),
("Reporting an incident",r'<h1[^>]*>Reporting an incident'),("Important notices",r'<div class="h2[^"]*"[^>]*>(<[^>]+>)*(IMPORTANT NOTICES|Important notices)'),
("Legal notices",r'<h1[^>]*>Legal notices'),("I. Insuring agreements",r'<h1[^>]*>I\. Insuring'),
("1. Respond to an incident: A and B",r'<div class="h2[^"]*"[^>]*>(<[^>]+>)*1\. RESPOND'),
("2. Cyber extortion and ransomware: C",r'<div class="h2[^"]*"[^>]*>(<[^>]+>)*2\. CYBER'),
("3. Recover income: D, E and optional P",r'<div class="h2[^"]*"[^>]*>(<[^>]+>)*3\. RECOVER'),
("4. Restore data and systems: F and G",r'<div class="h2[^"]*"[^>]*>(<[^>]+>)*4\. RESTORE'),
("5. Recover payments: H",r'<div class="h2[^"]*"[^>]*>(<[^>]+>)*5\. RECOVER'),
("6. Claims and investigations against you: I-L and optional Q",r'<div class="h2[^"]*"[^>]*>(<[^>]+>)*6\. CLAIMS'),
("7. Other losses: M-O",r'<div class="h2[^"]*"[^>]*>(<[^>]+>)*7\. OTHER'),
("II. Limits of insurance",r'<h1[^>]*>II\. Limits'),("III. Retention",r'<h1[^>]*>III\. Retention'),
("IV. Defense and settlement",r'<h1[^>]*>IV\. Defense'),("V. Definitions",r'<h1[^>]*>V\. Definitions'),
("VI. Exclusions",r'<h1[^>]*>VI\. Exclusions'),("VII. Conditions",r'<h1[^>]*>VII\. Conditions')]
rows=[]
for n,(label,pat) in enumerate(TOC):
    m=re.search(pat,body)
    if not m: print('TOC miss',label); continue
    tag=m.group(0)
    tid=f'toc{n}'
    idm=re.search(r' id="([^"]+)"',tag)
    if idm: tid=idm.group(1)
    else:
        first=re.match(r'<(h1|div)',tag).group(0)
        body=body[:m.start()]+first+f' id="{tid}"'+body[m.start()+len(first):]
    rows.append(f'<tr><td><a class="x" href="#{tid}">{label}</a></td><td class="pg"><a class="x" href="#{tid}"></a></td></tr>')
toc='<table class="toc"><tr><th>Section</th><th class="pg">Page</th></tr>'+''.join(rows)+'</table>'
body=body.replace('<!--TOC-->',toc)
# Declarations form number
body=re.sub(r'<h1([^>]*?) class="pb"([^>]*)>Declarations',r'<h1\1 class="pb decl"\2>Declarations',body,count=1)
body=re.sub(r'<h1([^>]*?) class="pb"([^>]*)>Reporting an incident',r'<h1\1 class="pb nondecl"\2>Reporting an incident',body,count=1)
for h in ('Core cover and your share','Core cover and optional choices','Premium, dates and policy forms','III. Retention'):
    body=re.sub(r'<h1([^>]*?) class="pb"([^>]*)>'+re.escape(h),r'<h1\1 class="cont"\2>'+h,body,count=1)
CSS=open('policy.css').read()
doc=f'''<!doctype html><html><head><meta charset="utf-8"><title>Corgi | Cyber Protection Policy</title>
<meta name="author" content="Rana"><style>{CSS}</style></head><body>
<div class="runhead"><div class="logo">corgi</div><div class="rh">CYBER PROTECTION POLICY</div></div>
{body}</body></html>'''
open('policy.html','w').write(doc)
out=sys.argv[1] if len(sys.argv)>1 else 'policy.pdf'
weasyprint.HTML(string=doc, base_url='.').write_pdf(out)
print('wrote',out)
