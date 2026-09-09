name = input("Enter your pet name: ") # variable declaration - input: collects data from user and stores it into a variable "name" which we print below
print(name + " is the name you have entered") # printing a variable and string

# usage of multiple variable and printing it
age = 2
country = "India"
place = "Salem"
print(name, age, place, country)

# usage of multiple variable at once using .split()
x,y,z = input("Enter your 3 fav colors: ").split()
print("your fav colors are: " + x, y + " and " + z)

# usage of type apart from string
personAge = int(input("Enter your age: "))
personHeight = float(input("Enter your height: "))
print(type(personAge))
print(type(personHeight))
print(personAge, personHeight, " is the age and height")