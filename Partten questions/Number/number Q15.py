# 	  5
#    45
#   345
#  2345
# 12345
sp = 4
for sv in range(5,0,-1):
    print(' '*sp,end='')
    for num in range(sv,6):
        print(num,end='')
    sp-=1
    print()