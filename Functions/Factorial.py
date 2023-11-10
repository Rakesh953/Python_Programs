def Factorial(num,F=1):
    for val in range(1,num+1):
        F=F*val
    return F
print(Factorial(4))