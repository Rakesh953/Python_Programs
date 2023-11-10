        #Object Member
class Py_spiders:
    c_name='Python FullStack Development'
    b_name='Marthahalli'
    def __init__(self,Name,MNo,Mail):
        self.Name=Name
        self.MNo=MNo
        self.Mail=Mail
    def DTL(self):
        # print(f"{self.Name} Mobile Number is {self.MNo} And Mail is {self.Mail}")
        print('PP')
p1=Py_spiders('Rakesh',9078895125,'R@gmail.com')
p2=Py_spiders('Hari',9077798567,'H@gmail.com')
p3=Py_spiders('Ram',7895347896,'Rm@gmail.com')
p1.DTL()
p2.DTL()