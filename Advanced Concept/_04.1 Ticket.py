def single_ton(cls):
    l=[]
    def inner():
        if len(l)==0:
            obj=cls()
            l.append(obj)
        return l[0]
    return inner
@single_ton
class leo:
    def __init__(self):
        self.tickets=300
    def booking(self):
        tickets=int(input('Enter numbers of tickets :'))
        if self.tickets>=tickets:
            self.tickets-=tickets
            print('Tickets Booked succesfully...')
        else:
            print('Ticket is not available')
@single_ton
class jawan:
    def __init__(self):
        self.tickets=300
    def booking(self):
        tickets=int(input('Enter numbers of tickets :'))
        if self.tickets>=tickets:
            self.tickets-=tickets
            print('Tickets Booked succesfully...')
        else:
            print('Ticket is not available')
def book_my_Show():
    print('1-->Leo\n2-->Jawan')
    option=int(input('Choose an option:'))
    if option==1:
        l1=leo()
        l1.booking()
    elif option==2:
        j1=jawan()
        j1.booking()
    else:
        print('Please choose a valid option...')      
while True:
    book_my_Show()
    print('___'*10)