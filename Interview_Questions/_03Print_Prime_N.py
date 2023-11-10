num=785294
rem=0
res=0
while(num!=0):
    rem=num%10
    fc=0
    for value in range(1,rem+1): 
        if(rem%value==0):
            fc=fc+1
    num//=10
    if(fc==2):
        print(rem)
        