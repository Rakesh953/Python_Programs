from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    def walk(self):
        print('Walk with 4 legs')
class Dog(animal):
    def speak(self):
        print('Boo...Booo..')
class Cat(animal):
    def speak(self):
        print('Miao... Miao..')
class Goat(animal):
    def speak(self):
        print('Mehh.. Mehh..')
class Monkey(animal):
    def speak(self):
        print('Gruh....Gruh....')
    def walk(self):
        print('Walk wwith 2 Legs')
        
d1=Dog()
d1.speak()
d1.walk()

d2=Cat()
d2.speak()
d2.walk()

d3=Goat()
d3.speak()
d3.walk()

d4=Monkey()
d4.speak()
d4.walk()