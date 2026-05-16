# a. Create two sets of integers and perform the following operations:
# Union, intersection, difference, and symmetric difference.
# Check for subset and superset relationships. 
# Remove duplicate elements from a list using a set.
# Write a program to find common elements between two lists using sets. 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Union =", set1 | set2)
print("Intersection =", set1 & set2)
print("Difference =", set1 - set2)
print("Symmetric Difference =", set1 ^ set2)
print("Subset =", set1.issubset(set2))
print("Superset =", set1.issuperset(set2))

# Remove duplicates from list
lst = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(lst))
print("List after removing duplicates =", unique_list)

# Common elements between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print("Common Elements =", common)



# b. Create a program to find the sum of all even numbers between 1 and 100.
sum_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
print("Sum of Even Numbers =", sum_even)


# c. Write a program using a while loop to reverse a given number.

num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed Number =", reverse)