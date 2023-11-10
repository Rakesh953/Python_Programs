num=1
count=0
for value in range(1,num+1):
    if(num%value==0):
        count+=1
if(count>2):
    print('Composite Number')
else:
    print('Not composite Number')
    