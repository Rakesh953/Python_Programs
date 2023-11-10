s='MONK IS IMPORTANT'
# s='ENGINEERING'
news=''
for ch in s:
    if ch not in news:
        news+=ch
print(news)