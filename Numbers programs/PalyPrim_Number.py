num=181
count=0
copy=num
rev=0
for v in range(1,num+1):
    if(num%v==0):
        count+=1
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if(count==2) and(rev==copy):
    print('PalyPrime Number')
else:
    print('Not a PalyPrime Number')
    