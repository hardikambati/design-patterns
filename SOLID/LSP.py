"""
    3. Liskov Substitution Principle [LSP]
    -> For a base class, every derieved class should be replaceable by other derieved class, without changing the correctiveness of program
       if a function for derived class is called
"""


from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    
class Rectangle(Shape):

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width*self.height


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self) -> float:
        return pi * self.radius**2


def calc_area_for_shapes(shapes: list):
    for item in shapes:
        print(f'{item.calculate_area():.2f}')


rect = Rectangle(width=5, height=6)
circ = Circle(radius=3)

calc_area_for_shapes(shapes=[rect, circ])

# MORAL : `calc_area_for_shapes` function doesn't need to know any info about any shape
#          The shape should just be inheriting the base class (`Shape` class)