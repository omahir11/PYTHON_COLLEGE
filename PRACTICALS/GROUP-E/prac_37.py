# a. Write a Python program to create a file named example.txt,
# write a paragraph of text to it, and close the file.
# Reopen the file in read mode and display its contents. 
# Open the file in append mode and add an additional line of text. 
# Reopen the file in read mode and verify the updated content.


# Write to file
file = open("example.txt", "w")
file.write("Python is a powerful programming language.")
file.close()

# Read file
file = open("example.txt", "r")
print(file.read())
file.close()

# Append text
file = open("example.txt", "a")
file.write("\nThis is an added line.")
file.close()

# Read updated file
file = open("example.txt", "r")
print("\nUpdated Content:")
print(file.read())
file.close()