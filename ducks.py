
# ============
# ducks.py
# ============

# ===================================================
# Raising Exceptions
# ===================================================

# In the previous section, we looked at how to catch exceptions and handle them using the "try" and "except" statements.
# We also looked at how to use "finally" to make sure we can run cleanup code even if an exception is raised.
# We also saw another use of "else" keyword to execute code if an exception is not raised.

# Handling exception is important to make sure your code does not crash.
# But what happens if your code cannot handle the exception.
# If your module relies on a filename that is being provided by the user, they may have entered invalid volume.
# your module may be called by another code that requested the filename, so you cannot just pick a random location
# on the computer to write your data to.
# So in that case, there is not a lot that your code can do about the exception.
# you may be tempted to ask the user for another filename, but if your code is running on a remote server, or windows
# service, no one will see your prompt and your program will sit there waiting for input that never comes.

# In that case, there are two actions that your can take.
# (1) Do nothing - this can actually be the best approach and there is nothing wrong with ignoring exceptions that you cannot handle

# (2) Raise an exception to let the calling code know that something has gone wrong.
# We will use the duck class to demonstrate this.
# We will use our duck class in a demo program to model duck migration.

# we will add another class called "Flock"  right after the "penguin" class


class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()

# user this Penguin class until CHANGE_6
# At CHANGE_7, use the other Penguin class that has aviate method

class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")

# ============================
# Testing exception handlers
# ============================

# CHANGE_7
# The other reason you may want to raise exceptions is so that you can test your exception handlers.
# We will update the code with CHANGE_7 so that penguin1 has a flying method

# We give Penguin an aviate method
# When you run the program in migration.py, you will see that penguin1 can now fly and it prints
# the message "This new Penguin is now able to fly" and there is no exception error

# In this code, we have created a new __init__ data attribute called "fly" and we assign it to a reference to "aviate" method
# Note we don't include () after aviate, so without (), we are just adding a reference to aviate method
# NOTE that everything in python is an object, even functions and methods
# So you can assign a method to a variable (self.fly) and call that variable just like you call the method
# that it points to (self.aviate)

# Now how do we test that exception handlers are working correctly.
# We can pass inappropriate arguments to the add_duck method and we see it working, but sometimes getting real exceptions is not easy.
# Simulating a disk_full exception that prevents writing data to a file is possible but hard to set up.
# Other exceptions would be if your network link goes down while you're downloading data.

# We will raise exceptions below CHANGE_7 section next to class Flock(object)



class Penguin(object):

    def __init__(self):         # CHANGE_7 - we add init to define self.fly to be self.aviate
        self.fly = self.aviate  # Note we don't include () after aviate, so without (), we are just adding a reference to aviate method

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")

    def aviate(self):           # CHANGE_7 - we add this aviate method
        print("This new Penguin is now able to fly")




# Part of CHANGE_3 below
# We create a Mallard Class which is a subclass of Duck class

class Mallard(Duck):
    pass

# we create the Flock object here.

# We will add a hint to the add_duck method of class Flock so that users can know what to add.
# Parameters are "annotated" by using a colon (:) followed by the type of parameter (Duck in this case)
# Return value ( -> ) and then type of parameter is (None in this case)
# In this example, we originally have "def add_duck(self, duck):" and then when it is annotated, it becomes
# "def add_duck(self, duck: Duck) -> None:"

# After adding this annotation, we go back to migration.py and notice that error check has noticed the annotation
# on line "flock.add_duck(penguin1)". if you hover on it, it says "Expected type "Duck" not 'Penguin'"

