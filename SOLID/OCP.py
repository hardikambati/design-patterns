"""
    2. Open-Closed Principle [OCP]
    -> Every software entity (class, function, module etc) should be OPEN for EXTENSION but CLOSED for MOFIFICATION
"""


from math import pi


class Shape:

    def __init__(self, shape_type: str, **kwargs):
        self.shape_type = shape_type

        if shape_type == 'rectangle':
            self.width = kwargs.get('width')
            self.height = kwargs.get('height')
        elif shape_type == 'circle':
            self.radius = kwargs.get('radius')
        # step 1 : for triangle, we'll need to add another elif condition here
        else:
            raise TypeError('Invalid shape_type received')


    def calculate_area(self) -> float:
        if self.shape_type == 'rectangle':
            return (self.width*self.height)
        elif self.shape_type == 'circle':
            return (pi * self.radius**2)
        # step 2 : for triangle, we'll need to add another elif condition here as well
        # bad practise because, the class should be CLOSED for MOFIFICATION



# rect = Shape(shape_type='rectangle', width=5, height=5)
# print(rect.calculate_area())


# tr = Shape(shape_type='triangle', breadth=5, height=5)
# print(tr.calculate_area())


# TO


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
    
# Now, for every type of shape, you can create a separate class with it's own `calculate_area` implementation


rect = Rectangle(width=4, height=4)
print(rect.calculate_area())


