# num=17
# copy=num
# rev=0
# count=0
# count1=0
# while(num!=0):  #Not palindrom
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
    
# # if(rev==copy):
# #     print('palindrom')
# # else:
# #     print('N padlindrom')

# for value in range(1,copy+1): #prime or not
#     if(copy%value==0):
#         count1=count1+1

# # if(count1==2):
# #     print("prime")
# # else:
# #     print('Not Prime')


# while(num!=0):  #Reverse number is prime or not
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# for value2 in range(1,rev+1):
#     if(rev%value2==0):
#         count=count+1
        
# # if(count==2):
# #     print('Prime Number')
# # else:
# #     print('Not a prime number')
            
# if(rev!=copy) and (count1==2) and (count==2):
#     print('Emirp Number')
# else:
#     print('Not a Emirp number')

    
num=17
copy=num
rev=0
count=0
count1=0
while(num!=0):  #Not palindrom
    rem=num%10
    rev=rev*10+rem
    num=num//10
for value in range(1,rev+1):
    if(rev%value==0):
        count=count+1
for value1 in range(1,copy+1): #prime or not
    if(copy%value1==0):
        count1=count1+1
if(rev!=copy) and (count==2) and (count1==2):
    print('Emirp Number')
else:
    print('Not a Emirp number')

    
