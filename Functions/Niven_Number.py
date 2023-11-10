def niven(num,copy,sum=0):
    while(num!=0):
        rem=num%10
        sum+=rem
        num//=10
    return copy%sum==0
num=153
print(niven(num,copy=num))

# if (niven(num,num)):
#     print('Niven Number')
# else:
#     print('Not a Niven Number')