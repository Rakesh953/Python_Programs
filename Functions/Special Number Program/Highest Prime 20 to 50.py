def prime(num,FC=0):
    for val in range(1,num+1):
        if num%val==0:
            FC+=1
    return FC==2
for num in range(50,19,-1):
    if prime(num):
        print(num)
        break