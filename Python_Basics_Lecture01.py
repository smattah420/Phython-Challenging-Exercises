                            # ==============================
                            # Practice Questions – Python
                            # ==============================

"""
========================================
Lecture 01 – Python Basics Practice
========================================
# ========================================
# Lecture 01 – Topics Covered
# ========================================
# 1. print() function
#    - Basic printing
#    - sep and end parameters
#
# 2. Variables
#    - Variable creation
#    - Variable reassignment
#
# 3. Data Types
#    - int, float, string
#    - type() function
#
# 4. input() function
#    - Taking user input
#    - Understanding input as string
#
# 5. Type Casting
#    - Converting string to int using int()
#
# 6. Multiple Assignment
#    - Storing multiple values in one line
#
# 7. Swapping Variables
#    - Swapping without third variable
#
# 8. String Operations
#    - String concatenation
#    - Multiline strings
#
# 9. String Formatting
#    - f-strings
#    - format() method
#
# 10. Variable Naming Rules
#
# 11. Basic List Printing
# ========================================

Author: Syed Md Attah
"""

# ----------------------------------------
# Question 1
# ----------------------------------------
# Write a Python program to print “Python is Fun!” using a single print() statement
print("Python is Fun!")  

# ----------------------------------------
# Question 2
# ----------------------------------------
# Print your name and age in a single line output.
print("Name:", "Syed Attah", "| Age:", 18)

# ----------------------------------------
# Question 3
# ----------------------------------------
# Print the numbers 1, 2, 3, 4 separated by a Hash (#) using the sep parameter.
print(1, 2, 3, 4, sep="#")

# ----------------------------------------
# Question 4
# ----------------------------------------
# Use the end parameter to print "Hello" and "World" on the same line with a space in between.
print("Hello", end=" ")
print("World")

# ----------------------------------------
# Question 5
# ----------------------------------------
# Print “Learning-Python-is-easy!” using sep and end parameters.
print("Learning", "Python", "is", "easy!", sep="-", end="\n")

# ----------------------------------------
# Question 6
# ----------------------------------------
# Print the numbers 10, 20, 30 separated by a comma and a space (", "),
# and ensure the next print statement starts on the same line.
print(10, 20, 30, sep=", ", end=" ")
print("Done")

# ----------------------------------------
# Question 7
# ----------------------------------------
# Write a program that prints your name, age and city on the same line,
# each separated by the word "and".
print("Syed Attah", 18, "Karachi", sep=" and ")

# ----------------------------------------
# Question 8
# ----------------------------------------
#  Use the print() function to output the following without using multiple print statements:
# Welcome to Python.
# Let's learn together.
print("Welcome to Python.\nLet's learn together.")

# ----------------------------------------
# Question 9
# ----------------------------------------

a = 5
a = 2.5
print(a)
print(type(a))

# Output:
# 2.5
# <class 'float'>

# Explanation:
# Variable 'a' is reassigned from int to float.


# ----------------------------------------
# Question 10
# ----------------------------------------
# What will be the output of the following code?

value = "False"
print(type(value))

# Output:
# <class 'str'>

# Explanation:
# "False" is inside quotes, so it is treated as a string.


# ----------------------------------------
# Question 11
# ----------------------------------------
# What is the data type returned by input()
# and what will be the output of the code?

age = input("Enter your age: ")
print("You entered:", age)

# The following line is commented to avoid error
# print(age + 5)

# Explanation:
# input() always returns a string.
# Adding string and integer causes TypeError.


# Correct Version

age = int(input("Enter your age again: "))
print("Age after 5 years:", age + 5)


# ----------------------------------------
# Question 12
# ----------------------------------------
# Write a program to ask the user to enter two numbers,
# swap them, and print the result.


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Swapping using Python method
num1, num2 = num2, num1

print("After swapping:")
print("First number:", num1)
print("Second number:", num2)

# ----------------------------------------
# Question 13
# ----------------------------------------
# Create variables name and city with your name and city as values.
# Print both variables in a single line.

name = "Syed Md Attah"
city = "Karachi"

print("Name:", name, "| City:", city)


# ----------------------------------------
# Question 14
# ----------------------------------------
# Start with x = 5. Reassign x to 10.
# Print the final value of x.

x = 5
x = 10
print("\nFinal value of x:", x)


# ----------------------------------------
# Question 15
# ----------------------------------------
# Which of these variable names are valid in Python:
# my_var, 123_var, myVar1, your var?
# Use all valid variables and show output.

my_var = 100        # valid
myVar1 = 200        # valid

print("\nValid variable outputs:")
print("my_var =", my_var)
print("myVar1 =", myVar1)

