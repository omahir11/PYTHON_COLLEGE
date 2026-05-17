# 5 a. Write a program to check if a given string is a palindrome.
# Modify the program to ignore case sensitivity. 

string = input("Enter a string: ")
new_string = string.lower()
if new_string == new_string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")





# b. Create a list of integers and perform the following: 
# Add, remove, and modify elements. 
# Sort the list in ascending and descending order.
# Find the maximum, minimum, and sum of the list.
# Write a program to remove duplicates from a list. 
# Implement list slicing to extract sub-lists. 

numbers = [10, 20, 30, 40, 50]

# Add element
numbers.append(60)
# Remove element
numbers.remove(20)
# Modify element
numbers[1] = 25
print("Updated List =", numbers)

# Sorting
print("Ascending Order =", sorted(numbers))
print("Descending Order =", sorted(numbers, reverse=True))

# Maximum, Minimum, Sum
print("Maximum =", max(numbers))
print("Minimum =", min(numbers))
print("Sum =", sum(numbers))

# Remove duplicates
dup_list = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(dup_list))
print("Without Duplicates =", unique)

# List slicing
print("Sub List =", numbers[1:4])



# c. Implement a program to check if a given matrix is symmetric.

matrix = [[1, 2, 3],
          [2, 4, 5],
          [3, 5, 6]]

rows = len(matrix)
cols = len(matrix[0])

symmetric = True

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break

if symmetric:
    print("Matrix is Symmetric")

else:
    print("Matrix is Not Symmetric")