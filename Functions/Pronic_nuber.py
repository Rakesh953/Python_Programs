def Pronic(num,n=0):
    while(n*(n+1)<=num):
        if(n*(n+1)==num):
            return True
        n=n+1
    return False
num=12
print(Pronic(num))
