L=[2,4,6,9,0,3,0,2,6,0,2,0]
# Output - [2, 4, 6, 9, 3, 2, 6, 2, 0, 0, 0, 0]
n1=[num for num in L if num!=0]
n2=[num for num in L if num==0]
print(n1+n2)

#       or
L=[2,4,6,9,0,3,0,2,6,0,2,0]
newl=[num for num in L if num!=0]+[0],L.count[0]
print(newl)


L = [2, 4, 6, 9, 0, 3, 0, 2, 6, 0, 2, 0]

# Count the number of zeros in the original list L
num_zeros = L.count(0)

# Create a new list without the zeros, and then append the appropriate number of zeros at the end
newl = [num for num in L if num != 0] + [0] * num_zeros

print(newl)
