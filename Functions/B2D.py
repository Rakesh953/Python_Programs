def B2D(Bin,p=1,sum=0):
    while(Bin!=0):
        rem=Bin%10
        sum=rem*p+sum
        Bin//=10
        p=p*2
    return sum
Bin=10110
print(B2D(Bin))