class Flock(object):

    def __init__(self):
        self.flock = []  # Creates empty list called flock.

    def add_duck(self, duck: Duck) -> None:  # we annotate by adding :, then type of parameter (Duck), then return value (->) then type of parameter (None)
        self.flock.append(duck)  # Adds new duck to the flock

    # =================================
    # What to do if users ignore hints
    # using " pass "
    # =================================

    # CHANGE_1 in ducks.py
    # if users ignore hints and enter penguin, we can make sure that all ducks that can fly are allowed to fly
    # and then ignore the penguin that cannot fly.
    # we do this in ducks.py under class Flock method def migrate
    # in other words, we catch the exception in the migrate method.
    # Remember if we call penguin, we get attribute error: AttributeError: 'Penguin' object has no attribute 'fly'

    # If we run this code now, with the AttributeError ignored and passed under migrate method, all the ducks that can fly will fly
    # And the penguin that cannot fly will be ignored.

    # This code ignores the penguin that cannot fly and lets other ducks fly
    # if does not notify migration.py that there is a problem with its inputs

    def migrate(self):
        for duck in self.flock:
            try:              # Check to see if ducks can fly
                duck.fly()    # causes every duck in the flock to fly by calling their fly method.
            except AttributeError:  # if there is an attributeError, we pass to the next duck
                pass



    # =================================
    # How to notify there is a problem:
    # using " raise "
    # =================================

    # CHANGE_2 in ducks.py
    # The problem here is that migration.py will not know if there is a problem and the programmer will not debug it.
    # There is a way to all the ducks that can fly still fly, but also raise an exception error to notify you
    # When we run the code now, it lets all the ducks that can fly to fly but also raises an AttibuteError for Penguin who cannot fly.

    # This code lets all ducks that can fly to fly but it also notifies migration.py that there is a problem.

class Flock(object):

    def __init__(self):
        self.flock = []  # Creates empty list called flock.

    def add_duck(self, duck: Duck) -> None:  # we annotate by adding :, then type of parameter (Duck), then return value (->) then type of parameter (None)
        self.flock.append(duck)  # Adds new duck to the flock

    def migrate(self):
        problem = None  # first we initialize problem with None.
        for duck in self.flock:
            try:              # Check to see if ducks can fly
                duck.fly()    # causes every duck in the flock to fly by calling their fly method.
            except AttributeError as e:  # attribute error is assigned to variable e
                print("This duck cannot fly")  # Notifies you there is a duck that cannot fly, indicating its probably not a duck
                problem = e  # Then the variable problem is assigned the AttributeError e
        if problem:  # if problem exist, in this case it does because we assigned it e
            raise problem   # Then we raise the problem in the main program. raise is opposite of pass.


    # =================================
    # Creating exceptions
    # =================================

    # CHANGE_3
    # We can create our own exceptions because exceptions are objects
    # We have already provided a hint that we should pass a "duck" or subclass of "duck"

    # But first we can check the type of argument that is passed under def add_duck method (CHANGE_3)
    # if we run code from migration.py, we see that all 7 ducks that can fly are allowed to fly
    # The penguin is ignored because it is not of type Duck

    # NOTE: This method of checking is wrong and non-pythonic, so you should not do it this way.
    # To see why this method does not work, we will create a "Mallard" class above which is also a duck
    # Then we run migration.py and pass it a Mallard instance called mallard1

    # If we run the code with mallard1 called, we still get only 7 ducks flying
    # program also ignores mallard1 even if it is a subclass of duck and has fly method.

    # As we can see, the "if type(duck) is Duck: " checks if type is Duck, and does excludes subclasses that may be deriving from Duck
    # and have same methods as Duck



