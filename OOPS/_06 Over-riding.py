class A:
    def method(self):
        print('Method of a Class A')
class B(A):
    def method(self):
        print('Method of a class B')
b1=A()
b1.method()