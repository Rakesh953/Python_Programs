factor=lambda num:list(filter(lambda fa:num%fa==0,range(1,num+1)))
print(factor(13))

even=lambda num:list(filter(lambda num:num%2==0,range(1,num+1)))
print(even(10))



