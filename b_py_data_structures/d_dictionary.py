# DICTIONARY - {key:value}
data = { "name": "Jake", "age": 22 }
print(data)

nested_data = {"name":"max", "address": {"country": "india", "state_details": {"state": "tamil_nadu", "district":"salem"}}, "age":12}
print(nested_data)



# DICTIONARY CREATION - 2 ways (like above and using dict keyword)
foods = {"veg":"carrot", "non-veg": "fish", "snacks": "chips"}
instrument = dict(western = "violin", karnatic = "flute")
print(foods)
print(instrument)



# Accessing DICT and getting values (2 ways; 1.array [] and 2. using "get" keyword)
food = {"veg":"carrot", "non-veg": "fish", "snacks": "chips"}
print(food["veg"])
print(food.get("non-veg"))

# ADD and UPDATE dict
d = {"name": "Sam"}
d["age"] = 21        # Adding a new key-value pair
d["name"] = "Alex"   # Updating an existing value
print(d)

# REMOVING dict items (del keyword, pop(), popitem(), clear())
e = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7}
print(e)
del e["a"] # deletes particular key value
print(e)

# POP - deletes given key and its value
e.pop("b") # deletes particular key value
print(e)

# POPITEM - deletes last key value pair
e.popitem()
print(e)

# CLEAR - it clears the entire dicts and make thm as empty object like -> {}
e.clear()
print(e)



# ITERATING DICT - using for loop
fav_food = {"veg":"carrot", "non-veg": "fish", "snacks": "chips"}
for key in fav_food: # ITERATING KEY
    print("it's key is: ",key)
    # print("value is: ",fav_food[key], "it's key is: ",key) # iterating both key, value

for value in fav_food.values(): # ITERATING VALUE - don't forget to give DICT.values()
    print("it's value: ",value)

for key,value in fav_food.items(): # ITERATING VALUE - don't forget to give DICT.values()
    print("its key and value are: ",key , value)



# NESTED DICT
studentData = {
    "student": {
        "name": "Sam",
        "age": 20
    }
}

print(studentData)
print(studentData["student"])
print(studentData["student"]["name"])