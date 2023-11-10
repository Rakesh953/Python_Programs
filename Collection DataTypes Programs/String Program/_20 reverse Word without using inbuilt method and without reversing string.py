# _20 reverse Word without using inbuilt method and without reversing string
s='This is Python Class'
word=''
res=''
for ch in s:
    print(ch)
    if ch == ' ':
        res=res+word+' '
        word=' '
    else:
        word=ch+word
print(res+word)
