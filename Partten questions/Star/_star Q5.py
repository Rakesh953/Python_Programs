# diplay this using loop
#                           *
#                          ***
#                         *****
#                        *******
#                       *********

space=4
for star in range(1,11,2):
    print(space * ' ',star * '*',sep='')
    space-=1