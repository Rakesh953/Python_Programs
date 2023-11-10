def palindrom(num,copy,rev=0):
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev==copy
num=202
print(palindrom(num,num))