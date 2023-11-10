L=[13,12,12,13,18,15,18,19]
NList=[]
for Num in L:
    if Num not in NList:
        NList.append(Num)
print(NList)