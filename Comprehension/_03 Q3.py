s1='abc'
s2='mn'
for ch1 in s1:
    for ch2 in s2:
        print(ch1+ch2)
        
        #or
s1='abc'
s2='mn'
newl=[s1+s2 for s1 in s1 for s2 in s2]
print(newl)
