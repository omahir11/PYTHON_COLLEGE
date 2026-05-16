# e. Create two sets of integers and perform the following operations:
# Union, intersection, difference, and symmetric difference.
# Check for subset and superset relationships. 
# Remove duplicate elements from a list using a set. 
# Write a program to find common elements between two lists using sets.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union
print("Union:", a | b)

# Intersection
print("Intersection:", a & b)

# Difference
print("Difference:", a - b)

# Symmetric Difference
print("Symmetric Difference:", a ^ b)

# Subset and Superset
print("Subset:", a.issubset(b))
print("Superset:", a.issuperset(b))

# Remove duplicates from list
nums = [1, 2, 2, 3, 4, 4, 5]
print("Without duplicates:", list(set(nums)))

# Common elements between lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)

print("Common elements:", common)