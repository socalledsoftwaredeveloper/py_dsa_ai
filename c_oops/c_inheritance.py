# INHERITANCE
class Animal:
    def __init__(self, name): # CONSTRUCTOR
        self.name = name # reusable properties - object attribute

    def info(self): # method
        print("Animal name:", self.name)

class Dog(Animal): # another class Dog(Animal) - Dog class inherits Animal(Base class)
    def sound(self): # this self will have access of current object that also have access to parent class attributes
        print(self.name, "barks")

d = Dog("Buddy")
# Inherited method
d.info()     
d.sound()



# SUPER() usage
class Animal: # Parent Class: Animal
    def __init__(self, name): # CONSTRUCTOR of this PARENT CLASS
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal): # Child Class: Dog and Animal is being inherited to Dog class
    def __init__(self, name, breed): # CONSTRUCTOR
        super().__init__(name) # Calls constructor based on MRO(Method Resolution Order)
        self.breed = breed

    def details(self):
        print(self.name, "is a", self.breed)

d = Dog("Buddy", "Golden Retriever") # object
d.info()      # Parent class method
d.details()   # Child class method



# Method OverRiding
class Fruit:
    def itsColor(self):
        print("fruit color method")

class Veggies(Fruit): # Fruit base class is inherited to Veggies child class
    def itsColor(self):
        print("Veggies method overriding is completed")

e1 = Fruit()
e1.itsColor()
e2 = Veggies()
e2.itsColor()