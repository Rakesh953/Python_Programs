def strong(num,copy,sum=0):
    while num!=0:
        rem=num%10
        FC=1
        for val in range(1,rem+1):
            FC=FC*val
        sum=sum+FC
        num//=10
    return copy==sum
num=145
print(strong(145,copy=num))
# if strong(num,num):
#     print('Strong Number')
# else:
#     print('Not a Strong Number')