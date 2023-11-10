# print odd number in decending order and even number in accending order
    # inpute like - [14,19,18,16,25,27,11]
    # Output -      [27,25,19,11,14,16,18]
L=[14,19,18,16,25,27,11]
evn=[num for num in L if num%2==0]
odd=[num for num in L if num%2!=0]
newevn=sorted(evn)
newodd=sorted(odd ,reverse=True)
print(newodd+newevn)

#       Or

L=[14,19,18,16,25,27,11]
evn=[num for num in L if num%2==0]
odd=[num for num in L if num%2!=0]
evn.sort()
odd.sort(reverse=True)
print(odd+evn)