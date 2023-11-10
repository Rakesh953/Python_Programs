def auto(num,sqr,p):
    return sqr%10**p==num
num=25
print(auto(num,num**2,len(str(num))))
      
    
        