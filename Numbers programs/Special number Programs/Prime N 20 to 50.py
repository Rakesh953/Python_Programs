for v1 in range(1,100):
    FC=0
    for v2 in range(1,v1+1):
        if v1%v2==0:
            FC+=1
    if FC==2:
        print(v1)