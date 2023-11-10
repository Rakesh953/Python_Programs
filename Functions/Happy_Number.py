def happy(num):
    while num>9:
        sum=0
        while num!=0:
            rem=num%10
            sum=rem**2+sum
            num//=10
        num=sum
    return sum==1
num=94
print(happy(num))
