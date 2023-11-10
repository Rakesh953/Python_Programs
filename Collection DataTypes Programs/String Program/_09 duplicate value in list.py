# Print duplicate value in given list
L=[12,14,12,13,14,10,12,14,18]
newL=[]
for num in L:
    if num not in newL:
        newL.append(num)
for num in newL:
    if L.count(num)>1:
        print(num)