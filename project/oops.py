# basic class and object

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name, self.age)
    
s1 = Student("Mohith", 19)
s1.display()

# constructor
class Car:
    def __init__(self, brand):
        self.brand = brand
        
c1 = Car("BMW")

# encapsulation
class Account:
    def __init__(self):
        self._balance = 0
    
    def deposit(self, amount):
        self._balance += amount
        
    def get_balance(self):
        print(self._balance)

a1 = Account()
a1.deposit(1000)
a1.get_balance()


# inheritance
class Animal:
    def speak(self):
        print("Animal speak")
    
class Dog(Animal):
    def bark(self):
        print("Dog bark")
        
d1 = Dog()
d1.speak()
d1.bark()


# Polymorphism (overridding)
class Animal:
    def sound(self):
        print("Animal sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

c = Cat()
a2 = Animal()
a2.sound()
c.sound()

# overloading
class Calaculations:
    def add(self, *args):
        return sum(args)
    
sum1 = Calaculations()
print(sum1.add(1,2,3))
print(sum1.add(1,2))

#Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class rectangle(Shape):
    def area(self, l, w):
        return l * w
    
r1 = rectangle()
print(r1.area(3, 4))







        


