# With Slicing
s='PYTHON'
L= s[::-1]
print(L)

# Without Using Slicing
s='PYTHON'
l=len(s)
revS=''
for ind in range(-1,-l-1,-1):
    revS+=s[ind]
print(revS)