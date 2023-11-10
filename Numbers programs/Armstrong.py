num=123
copy=num
res=0
p=len(str(num))
while(num!=0):
    rem=num%10
    res+=rem**p
    num//10
if(copy==res):
    print('Armstrong Number')
else:
    print('Not Armonstrong Number')