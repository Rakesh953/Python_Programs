# ## To add single value pair to Dictionary

# Add by using Key
# D={}
# D[10]=120
# print(D)

# Update
# D1={10:"50",12:'ABCD'}
# D1.update({50:20,12:30})
# print(D1)

# D1={10:"50"}
# D1.update({50:20,12:30})
# print(D1)

# To Remove key value from dictionary
# Pop
DC={'a':10,'b':20,'c':30,20:'MNO'}

print(DC)
print(DC.pop('c'))
print(DC.pop('d'))# Error - Key Error
print(DC)