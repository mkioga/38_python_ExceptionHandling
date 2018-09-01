
# ===============================================
# EXCEPTIONS
# ===============================================

# There are two types of errors that we can get
# (1) Syntax errors
# (2) Exceptions

# Syntax errors:
# are where we make a mistake in the code
# In this case, we type x = 8 = 5 instead of x = 8 - 5, we get "SyntaxError: can't assign to literal"
# We can fix these errors so its valid code and the program will run

# x = 8 = 5


# Exception errors:
# When our program is running, we may get other errors from flaws in the codes logic or conditions that we could not predict.
# For example we may try to create a new database but there is no space in the drive that we specify
# These are exception errors and if you don't handle them when they occur, the program crashes.
# Example if we try to divide by zero, we get Exception error "ZeroDivisionError: division by zero"

# y = 2 / 0

# If we don't "handle" an exception, it is called an "unhandled exception" and execution of the program stops
# Python then prints out the details of the exception and shows line where the exception occured
# in "ZeroDivisionError: division by zero", ZeroDivisionError is the exception name and the rest are its details

# For a list of all inbuilt exceptions, check this link
# https://docs.python.org/3/library/exceptions.html

# We can look at an example of RecursionError exception which has this definition:
# This exception is derived from RuntimeError. It is raised when the interpreter detects that the maximum
# recursion depth (see sys.getrecursionlimit()) is exceeded.


# We previously looked at recursive functions to generate factorials (Search python notes)
# NOTE: Factorial 4 = 1x2x3x4 = 24
# if we try to run the factorial code with large numbers say over 1000, the stack overflows (no memory) and you end up with a recursion error
# Here the factorial of 1000 produces error "RecursionError: maximum recursion depth exceeded in comparison" and crashes program

def factorial(n):
    """ n! can also be defined as n * (n-1)! """
    """ Calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial 2 = {}".format(factorial(2)))
print("Factorial 3 = {}".format(factorial(3)))
print("Factorial 4 = {}".format(factorial(4)))
print("Factorial 900 = {}".format(factorial(900)))
print("Factorial 1000 = {}".format(factorial(1000)))

print("="*30)

# We can prevent above program from crashing using "try/except" clause
# Note that if we have a large number that creates an exception, it will run the line under except:
# Once the try/except clause finishes, program does not crash and it will continue to the other print line (program terminating)

# Exception handling is a very useful feature. It can prevent your code from crashing if something unexpected happens
# in many situations, it can allow the program to recover from whatever was causing the error


def factorial(n):
    """ n! can also be defined as n * (n-1)! """
    """ Calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

try:
    print("Factorial 1000 = {}".format(factorial(1000)))
except RecursionError:  # here we explicitly say we are expecting a RecursionError. although sometimes you don't have to
    print("This program cannot calculate factorials that large")

print("Program terminating")

print("="*30)

# =======================================
# How to handle more than one exception
# =======================================

# Here we specified that we are expecting "RecursionError" and it checks for that
# However if we introduce a "ZerodivisionError", the program will crash because we have only handled RecursionError
# We can handle more than one exception errors by adding another except, in this case, add except ZeroDivisionError

# NOTE that if the program hits one exception, it loops out and does not check the next
# in this case, since it encounters print(n / 0) first, it raises ZeroDivisionError exception and does not go to next
# factorial exception

def factorial(n):
    """ n! can also be defined as n * (n-1)! """
    """ Calculates n! recursively """
    if n <= 1:
        return 1
    else:
        print(n / 0)  # Here we introduce ZeroDivisionError by trying to print n/0. Result gives ZeroDivisionError:
        return n * factorial(n-1)

try:
    print("Factorial 1000 = {}".format(factorial(1000)))
except RecursionError:  # here we explicitly say we are expecting a RecursionError. although sometimes you don't have to
    print("This program cannot calculate factorials that large")
except ZeroDivisionError:  # we add this ZeroDivisionError exception and program will now work
    print("You cannot divide by Zero")

print("Program terminating")

print("="*30)


# ===============================================
# Handling more than one exception in one line
# ===============================================

