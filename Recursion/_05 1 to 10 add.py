def add(num):
    if num==10:
        return num
    return num+add(num+1)
print(add(1))