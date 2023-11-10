# 12345
#  2345
#   345
#    45
#     5

sp=0
for sv in range(1,6):
    print(' '*sp,end='')
    for num in range(sv,6):
        print(num,end='')
    sp+=1
    print()