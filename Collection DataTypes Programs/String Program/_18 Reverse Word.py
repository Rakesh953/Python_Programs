# Reverse Word in String without reversing the string
s='we are in class'
L=s.split()
newl=[]
for word in L:
    rev=word[::-1]
    newl.append(rev)
print(' '.join(newl))
    