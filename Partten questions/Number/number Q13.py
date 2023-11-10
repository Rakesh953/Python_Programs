	# 54321
	#  5432
	#   543
	#    54
	#     5
sp=0
for ev in range(0,5):
    print(' '*sp,end='')
    for num in range(5,ev,-1):
        print(num,end='')
    sp+=1
    print()