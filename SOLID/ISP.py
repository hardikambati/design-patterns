"""
    4. Interface Segregation Principle [ISP]
    -> Interfaces should be client(classes) specific
       Clients(classes) should not be forced to depend on interfaces that they do not use
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw_square(self):
        pass

    @abstractmethod
    def draw_circle(self):
        pass


class Square(Shape):
    def draw_square(self):
        print('drawing square...')

    def draw_circle(self):
        print('drawing circle...')
        # DOESN'T MAKE SENSE


class Circle(Shape):
    def draw_square(self):
        print('drawing square...')
        # DOESN'T MAKE SENSE

    def draw_circle(self):
        print('drawing circle...')


# TO
        

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        print('drawing square...')


class Circle(Shape):
    def draw(self):
        print('drawing circle...')