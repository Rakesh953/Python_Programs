s='ENGINEERING'
news=''
for ch in s:
    if ch not in news:
        news+=ch
for ch in news:
    print(f'{ch}={s.count(ch)}')
    
s='ENGINEERING'
while s!='':
    print(f'{s[0]}={s.count(s[0])}')
    s=s.replace(s[0],'')