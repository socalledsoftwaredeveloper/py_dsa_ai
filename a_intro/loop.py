# FOR LOOP - used to iterate sequences like LIST, STRING, TUPLE and RANGES
# RANGE
for i in range(0, 5): # if 3 args are given then it will consider 3rd as stepper
    print("range is: ", i)
for i in range(0, 10, 2):
    print("Stepper jump of 2: ", i)

# LIST
countries = ["Brazil", "Russia", "India", "China", "SouthAfrica"]
for i in countries:
    print(i)

# STRING
userName = "RockRider"
for i in userName:
    print("Each character in string: ", i)

# TUPLE
trees = ("Neem", "Mango", "Apple", "Orange")
for i in trees:
    print("Tree is: ", i)

# FOR with ENUMERATE (enumerate is used with FOR-loop to access both INDEX and KEY(in terms of DICT) or VALUE in terms of LIST/TUPLE)
personDetail = {"name": "Max", "Age": 2, "place": "Thanda",  "isAlive": True}
for i,j in enumerate(personDetail):
    print("INDEX is: ", i , "KEY is: ", j)

for i,j in enumerate(countries):
    print("INDEX: ", i , "KEY: ", j)

# NESTED FOR LOOP
for i in range(1,5):
    for j in range(1, 5): # for each i iteration this will run 4 times, every-time j will start from 1 till 4
        print("i is: ", i , "j is: ", j)

for i in range(1,5):
    for j in range(i, 5): # for each i iteration this will run 4 times, every-time j will be incremented and start from i(which is 1,2,3) till 4
        print("i is: ", i , "j is: ", j)

# using FOR LOOP - MAPPING SEQUENCE
students = ["Emma", "Daniel"]
subjects = ["Math", "Science", "English"]
for i in students:
    for j in subjects:
        print(i, " - ", j)
print()
# using WHILE LOOP - MAPPING SEQUENCE
for i in students:
    indexValue = 0
    while indexValue < len(subjects):
        print(i, ' - ', subjects[indexValue])
        indexValue+=1

# STAR PATTERN
noOfStars = 5
for i in range(1, noOfStars+1): # outer loop should always use 2 range values or noOfStars+1
    for j in range(i): # this will stop at as per i iteration like 1 = 0,1(but not last element till 5),  2 = 0,1,2  ,3 = 0,1,2,3  ,4=0,1,2,3,4  ,5=0,1,2,3,4,5
        print("*", end=' ')
    print()


# NESTED LIST COMPREHENSION
matrixValue = [[j for j in range(3)] for i in range(3)] # SYNTAX - [[expression for item in inner_sequence] for item in outer_sequence]
print(matrixValue)


# PASS in forLoop
for i in range(1,3):
    pass # this is the placeholder used when no code needs to be executed


# WHILE LOOP - it runs until certain condition satisfies
count = 10
while count <= 3:
    count+=1
    print("py")
print("numPy") # this will run regardlessly

# INEFFICIENT USE
age = 1
while age>0:
        if(age < 18):
         print("not eligible")
         break
        else:
         print("you are eligible")
         break

# GETTING USER INPUT
''' SYNTAX
    try:
        # Code that may raise an exception
        # or
        # We can use if/else and print value
    except:
        # Runs if an exception occurs
    else:
        # Runs if no exception occurs
    finally:
        # Regardlessly runs the code no matter pass/fail
'''
while True:
    try:
        age = int(input("Enter your age: "))
        if(age < 18):
            print("not adult")
        else:
            print("18+")
        break
    except ValueError:
        print("other characters are not allowed")

# COUNT CHARACTER
zeroLength = 0
nameLength = "Rani"
while zeroLength < len(nameLength):
    # if(nameLength[zeroLength]):
        print(nameLength[zeroLength])
        zeroLength+=1
else:
    print("Loop completed!")