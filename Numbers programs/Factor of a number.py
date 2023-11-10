num=100
count=0
for val in range(1,num+1):
    if num%val==0:
        print(val)
        count+=1
print('There are',count,'factor of ',num,'above numbers are factors of',num)
