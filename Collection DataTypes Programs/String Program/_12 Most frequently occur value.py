L=[12,14,12,13,14,10,12,14,] # opt: 12,14
newL=[]
HF=0
for num in L:
    if L.count(num)>HF:
        HF=L.count(num)
    if num not in newL:
        newL.append(num)
for num2 in newL:
    if L.count(num2)==HF:
        print(num2)
        