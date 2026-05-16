# 11 a. Use the random module to generate: A random integer between two numbers. 
# A random floating-point number. A random element from a list. 
import random
# Random integer
print("Random Integer:", random.randint(1, 100))
# Random floating-point number
print("Random Float:", random.random())
# Random element from list
colors = ["Red", "Blue", "Green", "Yellow"]
print("Random Choice:", random.choice(colors))


# b. Write a Python program to create a CSV file data.csv with fields:
#  ID, Name, and Age. Insert 5 records into the file. 
#  Read and display the contents of the CSV file. Search and display a specific record by ID.

import csv
# Writing to CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Age"])
    writer.writerow([1, "Om", 20])
    writer.writerow([2, "Rahul", 21])
    writer.writerow([3, "Amit", 22])
    writer.writerow([4, "Sneha", 19])
    writer.writerow([5, "Priya", 23])

print("CSV File Created")

# Reading CSV file
print("\nCSV File Contents:")

with open("data.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# Search record by ID
search_id = input("\nEnter ID to search: ")

with open("data.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)

    found = False

    for row in reader:

        if row[0] == search_id:
            print("Record Found:", row)
            found = True
            break

    if not found:
        print("Record Not Found")