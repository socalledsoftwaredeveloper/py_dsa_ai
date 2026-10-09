# Class
class Dog:
    name = "max"
    place = "salem"
    age = 2

karupu = Dog() # creating object from the class blueprint
print(karupu.name)



# Class with constructor and str(to print message)
class Cat:
    country = "India" # common class attribute
    def __init__(self, name,age,place): # constructor and here is where CLASS is being initiated
        # self - it refers to the current object and it is just like "this" in JS and here it should always be the first param value
        self.name = name # instance attribute
        self.age = age # instance attribute
        self.place = place # instance attribute

    def __str__(self): # __str__ used to print readable name instead of showing garbage/address values
        return f"{self.name} is my cat and he is {self.age} years old, I bought from {self.place}"

cat1 = Cat("saambal", 12, "kovai") # object creation - reusing from class template Cat
cat2 = Cat("karupuVellai", 3, "salem") # object creation - reusing from class template Cat
print(cat1)
print(cat2)



# SELF - it can be of any name and it is same like "this" in JS. It should always be called as 1st params
class Human:
    age = 18
    def __init__(self, hairColor, skinColor, eyeColor):
        self.hairColor = hairColor
        self.skinColor = skinColor
        self.eyeColor = eyeColor

    def describeHuman(self): # NOTE: All methods must have self as the first parameter.
        return f"I saw the human with {self.skinColor} skin color, {self.eyeColor} eye color and {self.hairColor} hair color"

    def greetHuman(self):
        getHuman = self.describeHuman() # calling other method using SELF
        return f"Good Morning all, {getHuman} and seems to be {self.age} plus"
        
human1 = Human("black", "brown", "blue")
print(human1.greetHuman())



# Create multiple method in class
class SongList:
    def __init__(self, name):
        self.name = name
        self.songs = []
    #add
    def addSong(self, newSong):
        self.songs.append(newSong)
        print("new song added")
    #list
    def listSongs(self):
        for song in self.songs:
            print(f"play list: {song}")
        
    #delete - this is 2 step, the better approach is in line 72
    def removeSong(self, removeThisSong):
        for remove_a_Song in self.songs:
            if remove_a_Song == removeThisSong:
                self.songs.remove(removeThisSong)
                print("song removed")

    # delete song - better approach
    def removeSong(self, removeThisSong):
        if removeThisSong in self.songs:
                self.songs.remove(removeThisSong)
                print("song removed efficiently")

song1 = SongList("Jananayagan")
song1.addSong("oru peairea varalaru")
song1.addSong("kannea maniyea")
song1.addSong("thalapathi kacheri")
song1.addSong("vetai karupu")

print(song1.listSongs())
song1.removeSong("vetai karupu")
print(song1.listSongs())
