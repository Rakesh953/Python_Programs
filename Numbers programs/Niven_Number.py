num=114
copy=num
sum=0
while num!=0:
    rem=num%10
    sum+=rem
    num//=10
print('Niven' if copy%sum==0 else 'Not Niven')