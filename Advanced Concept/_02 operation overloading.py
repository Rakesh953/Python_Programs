class mno:
    def __init__(self,n):
        self.n=n
    def __add__(self1,self2):
        return self1.n+self2.n
    def __sub__(self1,self2):
        return self1.n-self2.n
    def __mul__(self1,self2):
        return self1.n*self2.n
m1=mno(2)
m2=mno(4)
print(m1+m2)
print(m1-m2)
print(m1*m2)