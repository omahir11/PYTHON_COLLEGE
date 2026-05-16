# a. If the basic salary of an employee is input through the keyboard,
# and the dearness allowance is 50% of the basic salary while the house
# rent allowance is 20% of the basic salary, write a program to calculate
# the employee's gross salary. 


basic = float(input("Enter Basic Salary: "))
da = 0.50 * basic
hra = 0.20 * basic
gross_salary = basic + da + hra
print("Dearness Allowance =", da)
print("House Rent Allowance =", hra)
print("Gross Salary =", gross_salary)



# b. Use the statistics module to calculate mean, median, and mode of a list of numbers.

import statistics
numbers = [10, 20, 30, 40, 50, 20]
mean_value = statistics.mean(numbers)
median_value = statistics.median(numbers)
mode_value = statistics.mode(numbers)
print("Mean =", mean_value)
print("Median =", median_value)
print("Mode =", mode_value)




# c. Write a Python program to store student records in a file students.txt.
# Each record should contain fields: Roll Number, Name, and Marks.
# Provide options to: Add a new record. Display all records. 
# Search for a student by Roll Number.


FILE_NAME = "students.txt"

def add_record():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{marks}\n")

    print("Record Added Successfully")


def display_records():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No records found")
            else:
                print("\nStudent Records")
                for line in data:
                    roll, name, marks = line.strip().split(",")
                    print("Roll:", roll, "Name:", name, "Marks:", marks)

    except FileNotFoundError:
        print("File does not exist")


def search_record():
    search_roll = input("Enter Roll Number to Search: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for line in file:
                roll, name, marks = line.strip().split(",")

                if roll == search_roll:
                    print("Record Found")
                    print("Name:", name)
                    print("Marks:", marks)
                    found = True
                    break

            if not found:
                print("Record not found")

    except FileNotFoundError:
        print("File does not exist")


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