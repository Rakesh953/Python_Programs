
s='python'
count=1
for ch in s:
    print(ch*count)
    count+=1
   

s='python'
count=6
for ch in s:
    print(ch*count)
    count-=1


s='PYTHON'
for ei in range(1,7):
    print(s[:ei])

s='python'
for ei in range(6,0,-1):
    print(s[:ei])

s='PYTHON'
space=5
for si in range(-6,0,1):
    print(' '*space,s[si:-7:-1],sep='')
    space-=1
    
s='python'
space=0
for si in range(-1,-7,-1):
    print(' '*space,s[si:-7:-1],sep='')
    space+=1
    
s='PYTHON'
for si in range(-6,0):
    print(s[si:-7:-1])
    
    
s='PYTHON'
for si in range(-1,-7,-1):
    print(s[si:-7:-1])
    
s='python'
space=6
for ei in range(0,7):
    print(' '*space,s[:ei],sep='')
    space-=1