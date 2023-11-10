### String Inbuild method ###


## Case Conversion method ##
# Upper
s='rakesh'
print(s.upper())

# Lower
s='RakeSh mEher'
print(s.lower())

# Swapcase
s='iT cONVERT aLL sTRING lOWER tO uPPER aND uPPRE tO lOWER'
print(s.swapcase())

# title
s='IT WILL convert FIRST cHARACTER OF WORD IN GIVEN STRING TO UPPER CASE AND REMAIN CHARACTER IT WILL CONVERT LOWER CASE'
print(s.title())

# capitalize
s='it covert FirSt Alphabat To Upper case  Of The Sentence'
print(s.capitalize())


## Index Method ##
# index
S='Pythoon'
print(S.index('o',1,5))


# rindex
s='Development'
print(s.rindex('e',0,4)) # its check Last Occurance  of the string/list/Tuple in the given range

# find
s='development'
print(s.find('n'))
s='development'
print(s.find('n',0,5))

# rfind
s='we are what we are'
print(s.rfind('we'))
s='we are what we are'
print(s.rfind('we',0,3))
s='we are what we are'
print(s.rfind('are'))
s='we are what we are'
print(s.rfind('are',0,8))


# replace method
S='BANANA'
print(S.replace('A','&'))
print(S.replace('N','@'))
print(S.replace('AN','@'))
print(S.replace('ANA','@'))
print(S.replace('ANAN','@'))
print(S.replace('BANANA','@'))
print(S.replace('A','@',2))        #arg3 represent how many character you want to replace


# Count Method
cn='Hello World! Hello Hello 123'
print(cn.count('Hello'))
print(cn.count('Hello',0,8))


#Split Method
Spt='NO HOLIDAY TOMORROW'
print(Spt.split())
print(Spt.split('O'))
print(Spt.split('A'))

eng='ENGINEERING'
print(eng.split('N'))
print(eng.split(' '))
print(eng.split('E'))

gr='WE ARE GROOT'
print(gr.split('O'))

# Format String
name='RaKesh'
marks=89
subject='Math'
# print('{}got {}marks in{}'.format(subject,name,marks))
print('{} got {} marks in {}'.format(name,marks,subject))

name='Rakesh'
Marks=90
sub='maths'
yr=2023
print('{3} Got {1} Marks in {2} in the year {0}'.format(yr,Marks,sub,name))
print('{n} Got {m} Marks in {s} in the year {y}'.format(y=yr,m=Marks,s=sub,n=name))
print('{name} Got {marks} Marks in {sub} in the year {yr}')

print('{10-3}-{25+5}-{8*5}')
print(f'{10-3}-{25+5}-{8*5}')

