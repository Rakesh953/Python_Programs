def prime(num,FC=0):
    for val in range(1,num+1):
        if num%val==0:
            FC+=1
    return FC==2
num=326547
SP=0
while num!=0:
    rem=num%10
    if prime(rem):
        SP+=rem
    num//=10
print(SP)
