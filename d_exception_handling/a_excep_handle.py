# Exception Handle - simple example
def checkDivisibility(args):
    try:
        res = 10/args
    except ZeroDivisionError:
        print("provided number can't be divided")
    except TypeError:
        print("You have not entered proper number type")
    else:
        print("result of division: ", int(res))
        return f"Result is: {res}"
    finally:
        print("Math operation")

checkDivisibility(2)
checkDivisibility(0)
checkDivisibility("4")



# CATCHING EXCEPTIONS
# 1. Specific Exception - Single Exception Handling
try:
    vals = "str" # In case the value is given as 0 then we would get ZeroDivision error
    res = 10/vals
except TypeError:
    print(f"Please enter a valid type to make division: {vals} is not correct type to divide 10")
except ZeroDivisionError:
    print(f"Unable to divide string type with number type")



# 2. Multiple Exception handling
# NOTE: We can catch multiple exceptions in a single block if we need to handle them in the same way or we can separate them if different types of exceptions require different handling.
listValues = [10, "Eleven", 12]
try:
    res = listValues[0] + listValues[1]
except (TypeError, ValueError) as e:
    print("Error: ", e)
except IndexError: # This exception would get occur if the list index is out of range
    print("Range Error")  
else:
    print(f"Result is: {res}")



# 3. Catch-All handlers - Use safely because we might not known what as the exact reason. Use as a final net to catch
try:
    res = "50"/2
except ArithmeticError:
    print("Arithmetic Error")
except: # NOTE: Use it wisely, still this would not give exact error and this debugging is harder
    print("Something went wrong!!!")



# 4. RAISE - Custom Exception
def checkEligible(age):
    # print("Eligible to VOTE") if age>=18 else ValueError("Person is minor, below 18")
    if age < 18:
        raise ValueError("Person is minor, below 18")
    print("Eligible to VOTE")

try:
    checkEligible(17)
except ValueError as e:
    print("Error: ", e)



# CUSTOM EXCEPTION
class CustomException(Exception): # inherit the base Exception from py library
    def __init__(self, message, errCode):
        super().__init__(message) # passes the message to the base exception class.
        self.message = message
        self.errCode = errCode
    def __str__(self): # message to print the err
        return(f"{self.message}, Error Code: {self.errCode}")

err = CustomException("User is unauthorized", 403)
print(err)

# RAISING CUSTOM EXCEPTION - make sure the name should be same
class MyCustomException(Exception): 
    pass
def divideNow(a,b):
    if b == 0:
        raise MyCustomException(f"can't divide {b} with {a}")
    print(f"Result is: {a/b}")
    return a/b

try:
    divideNow(4, 0) # try changing the b value and see the terminal output
except MyCustomException as e:
    print(e)
    