#W.A.P To given number is Armstrong Number or not
num=34
copy=num
res=0
p=len(str(num))
while(num!=0):
    rem=num%10
    res+=rem**p
    num=num//10
if(copy==res):
    print('Armonstrong ')
else:
    print('Not armonstrong')
    
