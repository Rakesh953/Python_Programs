s='Think and write the logic think'
HF=0
newL=[]
L=s.split()
for word in L:
    if len(word)>HF:
        HF=len(word)
    if word not in newL:
        newL.append(word)
for word in newL:
    if len(word)==HF:
        print(word)
        
# lengthiest word in the string