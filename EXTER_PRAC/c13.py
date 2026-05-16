# 13 a. Create a tuple of mixed data types and access elements using indexing.
# Write a program to: Find the index of an element. 
# Count the occurrences of an element in the tuple. 
# Convert a tuple to a list and back to a tuple after modifications. 

my_tuple = (10, "Python", 20.5, "Python", True)
print("Tuple =", my_tuple)
# Access using indexing
print("First Element =", my_tuple[0])
# Find index
print("Index of Python =", my_tuple.index("Python"))
# Count occurrences
print("Count of Python =", my_tuple.count("Python"))
# Convert tuple to list
temp_list = list(my_tuple)
# Modify list
temp_list.append("New Element")
# Convert back to tuple
my_tuple = tuple(temp_list)
print("Modified Tuple =", my_tuple)





# b. Write a Python program to copy the contents of source.txt into destination.txt. 
# Ensure the program handles the case where source.txt does not exist,
# displaying an appropriate error message using exception handling.


try:
    with open("source.txt", "r") as source:
        content = source.read()
    with open("destination.txt", "w") as destination:
        destination.write(content)
    print("File Copied Successfully")
except FileNotFoundError:
    print("source.txt file does not exist")