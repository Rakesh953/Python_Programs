def OT(num):
    print(num)
    if num==1:
        return
    OT(num-1)
OT(10)