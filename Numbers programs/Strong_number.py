#Strong Number
num=145
copy=num
sum=0
while(num!=0):
    rem=num%10
    ans=1
    for val in range(1,rem+1):
        ans=ans*val
    sum=sum+ans
    num//=10
if copy==sum:
    print('Strong Number')
else:
    print('Not a strong Number')