num=6
Factor_sum=0
for value in range(1,(num//2)+1):
    if(num%value==0):
        Factor_sum+=value
if(Factor_sum==num):
    print('Perfect Number')
else:
    print('Not a Perfect Number')


num = 6
Fsum=0
for val in range(1,num+1):
    if num%val==0:
        Fsum+=val
if num*2==Fsum:
    print('Perfect')
else:
    print('Not Perfect')