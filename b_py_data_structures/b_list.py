a = [1, 2, "Python", 3.3, "a"] # we can have any no.of data with any types
print(a[0])   # index-based
print(a)



# ADDING (APPEND - 1 element can be added, insert - INSERT 1element at specific index position, EXTEND - add multiple elements)
# APPEND - 1 element can be added
b = [12,13]
b.append(14) # adding > 1 element will throw error
print(b)
# INSERT - insert 1element at specific index position
c = [4,5]
c.insert(1, 6) # adding > 1 element will throw error
print(c)
# EXTEND - add multiple elements at last
d = ["a","b"]
d.extend(["c", 1, 2.2, "max"])
print(d)
# UPDATING

# REMOVING (REMOVE - removes 1st occurrence from the list, POP - remove item at specific position, if index is not specified then, it removes the last element by default, DEL keyword - removes index based item from the list)
# REMOVE
e = [14,15,16]
e.remove(15) # if the value is not present then, will throw error
print(e)
# POP
f = [7, 8, 9, 10, 11]
f.pop() # removes last element since no index is specified
print(f)
f.pop(1) # removes specific index item from the list
print(f)
# DEL keyword
g = [9,3,6,7]
del g[-1] # remove's last item from the list
print(g)