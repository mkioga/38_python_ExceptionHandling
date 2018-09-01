
# ===============
# migration.py
# ===============

# We need to import ducks.py so that we can use the objects from ducks.py
# Then we will create a new Flock and add some ducks to that.

import ducks

# Uses the Flock class from ducks.py

flock = ducks.Flock()

# We define duck objects using Duck class from ducks.py

duck1 = ducks.Duck()
duck2 = ducks.Duck()
duck3 = ducks.Duck()
duck4 = ducks.Duck()
duck5 = ducks.Duck()
duck6 = ducks.Duck()
duck7 = ducks.Duck()

# Now we will add the ducks to the flock.

flock.add_duck(duck1)
flock.add_duck(duck2)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

# Now that we have added all 7 ducks above to the flock.
# We will make them migrate.
# When we run this code, we get 7 results of "Weee, this is fun" which comes from the ducks flying

flock.migrate()


# ===============================================

# Now the problem comes when we try to add "penguin1" the penguin to the ducks.
# when we run this program with penguin1 being added to ducks, we get an error "'Penguin' object has no attribute 'fly'"
# Penguins cannot fly, so the migration.py code crashes when it tries to call penguins fly method (which does not exist)


import ducks

# Uses the Flock class from ducks.py

flock = ducks.Flock()

# We define duck objects using Duck class from ducks.py

duck1 = ducks.Duck()
duck2 = ducks.Duck()
duck3 = ducks.Duck()
duck4 = ducks.Duck()
duck5 = ducks.Duck()
duck6 = ducks.Duck()
duck7 = ducks.Duck()

penguin1 = ducks.Penguin()  # first we create penguin1, from the Penguin class

mallard1 = ducks.Mallard()  # Part of CHANGE_3. We create a Mallard instance. NOTE Mallard is a subclass of Duck

# Now we will add the ducks to the flock.

flock.add_duck(duck1)
flock.add_duck(duck2)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(penguin1)   # Now we add penguin1 to the flock of ducks
flock.add_duck(duck5)
flock.add_duck(mallard1)   # Now we add mallard1 to the flock. Note that Mallard is a subclass of Duck
flock.add_duck(duck6)
flock.add_duck(duck7)



# Now that we have added all 7 ducks above to the flock.
# We will make them migrate.
# When we run this code, we get 7 results of "Weee, this is fun" which comes from the ducks flying
# But will also get error "'Penguin' object has no attribute 'fly'" when we try to call penguin1 because
# class penguin has no fly method.

flock.migrate()

# ===================================================
# How to handle problems like one above using "hint"
# ===================================================

# First thing we can do is provide users of our module with a hint as to what they should be passing to our methods
# Python 3.5 added support for type "Hint" in function and method declarations but function "annotations" have been around since pyhon 3.0
# You can use an "annotation" in the same format as you use a type "hint" , what we will do will work with all versions of python 3

# Now we will add some "hints" to our "add_duck" method under "Flocks" in ducks.py so that anyone using that module
# has an indication of what they should be providing to the method.

# Go to ducks.py, under class Flock

# =================================

# After adding annotation in ducks.py, we come back to migration.py and notice that error check has noticed the annotation
# on line "flock.add_duck(penguin1)". if you hover on it, it says "Expected type "Duck" not 'Penguin'"

# If you click above add_duck method and then type Ctrl+Q, it gives an indication that we should be adding objects of type Duck
# Note that self has been annotated automatically into "self: flock", hence there is no need to annotate self parameters in method calls.

# NOTE that if you use a hint for one of your parameters, you should add a hint for all of them, including the return value.
# you can find more information on this in pep 484
# https://www.python.org/dev/peps/pep-0484/
# under non-goals, we see that:
# " It should also be emphasized that Python will remain a dynamically typed language,
# and the authors have no desire to ever make type hints mandatory, even by convention"

# under "Meanings of annotations" it recommends you add hints to all parameters if you add to any one of them

# NOTE that the hints or annotations are just to give user indication of what methods to use.
# If the ignore the hint, the program will still crash.

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

# =================================
# How to notify there is a problem:
# using " raise "
# =================================

# CHANGE_2 in ducks.py
# The problem here is that migration.py will not know if there is a problem and the programmer will not debug it.
# There is a way to all the ducks that can fly still fly, but also raise an exception error to notify you
# When we run the code now, it lets all the ducks that can fly to fly but also raises an AttibuteError for Penguin who cannot fly.

# =================================
# Creating exceptions
# =================================

# CHANGE_3
# We can create our own exceptions because exceptions are objects
# We have already provided a hint that we should pass a "duck" or subclass of "duck"
# We can create a "Mallard" class which is also a duck
# But first we can check the type of argument that is passed.
# We do this on CHANGE_3 under ducks.py
# if we run the code now, we see that all 7 ducks that can fly are allowed to fly
# The penguin is ignored because it is not of type Duck

# If we run the code with mallard1 called, we still get only 7 ducks flying
# program also ignores mallard1 even if it is a subclass of duck and has fly method.

# As we can see, the "if type(duck) is Duck: " checks if type is Duck, and does excludes subclasses that may be deriving from Duck
# and have same methods as Duck



# ================
# isinstance
# ================

# CHANGE_4
# Since we have seen the limitations of checking type in CHANGE_3
# There are times when you want to check type, we can use "isinstance" instead of checking "type'
# When we run this with "isinstance" we see that "mallard1" runs fine because it is part of class Duck

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

# =====================================
# Notifying user there is an exception
# =====================================

# CHANGE_6
# Above program runs fine but the user will not know that passing penguin that cannot fly is not acceptable in a module that uses fly method
# So we can raise an exception to warn the user. CHANGE_6
# We used a TypeError exception because it is most appropriate since user is trying to pass a penguin which cannot fly
# The error message (Stack trace) shows where the exception was raised and the call that originated the error
# So this error will be known immediately at testing and the programmer can remove the bug


# ============================
# Testing exception handlers
# ============================

# CHANGE_7
# The other reason you may want to raise exceptions is so that you can test your exception handlers.
# We will update the code with CHANGE_7 so that penguin1 has a flying method

# See more under ducks.py