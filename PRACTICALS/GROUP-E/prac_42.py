# f. Write a Python program to store student records in a file students.txt.
# Each record should contain fields: Roll Number, Name, and Marks.
# Provide options to: Add a new record. Display all records. 
# Search for a student by Roll Number. 
# Implement appropriate exception handling for invalid inputs or missing files.


def add_record():
    try:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        file = open("students.txt", "a")
        file.write(f"{roll},{name},{marks}\n")
        file.close()

        print("Record Added")

    except:
        print("Invalid Input")


def display_records():
    try:
        file = open("students.txt", "r")

        print("\nStudent Records:")
        print(file.read())

        file.close()

    except FileNotFoundError:
        print("File not found")


def search_record():
    try:
        roll = input("Enter Roll Number to search: ")

        file = open("students.txt", "r")

        found = False

        for line in file:
            data = line.strip().split(",")

            if data[0] == roll:
                print("Record Found:", data)
                found = True

        if not found:
            print("Record not found")

        file.close()

    except FileNotFoundError:
        print("File not found")


# Menu
while True:
    print("\n1. Add Record")
    print("2. Display Records")
    print("3. Search Record")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_record()

    elif choice == "2":
        display_records()

    elif choice == "3":
        search_record()

    elif choice == "4":
        break

    else:
        print("Invalid Choice")