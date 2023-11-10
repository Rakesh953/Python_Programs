def sample(num):
    print(num)
    if num==10:
        return
    sample(num+1)
sample(1)