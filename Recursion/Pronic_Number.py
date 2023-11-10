def Pronic(num,n=0):
    if n*(n+1)>num:
        return False
    elif n*(n+1)==num:
        return True
    else:
        return Pronic(num,n+1)
num=12
print(Pronic(num))