s='abcd'
newL=[ch*2 for ch in s]
print(newL)

s='abcd'
newL=[ch for ch in s if ord(ch)%2==0]
print(newL)

L=['*'*st for st in range(1,6)]
print('\n'.join(L))

#Print Even Number from given List 
l=[2,3,4,5,6,7,8,9]
newL=[num for num in l if num%2==0]
print(newL)

# Print Odd Number from given List 
l=[2,3,4,5,6,7,8,9]
newL=[num for num in l if num%2!=0]
print(newL)



