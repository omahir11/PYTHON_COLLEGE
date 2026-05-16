# 6 a. Given a list of temperatures in Celsius, use list comprehension to convert them to Fahrenheit.
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Celsius Values =", celsius)
print("Fahrenheit Values =", fahrenheit)


# b. Create a dictionary to store student details (e.g., name, roll number, marks). 
# Write a program to: Add, update, and delete key-value pairs. Iterate through keys, values, and items.
student = {
    "name": "Om",
    "roll_number": 101,
    "marks": 85
}

print("Original Dictionary:")
print(student)

# Add key-value pair
student["grade"] = "A"
# Update value
student["marks"] = 90
# Delete key-value pair
del student["grade"]

print("\nUpdated Dictionary:")
print(student)

# Iterate through keys
print("\nKeys:")
for key in student.keys():
    print(key)

# Iterate through values
print("\nValues:")
for value in student.values():
    print(value)

# Iterate through items
print("\nItems:")
for key, value in student.items():
    print(key, ":", value)


# c. Implement a program to count the frequency of words in a given string using a dictionary.

text = input("Enter a string: ")

words = text.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")

for word, count in frequency.items():
    print(word, ":", count)