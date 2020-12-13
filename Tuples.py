# Tuples in Python

# Conventionally, tuples look like this,
Fruit = ("Apples", 4, "Bananas", 5, "Oranges", 6)

List_of_Fruit = ["Apples", 4, "Bananas", 5, "Oranges", 6]

# We can modify elements within a list. We can't modify elements within a tuple!
List_of_Fruit[0] = "Strawberries"
print(List_of_Fruit)

# We can perform similar operations on tuples like we can with lists
# Slicing tuples
print(Fruit[1:5])

# Recalling elements within a tuple
print(Fruit[0])

# Concatenation of tuples
Fruit = Fruit[0:4] + ("Cherries", 10)
print(Fruit)

# Tuples with one element
x = (5, )  # This is the notation for a tuple with one element!
print(type(x))

# We can find the length of a tuple
print(len(Fruit))

# Creating a tuple
another_tuple = tuple(("Hello", 18, True))
print(type(another_tuple))

# Converting a tuple to a list and then back to a tuple!
Fruit = list(Fruit)
Fruit.append("Pears")
Fruit = tuple(Fruit)
print(Fruit)

# Unpacking tuples
Fruit = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
(one, *two, three, four) = Fruit
print(one)
print(two)
print(three)

# Incorporate loops within tuples
for i in range(len(Fruit)):
    print(Fruit[i])




