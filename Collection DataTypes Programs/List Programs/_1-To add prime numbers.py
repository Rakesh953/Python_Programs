L=[1,2,3,4,5,6,7]
sum=0
for num in L:
    if num>1:
        count=0
        for val in range(1,num+1):
            if num%val==0:
                count+=1
        if count==2:
            sum+=num
print(sum)