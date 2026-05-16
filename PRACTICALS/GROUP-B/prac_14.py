# c. Create a tuple of mixed data types and access elements using indexing.
# Write a program to: 
# Find the index of an element.
# Count the occurrences of an element in the tuple.
# Convert a tuple to a list and back to a tuple after modifications.



# Create tuple
t = (10, "Om", 5.5, 10, "Python")

# Access elements
print("First element:", t[0])
print("Second element:", t[1])

# Find index
print("Index of Python:", t.index("Python"))

# Count occurrences
print("Count of 10:", t.count(10))

# Convert tuple to list
lst = list(t)

# Modify list
lst.append("New")

# Convert back to tuple
t = tuple(lst)

print("Modified Tuple:", t)