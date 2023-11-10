# non-local 
def outer():
    n=200
    print(f'non-local1:{n}')
    def inner():
        n=300
        print(f'local:{n}')
    inner()
    print(f'non-local:{n}')
n=100
outer()
print(f'global:{n}')




def outer():
    n=200
    print(f'non-local:{n}')
    def inner():
        nonlocal n
        n=300
        print(f'local:{n}')
    inner()
    print(f'non-local:{n}')
n=100
outer()
print(f'Global:{n}')




    