def prime(num,FC=0):
    for val in range(1,num+1):
        if num%val==0:
            FC+=1
    return FC==2
for num in range(20,50):
    if prime(num):
        print(num)