# Invalid variable names (explained):
# 123_var  → invalid (cannot start with number)
# your var → invalid (space not allowed)


# ----------------------------------------
# Question 16
# ----------------------------------------
# Swap two variables a = 10 and b = 5 without using a third variable.

a = 10
b = 5

a, b = b, a

print("\nAfter swapping:")
print("a =", a)
print("b =", b)


# ----------------------------------------
# Question 17
# ----------------------------------------
# Concatenate strings stored in two different variables
# first_name and second_name and print result.

first_name = "Syed"
second_name = "Attah"

full_name = first_name + " " + second_name
print("\nFull Name:", full_name)


# ----------------------------------------
# Question 18
# ----------------------------------------
# Use f-strings to print your bio and input function must be used.

print("\nBio using f-string:")

bio_name = input("Enter your name: ")
bio_age = input("Enter your age: ")
bio_city = input("Enter your city: ")

print(f"My name is {bio_name}, I am {bio_age} years old and I live in {bio_city}.")


# ----------------------------------------
# Question 19
# ----------------------------------------
# Ask the user for their name, age, and city,
# then print a formatted sentence using format() method.

print("\nUsing format() method:")

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_city = input("Enter your city: ")

print("My name is {}, I am {} years old and I live in {}."
      .format(user_name, user_age, user_city))


# ----------------------------------------
# Question 20
# ----------------------------------------
# Take input from user as product & cost then print output:
# The Laptop costs $1200

print("\nProduct Cost Output:")

product = input("Enter product name: ")
cost = input("Enter product cost: ")

print(f"The {product} costs ${cost}")


# ----------------------------------------
# Question 21
# ----------------------------------------
# Print your full name, age, and city in the given format:
# Name: John | Age: 25 | City: New York

name = "Syed Md Attah"
age = 22
city = "Karachi"

print("Name:", name, "| Age:", age, "| City:", city)


# ----------------------------------------
# Question 22
# ----------------------------------------
# Print a countdown from 5 to 1 on the same line separated by spaces.

print("\nCountdown:")
print(5, 4, 3, 2, 1, sep=" ")


# ----------------------------------------
# Question 23
# ----------------------------------------
# Take user's email address using input function.

email = input("\nEnter your email address: ")
print("Your email is:", email)


# ----------------------------------------
# Question 24
# ----------------------------------------
# Print the names of five programming languages separated by (->)

# Using single print statement
print("\nProgramming Languages (Single Print):")
print("Python", "Java", "C++", "JavaScript", "PHP", sep=" -> ")

# Using multiple print statements
print("\nProgramming Languages (Multiple Print):")
print("Python", end=" -> ")
print("Java", end=" -> ")
print("C++", end=" -> ")
print("JavaScript", end=" -> ")
print("PHP")


# ----------------------------------------
# Question 25
# ----------------------------------------
# Print [1, 2, 3, 4, 5] using a single print statement.

print("\nNumbers List:")
print([1, 2, 3, 4, 5])


# ----------------------------------------
# Question 26
# ----------------------------------------
# Print the following output:
# Python
# Programming
# Assignment

print("\nAssignment Title:")
print("Python\nProgramming\nAssignment")


# ----------------------------------------
# Question 27
# ----------------------------------------
# Create two variables name and city and print them in a single line.

student_name = "Syed Md Attah"
student_city = "Karachi"

print("\nStudent Info:")
print("Name:", student_name, "| City:", student_city)


# ----------------------------------------
# Question 28
# ----------------------------------------
# We have four variables a = 5, b = 10, c = 3 and d = 6
# Swap values of a & b and c & d.

a = 5
b = 10
c = 3
d = 6

a, b = b, a
c, d = d, c

print("\nAfter Swapping:")
print("a =", a, ", b =", b)
print("c =", c, ", d =", d)


# ----------------------------------------
# Question 29
# ----------------------------------------
# Ask the user for their name, age, and city
# Print the sentence in reverse order using format()
# Expected output:
# Lahore is where I live. 22 is my age. My name is Ali.

print("\nReverse Sentence Output:")

u_name = input("Enter your name: ")
u_age = input("Enter your age: ")
u_city = input("Enter your city: ")

print("{} is where I live. {} is my age. My name is {}."
      .format(u_city, u_age, u_name))


# ----------------------------------------
# Question 30
# ----------------------------------------
# Ask the user to input product and its price
# Generate a receipt using f-string

print("\nReceipt:")

product = input("Enter product name: ")
price = input("Enter product price: ")

print(f"The {product} costs ${price}")


# ----------------------------------------
# End of Practice File
# ----------------------------------------


