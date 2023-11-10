L=[12,13,11,15,10,18]
m=max(L,key=lambda num:[num%5])
print(m)

s='we are in hunger of job'
l=s.split()
m=max(l,key=len)
print(m)


s='engineering'
m=max(s,key=lambda ch:[s.count(ch)])
print(m)