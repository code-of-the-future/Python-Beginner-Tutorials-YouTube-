# Booleans

print(True)
print("True")

print(type(True))  # This type is a bool
print(type("True"))  # This type is a string

# Testing whether these statements are correct
# print(5 == 5)
# print(6 == 5)

# Incorporating the if statement with a boolean
x = 11
y = 5
if x % y == 0:
    print(True)
else:
    print(False)

# while Loop
number = 1
while number < 4:
    print(number)
    if number == 4:
        break
    number = number + 1

# If statement
number = 1
if number > 1:
    print("Positive Number Greater Than One")
elif number == 0:
    print("Zero")
elif number == 1:
    print("One")
else:
    print("Negative Number")

# incorporating the else statement within the while loop
number = 2
while number < 4:
    print(number)
    number = number + 1
else:
    print("number is no longer less than 4")

def born(country):
    return print("i am from" + country)

born("england")

def squared(x):
    result = x**2
    return result

print(squared(2))
