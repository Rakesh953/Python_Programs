binary=10110
sum=0
p=1
while(binary!=0):
    rem=binary%10
    sum=rem*p+sum
    binary//=10
    p=p*2
print(sum)
    