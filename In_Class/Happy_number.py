# Using function
def happy(num):
    while num>9:
        res=0
        while num!=0:
            rem=num%10
            res+rem**2
            num//=10
        num=res
    return num==1
num=49
if happy():
    print('happy')
else:
    print('Not happy')