# Test yourself quiz!

# Question 1 - Assigning Variables
x = 10  # assigned an x variable equal to 10
y = 3   # assigned an y variable equal to 3
print(x * y)  # Multiplication
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x / y)  # Division


# Question 2 - Lists
my_list = list(range(0, 101, 2))  # Create the list
print(my_list)

print(my_list[0:10])  # Printing the first ten elements of the list

print(len(my_list))  # Finding the length of the list

my_list.append("Hello")  # Appending a value to this list - can be any type!
print(my_list)


# Question 3 - If Statement
number = 835
if number % 5 == 0:
    print("number is divisible by 5")
else:
    print("number is not divisible by 5")


# Question 4 - For Loop
for i in range(6):    # Remember we use 6 because the range command takes up to value n-1
    print(i)


# Question 5 - Turtle
import turtle

for i in range(5):  # A pentagon has five sides!
    turtle.right(72)  # This is the angle needed to produce a pentagon
    turtle.forward(100)  # This will give the length of the pentagon sides
turtle.done()


# Question 6 - Functions
def pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False


print(pythagorean_triple(3, 4, 5))   # This is True
print(pythagorean_triple(3, 9, 15))  # This is False


# Question 7 - Spot the Error!
n = 5
while n > 0:
    n = n + 1
    print(n)


# Questions 8 - Plotting
import matplotlib.pyplot as plt  # Import the relevant modules

list1 = [1, 6, 13, 16, 24]
list2 = [3, 7, 17, 28, 30]

plt.plot(list1, list2, c="blue", linewidth=1, label="A Line!", linestyle="dashed",
         marker='s', markerfacecolor="purple", markersize=2)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Python Plot of a Line")
plt.legend()
plt.show()
