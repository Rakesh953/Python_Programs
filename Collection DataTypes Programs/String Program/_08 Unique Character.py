s='AVENGER'
newS=''
for ch in s:
    if ch not in newS:
        newS+=ch
for ch in newS:
    if s.count(ch)==1:
        print(ch)
