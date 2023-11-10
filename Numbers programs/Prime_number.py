num=3
count=0
for value in range(1,num+1): #prime or not
    if(num%value==0):
        count=count+1
if(count==2):
    print(value,"is a prime number",)
else:
    print(value,'Not a Prime number')


#   With Out counting The Factors
# num=7
# if num>1:
#     for val in range(2,(num//2)+1):
#         if num%val==0:
#             print('Not a Prime Number')
#             break
#     else:
#         print('prime Number')
# else:
#     print('Not a Prime Number')