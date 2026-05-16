# a. Create a list of integers and perform the following: 
# Add, remove, and modify elements. 
# Sort the list in ascending and descending order.
# Find the maximum, minimum, and sum of the list.
# Write a program to remove duplicates from a list. 
# Implement list slicing to extract sub-lists.




# Create list
nums = [5, 2, 8, 2, 9, 1]

# Add element
nums.append(10)

# Remove element
nums.remove(2)

# Modify element
nums[0] = 100

print("List:", nums)

# Sorting
print("Ascending:", sorted(nums))
print("Descending:", sorted(nums, reverse=True))

# Max, Min, Sum
print("Maximum:", max(nums))
print("Minimum:", min(nums))
print("Sum:", sum(nums))

# Remove duplicates
unique = list(set(nums))
print("Without duplicates:", unique)

# List slicing
print("First 3 elements:", nums[:3])
print("Last 2 elements:", nums[-2:])