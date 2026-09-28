# STRING - anything with-in single/double quotes are considered as STRING. it has a length to read no.of characters
"""
    1. For single line string we use ""/''
    2. For multiline string we use ''''''/""""""""
"""
singleLineStr = "Max"
multiLineStr = '''Hello
world,
I am Godzilla'''
print("singleLineStr: ", singleLineStr)
print("multiLineStr: ", multiLineStr)
print("indexAccess: ", singleLineStr[0], singleLineStr[-1]) # -1 is last letter because, - always reads letter from last. We can also give -> singleLetter[len(singleLetter)-1]
print("indexAccess last letter: ", singleLineStr[len(singleLineStr)-1])



# SLICE a string
userName = "NissanGTR-R35"
print(userName[0:9]) # from 0 to 8th position, will exclude 9th
print(userName[:]) # complete
print(userName[1:4]) # 1st to 3rd, will exclude 4th
print(userName[:3]) # 0th till 2nd, exclude 3rd
print(userName[2:]) # from 2nd till last
print(userName[::-1]) # from reverse till first



# DELETE a string
userAge = 11
print("before deleting userAge: ", userAge)
del userAge
# print("Will throw error since userAge is already deleted: ", userAge)



# UPDATING A STRING
userAddress = "123/H"
alter_Address_1 = "Venue Block " + userAddress[:4] + "J"
alter_Address_2 = userAddress.replace("123", "456")
print(userAddress)
print(alter_Address_1)
print(alter_Address_2)



# String methods [NOTE: most of this are same as JS so I didn't mention everything here]
programmingLanguage = "Python"
print(programmingLanguage.split()) # keeps in array with 1 word of string