# 7 a. Write a function to calculate the factorial of a number using recursion. 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))







# b. Create a base class Shape with a method area().
#  Define two derived classes: Circle with a specific implementation of area() 
#  to calculate the area of a circle. Rectangle with a specific implementation of area()
#   to calculate the area of a rectangle.

class Shape:

    def area(self):
        print("Area Method")


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of Circle =", area)


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print("Area of Rectangle =", area)


c = Circle(5)
c.area()

r = Rectangle(4, 6)
r.area()