class Flock(object):

    def __init__(self):
        self.flock = []  # Creates empty list called flock.

    def add_duck(self, duck: Duck) -> None:  # we annotate by adding :, then type of parameter (Duck), then return value (->) then type of parameter (None)
        if type(duck) is Duck:  # CHANGE_3 - we check to see if duck is of type Duck class before adding it to the flock
            self.flock.append(duck)  # Adds new duck to the flock

    def migrate(self):
        problem = None  # first we initialize problem with None.
        for duck in self.flock:
            try:              # Check to see if ducks can fly
                duck.fly()    # causes every duck in the flock to fly by calling their fly method.
            except AttributeError as e:  # attribute error is assigned to variable e
                print("This duck cannot fly")  # Notifies you there is a duck that cannot fly, indicating its probably not a duck
                problem = e  # Then the variable problem is assigned the AttributeError e
        if problem:  # if problem exist, in this case it does because we assigned it e
            raise problem   # Then we raise the problem in the main program. raise is opposite of pass.



    # ================
    # isinstance
    # ================

    # CHANGE_4
    # Since we have seen the limitations of checking type in CHANGE_3
    # There are times when you want to check type, we can use "isinstance" instead of checking "type'
    # When we run this with "isinstance" we see that "mallard1" runs fine because it is part of class Duck

    # NOTE: Keep in mind that this solution is still not pythonic
    # in python, we are not interested in whether mallard1 is a Duck, but whether mallard1 can fly

class Flock(object):

    def __init__(self):
        self.flock = []  # Creates empty list called flock.

    def add_duck(self, duck: Duck) -> None:  # we annotate by adding :, then type of parameter (Duck), then return value (->) then type of parameter (None)
        if isinstance(duck, Duck):  # CHANGE_4 - We use isinstance to check type of instance
            self.flock.append(duck)  # Adds new duck to the flock

    def migrate(self):
        problem = None  # first we initialize problem with None.
        for duck in self.flock:
            try:              # Check to see if ducks can fly
                duck.fly()    # causes every duck in the flock to fly by calling their fly method.
            except AttributeError as e:  # attribute error is assigned to variable e
                print("This duck cannot fly")  # Notifies you there is a duck that cannot fly, indicating its probably not a duck
                problem = e  # Then the variable problem is assigned the AttributeError e
        if problem:  # if problem exist, in this case it does because we assigned it e
            raise problem   # Then we raise the problem in the main program. raise is opposite of pass.




    # =============================
    # Checking if mallard can fly
    # =============================

    # CHANGE_5
    # The best way to do this is to check if mallard1 can fly and then add it to the flock.
    # we are not interested if mallard is a duck object, we are just interested in if it can fly

    # First we check to see if there is an attribute called "fly"
    # Then we check to see if "fly" is a method and not a data attribute.

    # When we run migration.py, we see that mallard1 flies but penguin1 does not fly
    # This is because mallard1 has fly method while penguin1 does not.


class Flock(object):

    def __init__(self):
        self.flock = []  # Creates empty list called flock.

    def add_duck(self, duck: Duck) -> None:  # we annotate by adding :, then type of parameter (Duck), then return value (->) then type of parameter (None)
        fly_method = getattr(duck, 'fly', None)  # CHANGE_5 - get attribute 'fly' from duck instance, otherwise return None if not there
        if callable(fly_method):  # if fly_method is callable (is True), then add new duck to flock
            self.flock.append(duck)  # Adds new duck to the flock

    def migrate(self):
        problem = None  # first we initialize problem with None.
        for duck in self.flock:
            try:              # Check to see if ducks can fly
                duck.fly()    # causes every duck in the flock to fly by calling their fly method.
            except AttributeError as e:  # attribute error is assigned to variable e
                print("This duck cannot fly")  # Notifies you there is a duck that cannot fly, indicating its probably not a duck
                problem = e  # Then the variable problem is assigned the AttributeError e
        if problem:  # if problem exist, in this case it does because we assigned it e
            raise problem   # Then we raise the problem in the main program. raise is opposite of pass.




    # =====================================
    # Notifying user there is an exception
    # =====================================

    # CHANGE_6
    # Above program runs fine but the user will not know that passing penguin that cannot fly is not acceptable in a module that uses fly method
    # So we can raise an exception to warn the user. CHANGE_6
    # We used a TypeError exception because it is most appropriate since user is trying to pass a penguin which cannot fly
    # The error message (Stack trace) shows where the exception was raised and the call that originated the error
    # So this error will be known immediately at testing and the programmer can remove the bug

