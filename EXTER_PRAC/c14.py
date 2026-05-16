# 14 a. Use the os module to: Get the current working directory.
# List all files in a directory. Create a new directory.
import os
# Current working directory
print("Current Working Directory:")
print(os.getcwd())
# List all files
print("\nFiles in Directory:")
print(os.listdir())
# Create new directory
os.mkdir("NewFolder")
print("\nDirectory Created Successfully")


# b. Define a class Student with attributes: name, roll_number, and marks.
# Create methods to: Input data for a student. Display the student's details. 
# Create multiple student objects and test the methods.
class Student:

    def __init__(self):
        self.name = ""
        self.roll_number = 0
        self.marks = 0

    def input_data(self):

        self.name = input("Enter Name: ")
        self.roll_number = int(input("Enter Roll Number: "))
        self.marks = float(input("Enter Marks: "))

    def display(self):

        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)


# Create multiple objects
s1 = Student()
s2 = Student()

s1.input_data()
s2.input_data()

s1.display()
s2.display()