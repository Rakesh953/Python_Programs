class Bank:
    Bank_Name   = 'SBI'
    Branch_Name = 'Marthahalli'
    IFSC_Code   = 'SBI00891S160'
    ROI         =  0.06
    def __init__(self,Name,ACCNO,Mno,Bal,Pin):
        self.Name  = Name
        self.ACCNO = ACCNO
        self.Mno   = Mno
        self.Bal   = Bal
        self.Pin   = Pin
    @staticmethod
    def validate():
        return int(input('Enter 4 Dig Pin:'))
    def Withdraw(self):
        if self.Pin==self.validate():
            amount=int(input('Enter Your Amount:'))
            if self.Bal>amount:
                self.Bal-=amount
                print(self.Bal)
            else:
                print('Insufficient Balance...')
        else:
            print('Incurrect Pin...')
    def deposite(self):
        if self.Pin==self.validate():
            amount=int(input('Enter Your Amount :'))
            self.Bal+=amount
        else:
            print('Incorrect Pin....')
    def check_Bal(self):
        if self.Pin==self.validate():
            print(f"{self.Bal}/--")        
        else:
            print('Incorrect Pin...')
    def change_Pin(self):
        if self.Pin==self.validate():
            Pin1=int(input('Enter the new Pin:'))
            Pin2=int(input('Re-Enter The Pin:'))
            if Pin1==Pin2:
                self.pin=Pin1
                print('Pin Updated Successfuly...')
            else:
                print('Re-entered Pin is not matching\nPlease Try again...')
        else:
            print('Incorrect pin.....')
    @classmethod
    def ROI(cls):
        cls.ROI=float(input('Enter New Intrest :'))
        
B1=Bank('Rakesh Meher',466277011000841,9078896543,5000,1111)
B2=Bank('Siva Khamari',366267011090841,8578892543,6000,2222)

B1.Withdraw()


    

        