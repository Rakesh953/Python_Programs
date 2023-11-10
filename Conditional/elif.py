# # highest numbers between 5 numbers

# # a,b,c,d,e=100,200,300,400,500
# # if(a>b and a>c and a>d and a>e):
# #     print('a is highest')
# # elif(b>c and b>d and b>e):
# #     print('b is highest')
# # elif(c>d and c>e):
# #     print('c is highest')
# # elif(d>e):
# #     print('d is highest')
# # else:
# #     print('e is highest')


# yr=2005
# if(yr % 100==0):
#     if(yr % 400==0):
#         print('Leap year')
#     else:
#         print('Not leap year')
# else:
#     if(yr % 4==0):
#         print('Leap year')
#     else:
#         print('NOt Leap year')

# #what is the difference between the avove code conditions and below code conditions

# year=2004
# if(year % 4==0 and year % 100!=0 ):
#     print('Leap year')
# elif(year%400==0):
#     print('Leap year')
# else:
#     print('Not leap year')
    
year=2012
yr='Leap year' if(year % 400==0 and year % 4==0) or (year % 100!=0) else 'Not leap year'
print(yr)