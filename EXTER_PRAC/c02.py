# 2 a. Implement appropriate exception handling for invalid inputs or missing files.
    
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ValueError:
    print("Invalid input! Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program Ended")







# b. Define a class Employee with attributes: emp_id, name, and salary.
# Use a constructor to initialize the attributes.
# Define a destructor that prints a message when an object is deleted. 
# Create and delete employee objects to observe the behavior of the destructor.


class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

        print("Employee Object Created")

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

    def __del__(self):
        print("Employee Object Deleted")


e1 = Employee(101, "Om", 50000)

e1.display()

del e1