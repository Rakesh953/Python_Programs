def outer(arg):
    def inner():
        print('**************')
        arg()
        print('**************')
    return inner
@outer
def mno():
    print('Hello World!!!')
mno()