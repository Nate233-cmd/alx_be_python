import math

# Base Class
class Shape:
    """Base class for all shapes."""

    def area(self):
        """Calculate area of the shape. Must be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method")


# Derived Class - Rectangle
class Rectangle(Shape):
    """Rectangle shape with length and width."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of the rectangle."""
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    """Circle shape with a radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of the circle."""
        return math.pi * self.radius ** 2
