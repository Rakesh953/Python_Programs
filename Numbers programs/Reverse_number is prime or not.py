num=13
copy=num
rev=0
count=0
while(num!=0):  #Reverse number is prime or not
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)  
for v in range(1,rev+1):
    if(rev%v==0):
        count=count+1
if(count==2):
    print('Prime Number')
else:
    print('Not a prime number')