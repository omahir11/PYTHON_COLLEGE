# c. Define a class Employee with attributes: emp_id, name, and salary. 
# Use a constructor to initialize the attributes. 
# Define a destructor that prints a message when an object is deleted. 
# Create and delete employee objects to observe the behavior of the destructor.

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

        print("Employee Created")

    def __del__(self):
        print("Employee Deleted")

e1 = Employee(1, "Om", 50000)

del e1