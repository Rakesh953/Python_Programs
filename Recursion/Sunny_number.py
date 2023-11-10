def Sunny(num,n=0):
    if n**2>num+1:
        return False
    elif n**2==num+1:
        return True
    else:
        return Sunny(num,n+1)
num=8
print(Sunny(num))
if Sunny(num):
    print('Sunny Number')
else:
    print('Not a Sunny Number')