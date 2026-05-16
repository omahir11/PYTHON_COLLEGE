# 8 a. Write a Python program to create a file named example.txt, 
# write a paragraph of text to it, and close the file.
# Reopen the file in read mode and display its contents. 
# Open the file in append mode and add an additional line of text.
# Reopen the file in read mode and verify the updated content.
# Write to file
file = open("example.txt", "w")
file.write("Python is a powerful programming language.\n")
file.write("It is easy to learn and use.\n")
file.close()

# Read file
file = open("example.txt", "r")
print("File Contents:")
print(file.read())
file.close()

# Append to file
file = open("example.txt", "a")
file.write("This line is added using append mode.\n")
file.close()

# Read updated content
file = open("example.txt", "r")
print("\nUpdated File Contents:")
print(file.read())
file.close()


# b. Write a program to filter even numbers from a list using filter and a lambda function.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers =", even_numbers)