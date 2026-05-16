# e. Write a Python program to create a CSV file data.csv with fields: ID, Name, and Age.
# Insert 5 records into the file. 
# Read and display the contents of the CSV file. 
# Search and display a specific record by ID.

import csv

# Write CSV file
file = open("data.csv", "w", newline="")
writer = csv.writer(file)

writer.writerow(["ID", "Name", "Age"])

writer.writerow([1, "Om", 18])
writer.writerow([2, "Raj", 20])
writer.writerow([3, "Aman", 19])
writer.writerow([4, "Neha", 21])
writer.writerow([5, "Sara", 22])

file.close()

# Read CSV file
file = open("data.csv", "r")

reader = csv.reader(file)

print("CSV Contents:")
for row in reader:
    print(row)

file.close()

# Search by ID
search_id = input("Enter ID to search: ")

file = open("data.csv", "r")

reader = csv.reader(file)

for row in reader:
    if row[0] == search_id:
        print("Record Found:", row)

file.close()