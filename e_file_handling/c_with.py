# WITH: This doesn't need a manual close, it would get closed automatically
# OPEN, READ and CLOSE AUTOMATICALLY using WITH
with open('python3.txt', 'r') as withFile:
    content = withFile.read() # reads entire content
    print(content) # File closes automatically



# OPEN, WRITE and CLOSE AUTOMATICALLY using WITH
with open('python3.txt', 'w') as withWriteFile: # NOTE:  Here it replacing any existing content not appending
    content = withWriteFile.write("\nRanjan is a BEAST") # reads entire content
    print(content) # File closes automatically



# Efficient way for both SMALL and LARGE FILE
with open('python3.txt', 'r') as withAFile:
    for line in withAFile: # read line by line
        print(line.strip()) # File closes automatically



# CUSTOM CONTEXT MANAGER using WITH - The "with" relies on context manager where it provides allocation and de-allocation using 2 special methods (__enter__ and __exit__)
class FileManager():
    def __init__(self, fileName, mode): # it initializes fileName and mode
        self.fileName = fileName
        self.mode = mode

    def __enter__(self): # __enter__ -> opens the file and returns it
        self.file = open(self.fileName, self.mode)
        return self.file

    def __exit__(self, exc_type, exc, tb): # __exit__ -> release the resource and close/exit
        self.file.close() # once file got written, it closes

with FileManager('python3.txt', 'w') as file:
    file.write("Ranjan is making a progressive move")



# contextlib module
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

# Using the generator-based context manager
with open_file('example.txt', 'w') as file:
    file.write('Hello, World!')



# TRY, EXCEPT, ELSEm and FINALLY
def createWithFile():
    try:
        with open('python3.txt', 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Unable to find the file")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("file written successfully!")
    finally:
        print("File execution completed.")

createWithFile() # function call



# readLines() and writeLines()
# READLINES - read all lines from file and store it in list
L = ["Geeks\n", "for\n", "Geeks\n"]

file1 = open('myfile.txt', 'w')
file1.writelines(L) # read all lines from file and store it in list
file1.close()

file1 = open('myfile.txt', 'r')
Lines = file1.readlines()

count = 0
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

# WRITELINES - writes a list of iterable item into the file
L = ["Master\n", "Of\n", "Minds\n"]
with open("python3.txt", "w") as file:
    file.writelines(L) # writes a list of iterable item into the file

count = 0
with open("python3.txt", "r") as file:
    for line in file:
        count += 1
        print("Line{}: {}".format(count, line.strip()))

# Using LOOP
L = ["Winter\n", "Is\n", "Coming\n"]

file1 = open('python3.txt', 'w')
file1.writelines(L) # writes a list of iterable item into the file
file1.close()

file1 = open('python3.txt', 'r')
count = 0

for line in file1:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

file1.close()