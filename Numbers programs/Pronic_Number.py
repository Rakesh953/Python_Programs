num=12
n=0
while(n*(n+1)<=num):
    if(n*(n+1)==num):
        print('Pronic number')
        break
    else:
        n=n+1
else:
    print('Not a pronic number')
print(n)


