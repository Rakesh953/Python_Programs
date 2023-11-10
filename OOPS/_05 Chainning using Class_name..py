class A:
    def __init__(self):
        print('Constructor in A')
class B:
    def __init__(self):
        print('Constructor In B')
class C:
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('Constructor C')
C1=C()