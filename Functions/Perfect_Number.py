def perfect(num,sum=0):
    for val in range(1,(num//2)+1):
        if num%val==0:
            sum=sum+val
    return num==sum
num=28
print(perfect(num))
# if perfect(num):
#     print('Perfect Number')
# else:
#     print('Not a perfect number')

def Perfect(num,Fsum=0):
    for val in range(1,num+1):
        if num%val==0:
            Fsum+=val
    return num*2==Fsum
print(Perfect(28))