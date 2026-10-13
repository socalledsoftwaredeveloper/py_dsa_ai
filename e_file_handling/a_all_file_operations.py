# OPEN A FILE
openFile = open("python.txt", "r") # if a file is not present then py will raise a an exception
print(openFile) # this will give a wrapperText and not teh actual content in it, for displaying the details we have to make a read operation
readFile = openFile.read()
print(readFile)
openFile.close() # always close once read/done with any operations to free up the resource

# USING TRY/EXCEPT to handle errors
try:
    openFile = open("python.txt", "r") # if a file is not present then py will raise a an exception
    print(openFile) # this will give a wrapperText and not teh actual content in it, for displaying the details we have to make a read operation
    readFile = openFile.read()
    print(readFile)
    openFile.close() # always close once read/done with any operations to free up the resource
except FileNotFoundError as e:
    print(f"Error occurred: FILE NOT FOUND")



# CHECKING FILE PROPERTIES FOR OPENED FILE
f = open("python.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed) # boolean value

f.close()
print("Is Closed?", f.closed)



# OPEN, WRITE, APPEND, READ and CLOSE OPERATIONS
def doOperations():
    open_Or_Create_File = open('python3.txt', 'x') # Creates a new file and raises an error if it already exists
    print('File created successfully!')
    open_Or_Create_File.write('Ranjan is learning file handling')
    print('File written successfully')
    open_Or_Create_File.close() # Always close the file immediately once if open/read/write and don't close at the end because we would get unexpected result while printing and increase in memory usage

    appendText = open('python3.txt', 'a')
    appendText.write("\nRanjan is an AI Engineer")
    print("File appended successfully")
    appendText.close() # Always close the file immediately once if open/read/write and don't close at the end because we would get unexpected result while printing and increase in memory usage

    openToReadFile = open('python3.txt', 'r')
    readFile = openToReadFile.read()
    print(readFile)
    print("File read completed")
    openToReadFile.close()
    print("File closed")

try:
    doOperations() # calling the function
except FileExistsError as e:
    print(e)