# In above code, we wrote two except lines. one for RecursionError and other for ZeroDivisionError
# We can write multiple exceptions in one line by enclosing them in ( )


def factorial(n):
    """ n! can also be defined as n * (n-1)! """
    """ Calculates n! recursively """
    if n <= 1:
        return 1
    else:
        print(n / 0)  # Here we introduce ZeroDivisionError by trying to print n/0. Result gives ZeroDivisionError:
        return n * factorial(n-1)

try:
    print("Factorial 1000 = {}".format(factorial(1000)))
except (RecursionError, ZeroDivisionError):         # We put both exceptions here
    print("Cannot calculate factorials that large, or Cannot divide by Zero")

print("Program terminating")

print("="*30)


# ======================================================================

# Refer to documentation to read about the exceptions you may want to handle
# # https://docs.python.org/3/library/exceptions.html

# Example is OverflowError
# Raised when the result of an arithmetic operation is too large to be represented
# Python can handle very large integers, so OverflowError handling is usually not needed.

# =========================================================================



# ==============================
# Challenge
# ==============================

# Create a new python file and write a short program to ask the user to type in two integer numbers
# then print out their first number divided by the second.

# The program should not crash no matter what the user types in (don't worry about typing Ctrl keys)
# Hint: if you have to do the same thing more than once, that sounds like a good use for a function
# NOTE: you get the error type by running the error and seeing what error name python provides

# we use function getint() to get the numbers
# It will loop until you give it valid integers and then return number


def getint():
    while True:  # makes sure you input a number
        try:
            number = int(input("Prompt1: Please Enter a Number "))
            return number
        except ValueError:
            print("Invalid number entered. Please try again")

# Now we call above command twice to get the numbers.

number1 = getint()
number2 = getint()

# Now we calculate and print the division while checking for ZeroDivisionError

try:
    print("{} divide by {} = {}".format(number1, number2, number1/number2))
except ZeroDivisionError:
    print("You cannot divide by Zero")

print("="*30)




# ====================================
# Using prompt
# ====================================

# you can add "prompt" as an argument for getint() and then pass it a prompt that you want

def getint(prompt):  # add prompt as argument
    while True:  # makes sure you input a number
        try:
            number = int(input(prompt)) # Prompt that will be shown to user
            return number
        except ValueError:
            print("Invalid number entered. Please try again")

# Now we call above command twice to get the numbers.

number1 = getint("Prompt2: Please Enter Number_1: ")  # We provide the prompt for each call to getint(prompt)
number2 = getint("Prompt2: Please Enter Number_2: ")

# Now we calculate and print the division while checking for ZeroDivisionError

try:
    print("{} divide by {} = {}".format(number1, number2, number1/number2))
except ZeroDivisionError:
    print("You cannot divide by Zero")

print("="*30)

# NOTE that there are ways to crash this program
# if you type "Ctrl + D" you get End of file error message "EOFError: EOF when reading a line"



# =======================================
# Using sys module to handle EOFError:
# ======================================

# As we saw above, if you enter "Ctrl+D", it will crash and give you "EOFError: EOF when reading a line" error message
# We can handle this using "sys" module
# We add "except EOFError" and then "sys.exit(0)". The 0 here will show you which exit code the programs exits from
# For example, if we run code, and type Ctrl+D, it gives message "Process finished with exit code 0"
# This indicates it exited the program on sys.exit(0). If we add sys.exit(1), it will give "Process finished with exit code 1"

# First we need to import sys
import sys

def getint(prompt):  # add prompt as argument
    while True:  # makes sure you input a number
        try:
            number = int(input(prompt)) # Prompt that will be shown to user
            return number
        except ValueError:
            print("Invalid number entered. Please try again")
        except EOFError:
            sys.exit(0)  # This exits the program. We add 0 it indicates that it exits program with exit code 0

# Now we call above command twice to get the numbers.

number1 = getint("Prompt2: Please Enter Number_1: ")  # We provide the prompt for each call to getint(prompt)
number2 = getint("Prompt2: Please Enter Number_2: ")

# Now we calculate and print the division while checking for ZeroDivisionError

