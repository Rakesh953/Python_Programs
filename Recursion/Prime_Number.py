def prime(num,val):
    if num%val==0 or num<=2:
        return False
    if val==num//2:
       return True
    return prime(num,val+1)
num=7
if prime(num,val=2):
    print('Prime')
else:
    print('Not Prime')
   
# def prime(num):
#     if num%2==0 or num<=2:
#         return False
#     if num==num//2:
#         return True
#     return prime(num,2+1)
# if prime(num=9):
#     prime('Prime')
# else:
#     print('Not Prime')