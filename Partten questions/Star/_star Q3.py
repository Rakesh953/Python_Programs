# print this
#                 *
#                **
#               ***
#              ****

space=3
for star in range(1,5):
    print(space*' ',star*'*',sep='')
    space=space-1
