# General usage
a = "Max"
print("a value is: ", a)
a = 2
print("a value is: ", a)

# type casting and case sensitive
b = "Honey"
B = 333
print("b lowerCase  is: ", b)
print("B upperCase is: ", B)

# multiple variables at once
c,d,e = 1, "Max", 24.6
print(c, d, e)

# same values to multiple variables
f=g=h = "Hitler"
print(f)
print(g)
print(h)

# unpacking collection and keeping it in variable - just like extract and use in var on JS
fruits = ["JackFruit", "Guava", "Papaya"]
fruit1, fruit2, fruit3 = fruits
print("Fruit 1 is: ", fruit1)
print("Fruit 2 is: ", fruit2)
print("Fruit 3 is: ", fruit3)

# local and global vars
age = 3
name = "Max"
def userDetails():
    age = 5 # LOCAL
    global name # GLOBAL var OVERWRITTEN
    name = "Karupu"
    print("Inside function AGE is:", age , "and name is:", name)

userDetails()
print("Age is: ", age) # This will give only global var data
print("Name is: ", name) # this will not throw error since we made name as global in fn()
# print("Place is: ", place) # ERROR since place is not defined/declared with any values

# var swapping
g,h=1,2
print(g, h) # g is 1 and h is 2
g,h = h,g # swapped
print(g, h) # now, g is 2 and h is 1

# string length
place = "German"
print("Length of place variable is: ", len(place))

# variable deletion
mfg = 2021
print("mfg: ", mfg)
del mfg
# print("mfg: ", mfg) # this will produce error since we are trying to access deleted(non existing) variable