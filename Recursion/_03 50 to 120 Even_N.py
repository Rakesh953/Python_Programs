# Print 50 to 120 all Even Numbers
def even(num):
    if num==120:
        return
    if num%2==0:
        print(num,end=' ')
    even(num+1)
even(50)

# Another Way
def even(num):
    if num%2==0:
        print(num,end=' ')
        if num==120:
            return
    even(num+1)
even(50)