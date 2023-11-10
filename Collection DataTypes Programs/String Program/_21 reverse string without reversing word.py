# Reverse String without reversing Word

# s='This is python class'
# sp=s.split()
# L=sp[::-1]
# print(' '.join(L))


s='This is python class'
word=''
res=''
for ch in s:
    if ch==' ':
        res=' '+word+res
        word=''
    else:
        word=word+ch
print(word+res)