for num in range(100,1000):
   # print(num)
   res=0
   copy=num
   p=len(str(num))
   while(num!=0):
     rem=num%10
     res+rem**p
     num//=10
if copy==res:
      print(num)
     
    