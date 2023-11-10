# Example 1
mul=list(map(lambda n:n*10,[4,5,6]))
print(mul)

# Example 2
mul=list(map(lambda n:'Hello',[4,5,6]))
print(' '.join(mul))

# Star pattern Programs using Map function 
#       *
#       **
#       ***
#       ****
#       *****
st=list(map(lambda star:'*'*star,range(1,6)))
print('\n'.join(st))

#           *
#          **
#         ***
#        ****
#       *****
st=list(map(lambda space,star:' '*space+'*'*star,range(3,-1,-1),range(1,5)))
print('\n'.join(st))

 
#       ****
#        ***
#         **
#          *
st=list(map(lambda space,star:' '*space+'*'*star,range(4),range(4,0,-1)))
print('\n'.join(st))


#      *
#     ***
#    *****
#   *******
st = list(map(lambda space,star:' '*space+'*'*star,range(3,-1,-1),range(1,8,2)))
print('\n'.join(st))

#  *
#  **
#  ***
#  ****
#  ***
#  **
#  *
st=list(map(lambda star:'*'*star,range(1,5)))
print('\n'.join(st))
st1=list(map(lambda star:'*'*star,range(3,0,-1)))
print('\n'.join(st1))

#        1
#        22
#        333
#        4444
#        55555

n=list(map(lambda num:str(num)*num,range(1,6)))
print('\n'.join(n))

#       1
#      22
#     333
#    4444
#   55555
n=list(map(lambda space,num:' '*space + str(num)*num,range(4,-1,-1),range(1,6)))
print('\n'.join(n))