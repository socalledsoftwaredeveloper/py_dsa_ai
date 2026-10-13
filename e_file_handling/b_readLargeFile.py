# Reading a File Line by Line - It can be done in 2 ways 1. using forIn and strip(), 2nd is using while loop

# INEFFICIENT way for reading large file
openFile = open('largeEssay.txt', 'r')
readFile = openFile.read()
print(readFile)
openFile.close()

# FOR IN and STRIP() - Efficient way 1 for both SMALL and LARGE FILE
def usingForStrip():
    openFile = open('largeEssay.txt', 'r')
    for line in openFile: # Iterates over each line in the file.
        print(line.strip()) # Removes any leading/trailing whitespace, including newline characters.
    openFile.close()
usingForStrip() # function call

# Efficient way 2 - using WHILE LOOP and STRIP
def usingWhileStrip():
    openFile = open('largeEssay.txt', 'r')
    line = openFile.readline() # this readline() reads 1 line at a time
    while line: # this loop check keeps on until no lines are left
        print(line.strip())
        line = openFile.readline()
    openFile.close()
