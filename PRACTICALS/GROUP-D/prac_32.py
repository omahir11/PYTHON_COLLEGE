# a. Define a class Student with attributes: name, roll_number, and marks.
# Create methods to: Input data for a student. Display the student's details.
#  Create multiple student objects and test the methods.

class Student:
    def input_data(self):
        self.name = input("Enter name: ")
        self.roll = int(input("Enter roll number: "))
        self.marks = float(input("Enter marks: "))

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("Marks:", self.marks)

# Create objects
s1 = Student()
s2 = Student()

s1.input_data()
s2.input_data()

s1.display()
s2.display()