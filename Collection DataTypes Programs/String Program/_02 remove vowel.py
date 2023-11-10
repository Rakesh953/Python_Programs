s='Monk is important'
newS=''
for ch in s:
    if ch not in 'aeiouAEIOU':
        newS+=ch
print(newS)