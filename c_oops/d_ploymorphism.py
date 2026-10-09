# POLYMORPHISM - same function but different behavior
# Below I have used(inheritance, super k/word usage) It might be complex when seen, just see 2nd example for simple clarity if you find this first example as difficult
class Animal:
    isAlive = True # class attribute 
    def __init__(self, name):
        self.name = name # instance attribute
    def speak(self):
        return "Animal is making sound"

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        return f"Dog woof, and it's age is: {self.age} and currently is it still alive {self.isAlive}"

class Cat:
    def speak(self):
        return "Cat meow"

a1 = Animal("Kangaroo")
print(a1.speak())

d1 = Dog("Max", 2)
print(d1.speak())

c1 = Cat()
print(c1.speak())



# Simple Polymorphism example
class Phone:
    def ring(self):
        return "Phone -> tring tring"

class CellPhone:
    def ring(self):
        return "CellPhone-> tada tan tan tan"

class CoinPhone:
    def ring(self):
        return "CoiPhone -> killeling killeling"

phone1 = Phone()
cell1 = CellPhone()
coin1 = CoinPhone()
print(phone1.ring())
print(cell1.ring())
print(coin1.ring())



# POLYMORPHISM - 2 types (COMPILE-TIME POLYMORPHISM and RUNTIME POLYMORPHISM)
# COMPILE TIME POLYMORPHISM - It does know what it mean before running
class MathOps():
    def __init__(self, num1, *num2):
        return sum(num1, num2)

def sum(num1, num2):
    resOfNum2 = 0
    for i in num2:
        resOfNum2+=i
    print(num1+resOfNum2)
    # return num1+resOfNum2 # NOTE: Err will produce since __init__() only returns "None" and not any other type value

m1 = MathOps(1,2)
m1
m2 = MathOps(1,2,3,4,5)
m2

# or

class MathOps2():
    def __init__(self, num1, *num2):
        return sum(num1, num2)

def sum(num1, num2):
    result = num1+num2[0] if len(num2)<2 else callLoop(num1,num2)
    print(result)

def callLoop(num1,num2):
    resOfNum2 = 0
    for i in num2:
        resOfNum2+=i
    return num1+resOfNum2 # NOTE: Err will produce since __init__() only returns "None" and not any other type value

m1 = MathOps2(1,4)
m1
m2 = MathOps2(1,20,30,4,5)
m2

# RUNTIME POLYMORPHISM - It only knows at the time of running
class Animal:
    def makeSound(self): # always pass "self" or any args but don't leave it empty - will throw err if 0 args
        print("Animal is making sound")

class Dog(Animal):
    def makeSound(self):
        print("Dog sound - WOFF")

class Cat(Animal):
    def makeSound(self):
        print("Cat is making sound - MEOW")

def now_makeSound(obj): # Here, the function doesn't need to know but, the actual obj which is betting called would determine it (check line 110, 111)
    obj.makeSound()

now_makeSound(Dog())
now_makeSound(Cat())