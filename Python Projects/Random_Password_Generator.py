# Import relevant modules
import random

# All uppercase password
password = ""
for i in range(10):
    i = chr(random.randint(65, 90))
    password = str(password) + i
print(password)

# Upper and lower case password
password = ""
for i in range(5):
    i = chr(random.randint(65, 90))
    for j in range(5):
        j = chr(random.randint(65,90)).lower()
    password = str(password) + j + i
print(password)

# The upper and lowercase password can be simplified as follows:
password = ""
for i in range(5):
    i = chr(random.randint(65, 90))
    j = chr(random.randint(65, 90)).lower()
    password = str(password) + i + j
print(password)

# This was ommited from the YouTube video but is a much nicer way of handling this problem! 
