#To Print 1 to 10
def OT(num):
    print(num)
    if num==10:
        return
    OT(num+1)
OT(1)