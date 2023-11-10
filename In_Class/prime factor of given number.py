# to print prime factor of given number
num=56
for n in range(1,num+1):
    if num%n==0:
        Fc=0
        for val in range(1,n+1):
            if n%val==0:
                Fc=Fc+1
        if Fc==2:
            print(n)