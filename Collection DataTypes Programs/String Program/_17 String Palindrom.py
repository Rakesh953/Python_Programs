# check String Palindrom or not without Using Reversing the string
s = 'MALAYALAM'
n = len(s)
Last_Iteration = -1
for First_Iteration in range(n // 2):
    if s[First_Iteration] == s[Last_Iteration]:
        Last_Iteration -= 1
    else:
        print('Not Palindrome')
        break
else:
    print('Palindrom')



s='racecar'
n=len(s)
li=-1
for fi in range(n // 2):
    if s[fi]==s[li]:
        li-=1
    else:
        print('Not palindrom')
        break
else:
    print('Palindrom')