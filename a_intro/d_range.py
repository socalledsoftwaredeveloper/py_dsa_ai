for i in range(1,5):
    for j in range(1, 5):
        print("i is: ", i , "j is: ", j)

print("------")

for i in range(1,5):
    for j in range(i, 5):
        print("i is: ", i , "j is: ", j)

print("------")

for i in range(2, 3):
    for j in range(1, 6):
        print(i, "*", j, "=", i*j)

print("------")

# using FOR LOOP
students = ["Emma", "Daniel"]
subjects = ["Math", "Science", "English"]
for i in students:
    for j in subjects:
        print(i, " - ", j)
print()
# using WHILE LOOP
for i in students:
    indexValue = 0
    while indexValue < len(subjects):
        print(i, ' - ', subjects[indexValue])
        indexValue+=1

print("------")

noOfStars = 5
for i in range(1, noOfStars+1): # outer loop should always use 2 range values or noOfStars+1
    for j in range(i): # this will stop at as per i iteration like 1 = 0,1(but not last element till 5),  2 = 0,1,2  ,3 = 0,1,2,3  ,4=0,1,2,3,4  ,5=0,1,2,3,4,5
        print("*", end=' ')
    print()

for i in range(3):
    print(i)