# This is taken from the Codecademy site.

#Syntax

# Booleans - data type. Just like a switch, either True or False
# Variables can be used to store booleans:
a = True
b = False

# Variable examples
my_int = 7
my_float = 1.23
my_bool = True

# Reassigning variables
my_int = 9
my_int = 3
print(my_int)

# Whitespace
# In python, whitespace is sued to structure code. Whitespace is important, so you have to be careful
# with how you use it. Below is badly formatted code, and produces an error
def spam():
eggs = 12
return eggs
  
print spam()

# Correct formatting is:
def spam():
	eggs = 12
	return eggs

print spam()

# A matter of interpretation
# Discussing using the e/interpreter window on the Codecademy site
spam = True
eggs = False

# Single line comments, and I have been doing this, so we can move on
# Next is multiline comments
# As this shows, the # symbol is good for single line comments
# The following allows multiline comments
""" As we can see, if we use three quotation
marks at the start and end of a section of multiline text
it is considered to be a comment """

# Next we take a look at carrying out some maths operstions
addition = 72 + 23
subtraction = 108 - 204
multiplication = 108 * 0.5
division = 108 / 9

# Set count_to equal to the sum of two big numbers
a = 10000
b = 600
count_to = a+b
print count_to
# ##############################################################################################
#Next is a section called Exponentiation
# Maths can be done using calculators, so why bother with Python?
# Well, because you can combine maths with other data types, such as boolean
# and commands to create usful and powerful programs. 
# When working with exponents, we do the following to make a new variable
# called eight and set it to 8, using 2^3.

#Set eggs equal to 100 using exponentiation on line 3!

eggs = 10 ** 2

print eggs
eight = 2 ** 3

# ################################################################################################
# Modulo
# Our final operator is modulo. Modulo returns the remainder of a division. 
# Typing 3 % 2, it will return 1, because 2 goes into 3 once, with 1 left over.
# Set spam equal to 1 using modulo on line 3!

spam = 101 % 100

# #############################################################################################
# Bringing it all together
"""So far, you've learned about:
Variables, which store values for later use data types, such as numbers and booleans, whitespace, which separates statements,
comments, which make your code easier to read arithmetic operations, including +, -, *, /, **, and %
"""
# This is my comment.
monty = True
python = 1.234
monty_python = python ** 2
