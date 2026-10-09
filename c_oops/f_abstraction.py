# ABSTRACT METHOD
from abc import ABC, abstractmethod

class Animal(ABC): # pass ABC(Abstract Base Class) as inherit params to base class
    @abstractmethod
    def speak(self): # define the method so that the child class which is inheriting base class will be implementing this method
        pass # Abstract method, no implementation here

class Dog(Animal):
    def speak(self):
        return "Woff"

class Cat(Animal):
    def speak(self):
        return "Meow"

d1 = Dog() # Objects can be created by the child which is inheriting parent that has abstract method but, the parent class which has abstract method we can't create object - will throw err
c1 = Cat()
print(d1.speak())
print(c1.speak())
# a1 = Animal()
# print(a1.speak()) # Err - class which has abstract method we can't create object from it



# ABSTRACT PROPERTY(piece of info) with ABSTRACT METHOD(a behavior/action)
class Employee(ABC):
    @property # NOTE: It let you to access method like an attribute (from the below created obj, instead of Developer.salary() we can asses like Developer.salary)
    @abstractmethod
    def salary(self):
        pass # Abstract method, no implementation here

class Developer(Employee):
    @property # NOTE: If we miss @property then while accessing we will get address instead of string
    def salary(self):
        return 80000

class Manager(Employee):
    @property
    def salary(self):
        return 120000

d1 = Developer()
m1 = Manager()
print(d1.salary) # accessing like attribute instead of method
print(m1.salary) # accessing like attribute instead of method