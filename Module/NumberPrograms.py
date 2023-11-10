# prime number
def prime(num,fcount=0):
    for val in range(1,num+1):
        if num%val==0:
            fcount+=1
    return fcount==2
# print(prime(12))

# composite number
def composite(num,fcount=0):
    for val in range(1,num+1):
        if num%val==0:
            fcount+=1
    return fcount>2
# print(composite(12))

# perfect number
def perfect(num,factsum=0):
    for val in range(1,num//2+1):
        if num%val==0:
            factsum+=val
    return num==factsum
# print(perfect(12))

# pronic number
def pronic(num,n=0):
    while(n*(n+1)<=num):
        if(n*(n+1)==num):
            return True
        else:
            n+=1
    return False
# print(pronic(12))

# sunny number
def sunny(num,n=0):
    while(n**2<=num+1):
        if(n**2==num+1):
            return True
        else:
            n+=1
    return False
# print(sunny(16))

# niven number
def sumdig(num,dsum=0):
    while(num!=0):
        rem=num%10
        dsum+=rem
        num//=10
    return dsum
def niven(num):
    return num%sumdig(num)==0
# print(niven(235))

# spy number
def sumdig(num,dsum=0):
    while(num!=0):
        rem=num%10
        dsum+=rem
        num//=10
    return dsum
def prodig(num,psum=1):
    while(num!=0):
        rem=num%10
        psum*=rem
        num//=10
    return psum
def spy(num):
    return sumdig(num)==prodig(num)
# print(spy(123))


# palindrome no.
def reverse(num,rev=0):
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev
def palindrome(num):
    return num==reverse(num)
# print(palindrome(121))

# pallyprime no.
def reverse(num,rev=0):
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev
def prime(num,factcount=0):
    for val in range(1,num+1):
        if(num%val==0):
            factcount+=1
    return factcount==2
def palyprime(num):
    return num==reverse(num)and prime(num)
# print(palyprime(11))



# neon number
def sumdig(square,dsum=0):
    while(square!=0):
        rem=square%10
        dsum+=rem
        square//=10
    return dsum

def neon(num):
    return num==sumdig(num**2)
# print(neon(12))


# print(prime(3))  #Direct Call The Function in same Module

# print('name:',__name__)


if __name__=='Main':
    print(prime(3))
    print(perfect(28))
    print(prime(3))


# print(__name__)

# import Numberprograms
# if __name__=='Main':
#     print(Numberprograms(28))