try:
    print("{} divide by {} = {}".format(number1, number2, number1/number2))
except ZeroDivisionError:
    print("You cannot divide by Zero")
    sys.exit(2)   # Add this to show exit code 2 if we try to divide by 0

print("="*30)




# =======================================
# ELSE clause and FINALLY clause
# ======================================

# There are two other clauses that we can add to a "try" statement i.e. "else" and "finally"

# =================
# Finally clause:
# =================
# "finally clause" is the one that will always be executed whether the program runs or whether it catches an exception
# One use for finally clause is to terminate database connections, closing open files etc after program ends

# NOTE that finally clause must come after all your except clauses.
# NOTE that finally clause executes whether you put valid of invalid numbers, even entering Ctrl+D

# =================
# Else clause:
# =================
# else clause is executed if the code does Not raise an exception when used in the try statement.
# Else clause must also come after all except clauses but before any finally clause if you got one.
# we will add an else clause after ZeroDivisionError in this case.

# else is intended so that we don't accidentally catch an exception that was not raised by the code we are trying
# to protect the try block
# For example in bank transactions, if we are protecting the updating of two transactions using a try block
# you only want the code to roll back if there was an error during the saving of values to the two accounts
# But if we add more code inside the try block and that code raises an exception, then the transactions will
# be rolled back even if they completed successfully.


# ==================================================
# Exceptions superclass/subclass and their order
# =================================================

# Exceptions are objects and in python 3, exceptions must be derived from the BaseException class or one of its subclasses
# https://docs.python.org/3/library/exceptions.html - shows that
# "In Python, all exceptions must be instances of a class that derives from BaseException."

# if you click on ValueError below, it will open builtins showing it is derived from Exception
# class ValueError(Exception):
# Hence everything that ValueError can catch can be caught by Exception because it is derived from it
# if you replace "except ValueError:" with "except Exception:", it will still catch invalid code.
# It is however recommended to be specific in the Exceptions you catch instead of catching everything
# one reason for this is because you can handle (fix/resolve) different exceptions differently and hence if you catch all of them
# it will be difficult to handle them

# Another issue in catching all exceptions is because if you use Exception instead of ValueError,
# Then Exception will catch all errors including EOFError below it. because EOFError is a subclass of Exceptions.
# So if you run this code with both Exception and EOFError and then input Ctrl+D, there will be a loop failure
# Because the code that runs when EOFError is raised, is the code on this line: "print("Invalid number entered. Please try again")"
# Hence the program does not exist and it just prints a message and loops because the input stream is closed and we keep getting
# these EOFError raised by this line "number = int(input(prompt))"

# Exceptions order:
# So it is important that the more specific exceptions have to appear first
# So in this case, you should put "exception EOFError" before "exception Exception"

# ===============================
# Catching all exceptions
# ===============================
# if you want to catch all exceptions, just use the keyword except: and don't put any keyword after it.
# This will catch all possible exceptions



# First we need to import sys
import sys

def getint(prompt):  # add prompt as argument
    while True:  # makes sure you input a number
        try:
            number = int(input(prompt)) # Prompt that will be shown to user
            return number
        except ValueError:  # ValueError exception is Derived from Exception. replace with Exception and it will still work. not recommended
            print("Invalid number entered. Please try again")
        except EOFError:
            sys.exit(0)  # This exits the program. We add 0 it indicates that it exits program with exit code 0
        finally:         # NOTE that finally clause must come after all your except clauses
            print("Finally clause always executes whether program runs or raises exception")

# Now we call above command twice to get the numbers.

number1 = getint("Prompt2: Please Enter Number_1: ")  # We provide the prompt for each call to getint(prompt)
number2 = getint("Prompt2: Please Enter Number_2: ")

# Now we calculate and print the division while checking for ZeroDivisionError

try:
    print("{} divide by {} = {}".format(number1, number2, number1/number2))
except ZeroDivisionError:
    print("You cannot divide by Zero")
    sys.exit(2)   # Add this to show exit code 2 if we try to divide by 0
else:             # We add else clause after all except statements, but before finally if finally exists.
    print("Else clause runs because division was performed successfully")

