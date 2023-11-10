def armstrong(num,copy,p,sum=0):
    while(num!=0):
        rem=num%10
        sum=rem**p+sum
        num//=10
    return copy==sum
num=153
print(armstrong(num,num,len(str(num))))