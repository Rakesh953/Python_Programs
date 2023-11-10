def composite(num,count=0):
    for val in range(1,num+1):
        if num%val==0:
            count+=1
    return count>2
num=12
# print(composite(num))
if composite(num):
    print('Composite Number')
else:
    print('Not a Composite Number')