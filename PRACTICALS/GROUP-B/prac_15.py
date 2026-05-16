# d. Create a dictionary to store student details
# (e.g., name, roll number, marks). 
# Write a program to: Add, update, and delete key-value pairs.
# Iterate through keys, values, and items. 
# Implement a program to count the frequency of words in a given string using a dictionary.

# Create dictionary
student = {
    "name": "Om",
    "roll": 101,
    "marks": 85
}

# Add key-value pair
student["grade"] = "A"

# Update value
student["marks"] = 90

# Delete key-value pair
del student["roll"]

# Iterate keys
print("Keys:")
for k in student.keys():
    print(k)

# Iterate values
print("\nValues:")
for v in student.values():
    print(v)

# Iterate items
print("\nItems:")
for k, v in student.items():
    print(k, ":", v)

# Word frequency
text = input("\nEnter string: ").split()

freq = {}

for word in text:
    freq[word] = freq.get(word, 0) + 1

print("Word Frequency:", freq)