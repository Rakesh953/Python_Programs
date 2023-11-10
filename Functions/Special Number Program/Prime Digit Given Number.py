def prime(num,FC=0):
    for val in range(1,num+1):
        if num%val==0:
            FC+=1
    return FC==2
num=326547
while num!=0:
    PD=num%10
    if prime(PD):
        print(PD)
        num//=10
    else:
        num//=10
    






# PD=num%10
# if prime(PD):
#     print(PD)
#     num//=10
# else:
#     num//=10