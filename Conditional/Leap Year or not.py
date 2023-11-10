YR = 2032
if YR%4==0 and YR%100!=0:
    print('Leap Year')
elif YR%400==0:
    print('Leap Year')
else:
    print('Not a Leap Year')