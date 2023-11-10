s='ENGINEERING'
L=sorted(s)
print(L)


s='ENGINEERING'
L=sorted(s, key=lambda ch:[s.count(ch),ch])
print(L)

#arrange word to string according to its Length
s='we are in hunger of job'
l=sorted(s.split(),key=len)
print(l)

# print key in dictonary which is having the highest value
d={'a':100,'n':20,'b':30,'d':45}
L=max(d)
print(L)    #It finding the highest valeu of key(in ANSII Value)

d={'a':100,'m':1011, 'n':20, 'b':30, 'd':45}
L=max(d,key=lambda dt:[d[dt],dt])
print(L)

# arrange the key in doctonary according value
d={'a':100,'m':1011, 'n':20, 'b':30, 'd':45}
l=sorted(d,key=lambda k:d[k])
print(l)

# arrange the key in doctonary according value in decending order
d={'a':100,'m':1011, 'n':20, 'b':30, 'd':45}
l=sorted(d,key=lambda k:d[k],reverse=True)
print(l)

