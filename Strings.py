# Strings

# We have already covered strings, integers, floats, booleans and lists

# Integers, floats and booleans are all considered to be simple data types
# They cannot be broken down!

# Lists and strings are different! They are made up of smaller pieces which
# CAN be broken down.

# We already know what strings are!
print("Hello, world!")
print(type("Hello, world!"))

# Operations on strings
# Addition sign concatenation
Greeting = "Hello"
Name = "Ellie"
print(Greeting + Name)

# * Operator
print(Greeting*3)
print(Greeting + Name*3)
print((Greeting + Name)*3)

# Index Operator
Name = "Brad"
print(Name[2])
print(Name[0] + Name[3])

# Slicing strings
print(Name[0:4])
print(Name[:2])
print(Name[2:])

# Lowercase and Uppercase
Name = "Ellie"
print(Name.lower())
print(Name.upper())

# Count how many times a character appears in a string
print(Name.count("i"))

# Replace specific characters with other characters
print(Name.replace("l", "d"))

Name = "Ellie"
New_Name = Name.replace("l", "d")
print(New_Name)

# Finding the length of a string
print(len(Name))

# Format strings
# your_name = input("Your name: ")
# hello = "Hello {}".format(your_name)
# print(hello)

# Each letter in python is assigned to a specific number!
print("orange" < "strawberry")
print(ord("o"))
print(chr(78))
# We can perform maths on strings!

# in and not operators
fruit = "bananas"
print("a" in fruit)
print("s" not in fruit)

# Incorporate a few things we've learnt so far
x = "hello"
y = ""
for character in x:
    y = character.upper() + y
print(y)








