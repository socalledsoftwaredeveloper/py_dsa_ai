# "def" - function in python - this is mostly same as func in other programming languages

def canAddNums(a,b,c=3): # passing as args
    result = a+b+c
    print("result of this function canAddNums: ", result)
    return result # if return is not provided then it by default returns "none"
canAddNums(3, 3, 6) # calling the function with supported args. If no.of args has not passed then will throw error unless even if we not given default params
canAddNums(3, 3) # calling without 3rd args since default params are already provided



# KEYWORD ARGS - WHILE PASSING LIKE THIS THE ORDER DOESN'T MATTER
def getFullName(firstName, lastName):
    result = firstName+lastName
    print("fullName is: ", result)
    return result
getFullName(firstName="Green ", lastName="Grass")
getFullName(lastName="Carpet", firstName="Red ") # order changed but doesn't matter because we pass keyword and order be taken care by function "getFullName"



# Arbitrary Arguments - It allow functions to accept multiple values. This is done using two special symbols: (*args, **args)
    # *args -> collects extra positional arguments as a tuple
    # **args -> collects extra positional arguments as a dict
def getFavBooks(*bookName, **author):
    getListOfBooks = []
    for i in bookName:
        getListOfBooks.append(i)

    print(getListOfBooks)
    getBookWithAuthorDetails = []
    for key,value in author.items():
        getBookWithAuthorDetails.append({key:value})
        print(key, ":", value)
    print(getBookWithAuthorDetails)

getFavBooks("Eat that frog", "Ikigai", thiruvalluvar="Thirukurral", avvayar="Aathichudi")



# FUNCTION WITHIN FUNCTION
# func1(3) # This will not work like JS func is not hoisted. First define the function with proper definition and then call
def func1(a):
    resultOfA = a #6
    print("resultOfA: ", resultOfA)
    def func2(b):
        resultOfB = a+b #6+6 = 12
        print("resultOfB: ", resultOfB)
    func2(resultOfA)
func1(6)

# We have some RULES to be known for INNER FUNCTION
 # 1. Scope of variables in inner functions - Inner functions follow Python’s LEGB rule (Local --> Enclosing --> Global --> Built-in). They can access outer function variables, but modifying them requires special keywords like nonlocal.

 # Non modified data
def fun1(): 
    msg = "Geeks for geeks"
    def fun2(): 
        print(msg) 
    fun2()
fun1()

 # modified lexical data using keyword "nonlocal"
def fun1(): 
    a = 45
    def fun2(): 
        nonlocal a # modify lexical variable
        a=54
        print(a) # CLOSURE - A function + the variables from its surrounding scope that it remembers.
    fun2()
    print(a)
fun1()

"""
 Explanation: fun1() creates a local variable msg and defines fun2(), which prints msg. Because of lexical scoping, fun2() can access msg from fun1() and calling fun1() runs fun2() and prints the message.

Example 2: This example shows how the nonlocal keyword allows the inner function to modify a variable from the outer function instead of creating a new local copy.
"""

# CLOSURE - A function + the variables from its surrounding scope that it remembers.
def fun1(a):  
    def fun2():
        print(a)  
    return fun2 

closure_func = fun1("Hello, Closure!") # func1 called and executes and it returns the whole function but, with below call instead of returning whole function we are calling it to execute and do it's operation
closure_func()