class Bank_V1:
    def __init__(self,Name,Mno,Accno,Pan,Bal):
        self.Name=Name
        self.Mno=Mno
        self.Accno=Accno
        self.Pan=Pan
        self.Bal=Bal
class Bank_V2(Bank_V1):
    def __init__(self,Name,Mno,Accno,Pan,Bal,Adhar,Email):
        super().__init__(Name,Mno,Accno,Pan,Bal)
        self.Adhar=Adhar
        self.Email=Email
B1=Bank_V2('Rakesh',9078898456,202089782524,987765907,9000,8877665522445,'R@gmail')
print(Bank_V2)
