# SET
s = {10, 50, 20}
print(s)
print(type(s))

# SET - type-casting
s = set(["a", "b", "c"]) # set() method is used to convert other data types, such as lists or tuples, into sets.
print(s)
# below will throw error - values of set cannot be changed
#s[1] = "Hello" # ERROR

# HETEROGENEOUS SET
s = {"Geeks", "for", 10, 52.7, True}
print(s)

# SET and FROZENSET
s = set(["a", "b", "c"])
print("Normal Set:", s)

fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs)



# METHODS OF SET (add, union, intersect, difference, clear)
# ADD
s = {"a", "b", "c"}
s.add("d")
print(s)

# UNION
a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
print(u)

# INTERSECTION
a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(i)

# DIFFERENCE
a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d)

# CLEAR
s = {1, 2, 3}
s.clear()
print(s)