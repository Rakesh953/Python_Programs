def tech(num,copy,upd):
    rem=num%upd
    num//=upd
    return(rem+num)**2==copy
num=2025
print(tech(num,num,10**(len(str(num))//2)))




# if tech(num,num,10**(len(str(num))//2)):
#     print('Tech Number')
# else:
#     print('Not a Tech Number')