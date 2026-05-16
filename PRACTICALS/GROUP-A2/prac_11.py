# Write a program to check if a given string is a palindrome.
#  Modify the program to ignore case sensitivity.

s = input("Enter string: ")#.lower()
# s = input("Enter string: ").lower()

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")