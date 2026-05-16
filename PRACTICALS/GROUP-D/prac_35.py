# d. Create a base class Shape with a method area(). 
# Define two derived classes: Circle with a specific implementation of area() 
# to calculate the area of a circle. 
# Rectangle with a specific implementation of area() to calculate the area of a rectangle.
#  Demonstrate polymorphism by creating objects of both derived classes and calling the area() method.


class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

c = Circle(5)
r = Rectangle(4, 6)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())