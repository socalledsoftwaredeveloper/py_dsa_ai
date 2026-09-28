# LIST
a = [1, "Hello", [3.14, "world"]]
a.append(2)  # Add an integer to the end
print(a)



# NUMPY
import numpy as np
a = np.array([1,2,3]) #single array
print(a*2)

res = np.array([[1, 2], [3, 4]]) # Multi-dimensional array
print(res * 2)



# Array usage with list
import array as arr
arrData = arr.array('i', [2,3,4]) # NOTE: List are require a typecode during initialization to define the data type


# accessing first array
print(arrData[0])


# adding element to array
arrData.append(5)
print(arrData)



# Creating the array
import array as arr
arrayData = arr.array("i", [12,13,14])
for i in range(0, 3):
    print(arrayData[i], end=" ")


# Adding the element in array
print(*arrayData)
arrayData.insert(1, 4)  # Insert 4 at index 1
print(*arrayData)


# Accessing the array
print(arrayData[0])
print(arrayData[3])

b = arr.array('d', [2.5, 3.2, 3.3]) # decimal 'd' FLOAT required 8 byte of memory
print(b[1])
print(b[2])


# Searching the element
import array
arrValues = array.array('i', [1, 2, 3, 1, 2, 5])
print(arrValues.index(2)) # index of 1st occurrence of 2
print(arrValues.index(1)) # index of 1st occurrence of 1


# updating the array
import array
vals = array.array('i', [1, 2, 3, 1, 2, 5])
vals[2] = 6 # update item at index 2
print(vals)
vals[4] = 8 # update item at index 4
print(vals)



# Array operations (count, reverse, extend)
# count
import array
nums = array.array('i', [1, 2, 3, 4, 2, 5, 2])
count = nums.count(2)
print(count)


# reverse
nums.reverse()
print(*nums)


# extend
someMoreData = [6,7,8]
nums.extend(someMoreData)
print("extendedArrData: ", nums)
