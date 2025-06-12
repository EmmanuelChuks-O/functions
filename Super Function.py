# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape: # parent class
    def __init__(self,name, color, is_filled):
        self.color = color
        self.name = name
        self.is_filled = is_filled

    def describe(self):
        print(f"The {self.name} is {self.color} and it is {"filled" if self.is_filled else "not filled"}.")

class Circle(Shape):
    def __init__(self, name, color, is_filled, radius):
        super().__init__(name, color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a circle with the area of {3.14 * self.radius * self.radius}cm.")


class Square(Shape):
    def __init__(self, name, color, is_filled, width):
        super().__init__(name, color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with the area of {self.width * self.width}cm.")

class Triangle(Shape):
    def __init__(self, name, color, is_filled, width, height):
        super().__init__(name, color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with the area of {self.width * self.height / 2}cm.")


circle = Circle(name = "circle", color="red", is_filled=True, radius= 5)
square = Square(name= "square", color="blue", is_filled=False, width=10)
triangle = Triangle(name="triangle", color="black", is_filled=True, width=3, height=7)

circle.describe()
square.describe()
triangle.describe()

