L=[13,12,12,13,18,15,18,19]
newL=[]
for num in L:
    if num not in newL:
        newL.append(num)
print(newL)