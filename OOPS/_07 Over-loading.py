#   Method Over-loading
class mno:
    def add(self,a,b):
        return  a+b
    def add(self,a,b,c):
        return a+b+c
    def add(self,a,b,c,d):
        return a+b+c+d
m1=mno()
print(m1.add(10,20))   

# We can not perform Over-loading in python because it takes latest defined method
# But we can achieve it The help of default argument

class mno:
    def add(self,a=0,b=0,c=0,d=0):  #Default Argument
        return  a+b+c+d
m1=mno()
print(m1.add(10,20,30))