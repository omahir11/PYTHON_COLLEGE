# l. Use the os module to: 
# a. Get the current working directory.
# b. List all files in a directory. 
# c. Create a new directory.


import os

# Current working directory
print(os.getcwd())

# List files
print(os.listdir())

# Create new directory
os.mkdir("NewFolder")