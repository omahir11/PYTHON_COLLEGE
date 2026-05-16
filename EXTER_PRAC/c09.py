# 9 a. Use reduce to compute the sum of elements in a list.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum =", sum_numbers)


# b. Create a class Person with attributes like name and age. 
# Derive a class Employee from Person, adding attributes like emp_id and department.
#  Further derive a class Manager from Employee, adding an attribute team_size. 
#  Demonstrate the usage of attributes and methods from all levels.


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):

    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age)

        self.emp_id = emp_id
        self.department = department

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)


class Manager(Employee):

    def __init__(self, name, age, emp_id, department, team_size):
        super().__init__(name, age, emp_id, department)

        self.team_size = team_size

    def display_manager(self):
        print("Team Size:", self.team_size)


m = Manager("Om", 25, 101, "IT", 10)

m.display_person()
m.display_employee()
m.display_manager()