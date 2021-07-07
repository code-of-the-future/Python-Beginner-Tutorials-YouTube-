# Import relevant modules
import random

# This imports all the punctuation (i.e special characters) 
from string import punctuation
# Create a list with all of these special characters 
special_chars = list(punctuation)  # List has 32 elements in (can determine this by 'print(len(special_chars))'

# Set up the password generator as before
password = ""  # Create an empty string
for a in range(5):  # We want our password to 15 characters (3*5 = 15)
    i = chr(random.randint(65, 90))  # Creates a random upper case character
    j = chr(random.randint(65, 90)).lower()  # Creates a random lower case character
    k = special_chars[random.randint(0, 31)]  # Creates a random special character from our list 'special_chars'
    password = str(password) + i + j + k  # Takes our empty string and adds the random characters we have assigned
    # above. This is repeated 5 times.
print(password)
