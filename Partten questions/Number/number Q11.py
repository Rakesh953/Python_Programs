	# 12345
	#  1234
	#   123
	#    12
	#     1
sp=0
for ev in range(5,0,-1):
    print(' '*sp,end='')
    for num in range(1,ev+1):
        print(num,end='')
    sp+=1
    print()