class Flock(object):

    def __init__(self):
        self.flock = []  # Creates empty list called flock.

    def add_duck(self, duck: Duck) -> None:  # we annotate by adding :, then type of parameter (Duck), then return value (->) then type of parameter (None)
        fly_method = getattr(duck, 'fly', None)  # CHANGE_5 - get attribute 'fly' from duck instance, otherwise return None if not there
        if callable(fly_method):  # if fly_method is callable (is True), then add new duck to flock
            self.flock.append(duck)  # Adds new duck to the flock
        else:                        # CHANGE_6: This raises an exception and tells user he added Class Penguin instead of Duck
            raise TypeError("Cannot add duck, are you sure its not a "+str(type(duck).__name__))

    def migrate(self):
        problem = None  # first we initialize problem with None.
        for duck in self.flock:
            try:              # Check to see if ducks can fly
                duck.fly()    # causes every duck in the flock to fly by calling their fly method.
            except AttributeError as e:  # attribute error is assigned to variable e
                print("This duck cannot fly")  # Notifies you there is a duck that cannot fly, indicating its probably not a duck
                problem = e  # Then the variable problem is assigned the AttributeError e
        if problem:  # if problem exist, in this case it does because we assigned it e
            raise problem   # Then we raise the problem in the main program. raise is opposite of pass.



# ============================
# Testing exception handlers
# ============================

# CHANGE_7
# The other reason you may want to raise exceptions is so that you can test your exception handlers.
# We will update the code with CHANGE_7 so that penguin1 has a flying method
# we will give Penguin an aviator method

# Read more above on CHANGE_7 next to class Penguin(object) above

# Now we will raise an exception inside the for loop under under def migrate below. CHANGE_7
# When you run code under migration.py, you get error message "AttributeError: Testing exception handling in migrate"
# this comes after each duck flies (even the ones that fly) and when all the ducks have been processed, then we get the
# exception and the stack trace (stack trace is where it shows you lines that are causing errors).

# This is a useful technique of testing your exceptions.
# we raise an exception that we are handling in the code inside the try block

# NOTE: you need to remove the test code before you release the software for use, otherwise your users will get errors
# A way to help you remember is to put comment next to it: "TODO remove this before release"
# Any comment with word TODO causes intellij to track it as something that needs to be done.

# NOTE that intellij has a tab below to track all the TODO things in your code
# you can click it to see everything that needs to be removed. click on it and it takes you to the line you need.

class Flock(object):

    def __init__(self):
        self.flock = []  # Creates empty list called flock.

    def add_duck(self, duck: Duck) -> None:  # we annotate by adding :, then type of parameter (Duck), then return value (->) then type of parameter (None)
        fly_method = getattr(duck, 'fly', None)  # CHANGE_5 - get attribute 'fly' from duck instance, otherwise return None if not there
        if callable(fly_method):  # if fly_method is callable (is True), then add new duck to flock
            self.flock.append(duck)  # Adds new duck to the flock
        else:                        # CHANGE_6: This raises an exception and tells user he added Class Penguin instead of Duck
            raise TypeError("Cannot add duck, are you sure its not a "+str(type(duck).__name__))

    def migrate(self):
        problem = None  # first we initialize problem with None.
        for duck in self.flock:
            try:              # Check to see if ducks can fly
                duck.fly()    # causes every duck in the flock to fly by calling their fly method.
                raise AttributeError("Testing exception handling in migrate")  # CHANGE_7 - TODO remove this before release
            except AttributeError as e:  # attribute error is assigned to variable e
                print("This duck cannot fly")  # Notifies you there is a duck that cannot fly, indicating its probably not a duck
                problem = e  # Then the variable problem is assigned the AttributeError e
        if problem:  # if problem exist, in this case it does because we assigned it e
            raise problem   # Then we raise the problem in the main program. raise is opposite of pass.




if __name__ == '__main__':
    donald = Duck()
    donald.fly()

# Now we will use our ducks object in another program, so we will create a new python file called migration.py
