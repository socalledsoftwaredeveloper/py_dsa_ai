# ENCAPSULATION
class Animal:
    def __init__(self, name, age, country): # constructor
        self.name = name # PUBLIC - all attributes by default in py is public unless we use (_ or __). Public can be access anywhere(own class, sub-class or the object)
        self._age = age # PROTECTED - usage of single underscore _ (can be accessed in both  main & its sub-class)
        self.__country = country # PRIVATE - usage of double underscore __ (can be only access within main class)

    def fullDetails(self):
        return f"Hi, I am {self.name}, I'm {self._age} years old and I come from {self.__country}"


class Dog(Animal):
    def dogDetail(self):
        return f"Hi, my name is {self.name} and I'm {self._age}. Please dont ask me about my country it's so confidential"

obj1 = Dog("Max",2, "India")
print(obj1.dogDetail())
print(obj1.fullDetails())



# ENCAPSULATION - usage of public/protected/private methods
class BankAccount:
    def __init__(self, amount):
        self.__amount = amount # PRIVATE
        self.__updateYearlyInterest() # calling PRIVATE METHOD when object is initialized itself. The interest is calculated with initial amount of 2000

    def _showBalance(self): # PROTECTED function
        return f"Total balance: {self.__amount}"

    def depositAmount(self, depositAmount): # PUBLIC
        self.__amount+=depositAmount
        return f"Amount deposited successfully, new balance: {self.__amount}"

    def __updateYearlyInterest(self): # PRIVATE
        yearly_Interest_Percent = 16
        yearlyInterest = (self.__amount / 100) * yearly_Interest_Percent
        self.__amount+=yearlyInterest
        return f"Your annual balance post interest of {yearly_Interest_Percent} is: {self.__amount}"

b1 = BankAccount(2000)
print(b1.depositAmount(1000))
print(b1._showBalance()) # NOTE: It works, but should be treated as internal
# print(b1.__updateYearlyInterest()) # NOTE: This will throw error since private method



# GETTERS and SETTERS - recommended way to update the access modifiers attributes safely
class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):    # Getter method - with prefix (GET)
        return self.__salary

    def set_salary(self, amount):   # Setter method - with prefix (SET)
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")

emp = Employee()
print(emp.get_salary())  # Access salary using getter

emp.set_salary(60000)   # Update salary using setter
print(emp.get_salary())



# MANGLING example - this is highly used in Inheritance concept to prevent over-ride of variables (NOTE: python changes the mangling names as -> _ClassName__Attribute)
class Tree1:
    def __init__(self):
        self.__treeName = "Parent tree"
class Tree2(Tree1):
    def __init__(self):
        super().__init__()
        self.__treeName = "Child Tree"

tree = Tree2()
print(tree._Tree1__treeName) # NOTE: This shows that our PRIVATE variable is not truly PRIVATE, we can also access by this way
print(tree._Tree2__treeName)



# NO MANGLING usage - override example
class Parent0:
    def __init__(self):
        self.show()

    def show(self):
        print("Parent 0 class")

class Child0(Parent0):
    def show(self):
        print("Child 0 class")


obj = Child0()
obj.show()



# MANGLING USAGE - (Mix of : override, inheritance, name mangling and assigning a method/function to a reference and safely ignoring overriding)
class Parent1:
    def __init__(self):
       self.__show() # name mangling variable - will be called as soon object initialization is happened. NOTE: This conceptually becomes self._Parent__show() due to name mangling

    def show(self):
       print("Parent 1 class")
    __show = show # This mean, we are storing the function to a name mangling reference variable - to prevent overriding

class Child1(Parent1):
     def show(self):
        print("Child 1 class")

obj = Child1()
obj.show()