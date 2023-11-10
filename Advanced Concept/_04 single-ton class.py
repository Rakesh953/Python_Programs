def single_ton(cls):
    L=[]
    def inner():
        if len(L)==0:
            obj=cls()
            L.append(obj)
        return L[0]
    return inner

@single_ton
class sample:
    def __init__(self):
        print('Hello World')
        
s1=sample()
s2=sample()
s3=sample()
print(s1)
print(s2)
print(s3)