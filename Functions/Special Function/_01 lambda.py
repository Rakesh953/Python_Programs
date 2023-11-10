# Example
add=lambda a,b:a+b
print(add(1,90))

# Multiply number 
mul=lambda n1,n2:n1*n2
print(mul(9,8))


# Prime Number
prime=lambda num:len([val for val in range(1,num+1)if num%val==0])==2
print(prime(7))


# Composite Number
compo = lambda num:len([val for val in range(1,num+1) if num%val==0])>2
print(compo(6))

# Perfect Number
