num=2025
copy=num
upd=10**(len(str(num))//2)
rem=num%upd
num//=upd
if (rem+num)**2==copy:
    print('Tech number')
else:
    print('Not a Tech Number')
    