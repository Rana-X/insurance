import json,re,importlib.util
spec=importlib.util.spec_from_file_location('ae','apply_edits.py')
# reuse helpers without re-running: copy minimal helpers
items=json.load(open('items_edited.json'))
src=open('apply_edits.py').read()
ns=dict(ITEMS=json.load(open('items.json')),json=json,re=re,sys=__import__('sys'))
exec(src.split('done=[];fail=[]')[0].replace("items=json.load(open('items.json'))","items=ITEMS"),ns)
markup,replace_in,ctext=ns['markup'],ns['replace_in'],ns['ctext']
log=[]
def paras():
    for n,i in enumerate(items):
        if 'runs' in i: yield n,i,i['runs']
        for r in i.get('rows',[]):
            for c in r: yield n,i,c
        for p in i.get('paras',[]): yield n,i,p
def sub(old,new,count=1,where=None):
    c=0
    for n,i,rs in paras():
        t=ctext(rs); k=t.find(old)
        while k>=0 and c<count:
            rs[:]=replace_in(rs,k,k+len(old),markup(new) if new else [])
            c+=1; t=ctext(rs); k=t.find(old,k+len(new))
        if c>=count: break
    log.append((old[:40],c))
def settext_prefix(prefix,newprefix):
    for n,i,rs in paras():
        t=ctext(rs)
        if t.startswith(prefix):
            rs[:]=replace_in(rs,0,len(prefix),[dict(t=newprefix,b=False,l=None,o=False)]); log.append((prefix,1)); return i
    log.append((prefix,0))
def bold_range(rs,start,end):
    out=[];pos=0
    for r in rs:
        a,b=pos,pos+len(r['t']); pos=b
        if b<=start or a>=end or r['b']: out.append(r); continue
        if a<start: out.append(dict(r,t=r['t'][:start-a]))
        s,e=max(a,start),min(b,end); out.append(dict(r,t=r['t'][s-a:e-a],b=True))
        if b>end: out.append(dict(r,t=r['t'][end-a:]))
    rs[:]=out
# A-22 / G-9
for i in items:
    if i['k']=='h2' and ctext(i['runs']).strip()=='IMPORTANT NOTICES': i['runs']=[dict(t='Important notices',b=False,l=None,o=True)]
settext_prefix('7. Terrorism Risk Insurance Act disclosure','1. Terrorism Risk Insurance Act disclosure')
settext_prefix('8. Fraud warning (Colorado).','2. Fraud warning (Colorado).')
sub('(Legal notices, item 7)','(Legal notices, item 1)')
# A-16
for i in items:
    if i['k']=='h1':
        t=ctext(i['runs']).strip()
        m={'I. Insuring Agreements':'I. Insuring agreements','II. Limits of Insurance':'II. Limits of insurance','IV. Defense & Settlement of Claims':'IV. Defense and settlement of claims'}
        if t in m: i['runs']=[dict(t=m[t],b=False,l=None,o=False)]
# B-9 renumber III.1
for a,b in [('1. One dollar retention','1.1. One dollar retention'),('2. Business interruption','1.2. Business interruption'),('3. Claim expenses count','1.3. Claim expenses count'),('4. If you earn the reduced','1.4. If you earn the reduced')]:
    settext_prefix(a,b)
# A-18 exclusion 15
for a,b in [('1. What is excluded','15.1. What is excluded'),('2. Bystanders stay covered','15.2. Bystanders stay covered'),('3. Cyber terrorism','15.3. Cyber terrorism'),('4. Identifying who','15.4. Identifying who'),('5. Help continues','15.5. Help continues')]:
    settext_prefix(a,b)
sub('Part (b) does not apply','Part 15.1(b) does not apply')
sub('unless (a) or (b) applies','unless 15.1(a) or (b) applies')
# B-19 def 16(d)
sub('except: (a) amounts you would have owed anyway; (b) amounts','except: (i) amounts you would have owed anyway; (ii) amounts')
sub('; and (c) PCI fines','; and (iii) PCI fines')
# A-4 waiting periods -> Item 6
for ctx in ['longer than the waiting period in Item 7','own waiting period in Item 7','After the waiting period in Item 7','reputational harm waiting period in Item 7']:
    for n,i,rs in paras():
        t=ctext(rs); k=t.find(ctx)
        if k>=0:
            j=k+ctx.index('Item 7'); rs[:]=replace_in(rs,j,j+6,markup('Item 6')); log.append((ctx,1))
sub('hours shown in Item 7 that','time shown in Item 6 that')
# A-12 verbs
for n,i,rs in paras():
    for r_i,r in enumerate(rs):
        nxt=rs[r_i+1]['t'] if r_i+1<len(rs) else ''
        prv=rs[r_i-1]['t'] if r_i>0 else ''
        if r['b'] and r['t'].strip()=='damages' and nxt.startswith(', corrupts'): r['b']=False;r['l']=None
        if r['b'] and r['t'].strip()=='claim' and prv.endswith('falsely '): r['b']=False;r['l']=None
