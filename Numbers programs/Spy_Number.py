num=213
sum=0
product=1
while(num!=0):
    rem=num%10
    sum=sum+rem
    product=product*rem
    # num=num//10
if(sum==product):
    print('Spy Number')
else:
    print('Not Spy Number')