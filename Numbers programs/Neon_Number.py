num=9
n=num**2
sum=0
while(n!=0):
    rem=n%10
    sum=rem+sum
    n//=10
if num==sum:
    print('Neon Number')
else:
    print('Not Neon Number')