# A-21 statutory notices
for n,i,rs in paras():
    t=ctext(rs)
    if any(s in t for s in ['Terrorism Risk Insurance Act disclosure','certified acts of terrorism','Fraud warning (Colorado)','combined insured losses','reimbursement to the insurer']):
        for r in rs:
            if r['b'] and not r.get('o'): r['b']=False; r['l']=None
# A-13 TRIA row
sub('Taxes, surcharges and fees (assumed)','Terrorism (TRIA), taxes and fees (assumed)')
# A-25 stray text
sub('$250,000 selected. / Item 6','$250,000 / Item 6')
sub("Item 7 sets H's limit.","The table above sets H's limit.")
# A-30
sub("or a dependent provider's systems","or dependent systems")
sub("In Coverages A-H and M-P, \"you\" and \"your\" mean the named insured and its subsidiaries","In Coverages A-H and M-P, \"you\" and \"your\" mean the named insured and the companies in paragraph a")
# A-32
for n,i,rs in paras():
    t=ctext(rs).strip()
    if t in ('Special conditions. Chargebacks and ordinary processing fees are not covered.','Special conditions. Biometric information is not covered.'):
        rs[:]=rs+markup(' Section IV.'); log.append(('A-32',1))
# indents: B-8, B-17
sec=None
for n,i in enumerate(items):
    if i['k']=='h1': sec=ctext(i['runs']).strip()
    if i['k']!='p' or not sec: continue
    t=ctext(i['runs']).strip()
    if sec.startswith(('II.','III.','IV.','V.','VI.','VII.')):
        if re.match(r'^\d+(\.\d+)*\.\s',t):
            if i['x0']==54 and i['x1']==54 and sec.startswith('II.'): i['x0'],i['x1']=72,90
        elif re.match(r'^[a-z]\.\s',t):
            if i['x0']==54 or i['x1']!=90: i['x0'],i['x1']=72,90
        else:
            if sec.startswith('V.') and i['x0'] in (54,90): i['x0']=i['x1']=72
            elif sec.startswith(('II.','VI.','VII.')) and i['x0']==54 and i['x1']==54 and n>0: pass
# II part 4 follow-ons
for n,i in enumerate(items):
    if i['k']=='p' and ctext(i['runs']).startswith('4. Costs that fit'):
        i['x0'],i['x1']=72,90
        for j in items[n+1:n+4]:
            if j['k']=='p' and not re.match(r'^\d',ctext(j['runs'])): j['x0']=j['x1']=90
# A-20 run-in headings bold
sec=None
STOP=('We ','You ','If ','The ','Our ','Any ','This ','Every ','Tell ','Send ','Take ','A ','An ','After ','Use ','Coverage ','Do ','First ')
for n,i in enumerate(items):
    if i['k']=='h1': sec=ctext(i['runs']).strip()
    if i['k']!='p' or not sec or not sec.startswith(('II.','III.','IV.','VI.','VII.','Reporting','Legal')): continue
    t=ctext(i['runs'])
    m=re.match(r'^(\d+(?:\.\d+)*\.\s+)([^.]{2,80}?\.)(\s|$)',t)
    if not m: continue
    title=m.group(2)
    if len(title.split())>9 or title.startswith(STOP): continue
    bold_range(i['runs'],0,m.end(2))
for i in items:
    if i['k']=='h1' and ctext(i['runs']).strip()=='IV. Defense and Settlement': i['runs']=[dict(t='IV. Defense and settlement',b=False,l=None,o=False)]
    if i['k']=='p' and ctext(i['runs']).startswith('Bold terms'): i['x0']=i['x1']=54
for n,i,rs in paras():
    for k,r in enumerate(rs):
        nxt=rs[k+1]['t'] if k+1<len(rs) else ''
        if r['b'] and r['t'].strip()=='System Failure' and nxt.startswith(' Full Limit'): r['b']=False; r['l']=None
# Codex fixes
sub('before the change. You may buy an extended reporting period.','before the change. You may buy an extended reporting period under part 5.5.')
sub('5.5. Optional extended reporting. If either of us cancels or does not renew, you may buy','5.5. Optional extended reporting. If either of us cancels or does not renew, or the named insured is acquired as part 4.2 describes, you may buy')
sub('Tell us and pay within 60 days after the policy ends. It starts when the policy ends and includes the automatic 60 days.','Tell us and pay within 60 days after the policy ends, including when it ends after an acquisition. It starts when the policy ends and includes any automatic 60 days.')
sub('and a member of our incident response team will contact you within one hour of your report.','and we aim to have a member of our incident response team contact you within one hour of your report.')
sub('Assumes one covered claim and no earlier payments.','Assumes one fully covered claim, no earlier payments, and that no smaller coverage limit or settlement-sharing rule applies.')
json.dump(items,open('items_final.json','w'))
for l in log:
    if l[1]==0: print('MISS',l)
print('done',len(log))
