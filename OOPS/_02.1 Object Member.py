class py_spider:
    c_name='Python FullStack Development'
    b_name='Marthahalli'
    def __init__(self,Name,Mno,Email):
        self.Name=Name
        self.Mno=Mno
        self.Email=Email
    def SD(self):
        print(f'{self.Name} is a {self.c_name} Student \nHis Mobile Number:{self.Mno}\nHis Gmail is {self.Email}')
P1=py_spider('Rakesh',9078895123,'R@gmail')
P2=py_spider('Famesh',9087765437,'F@gmail.com')

# P1.SD()
P2.SD()