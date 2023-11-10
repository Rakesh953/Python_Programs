s='ENGINEERING'
newS=''
HF=0
for ch in s:
    if s.count(ch)>HF:
        HF=s.count(ch)
    if ch not in newS:
        newS+=ch
for ch in newS:
    if s.count(ch)==HF:
        print(ch)
        
        #or
        
s = 'ENGINEERING'
newS = ''
HF = 0
MFC= []
for ch in s:
    if s.count(ch) > HF:
        HF = s.count(ch)
        MFC = [ch]
    elif s.count(ch) == HF and ch not in MFC:
        MFC.append(ch)
print(MFC)

