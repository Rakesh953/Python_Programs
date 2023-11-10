# Print Unique value in given List 
L=[12,14,12,13,14,10,12,14,18]  #Output - 13 10 18
newL=[]
for num in L:
    if num not in newL:
        newL.append(num)
print(newL)
for num1 in newL:
    if L.count(num1)==1:
        print(num1)