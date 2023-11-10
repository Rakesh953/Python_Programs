def add(num):
    if num==5:
        return num
    return num+add(num+1)
num=1
print(add(num))
