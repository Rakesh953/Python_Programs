# def prime(num,count=0):
#     for val in range(1,num+1):
#         if num%val==0:
#             count+=1
#     if count==2:
#         print('Prime Number')
#     else:
#         print('Not a Prime Number')
# prime(7)



def prime(num,count=0):
    for val in range(1,num+1):
        if num%val==0:
            count+=1
    return count==2 
num=3
print(prime(num))
if prime(num):
    print('Prime Number')
else:
    print('Not a Prime Number')