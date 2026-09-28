# TUPLE CREATION
tup = ("a","b", 1, 2.2) # we can have any mixed data types
print(tup)
# Using String
tup = ('ant', 'spider')
print(tup)
# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))
# Using Built-in Function
tup = tuple('Max') # this creates tuple as a single items as "m", "a", "x" and we can't have any other mixed data types when using BUILT-IN function, if we introduce then it will throw error
print(tup)

# CONCATENATING TUPLE
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup1 + tup2
print(tup3)

# SLICING THE TUPLE
tup = tuple('GEEKSFORGEEKS')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])

# UNPACKING WITH "*"
tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a) 
print(b) 
print(c)

# DELETING A TUPLE
tup = (0, 1, 2, 3, 4)
del tup
print(tup) # this will throw error since we deleted