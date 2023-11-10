num=10
sum=0
while(num!=0):
    rem=num%2
    sum=sum+rem
    num//=2
if(sum==2):
    print('Evil Number')
else:
    print('Odious Number')