import math

# area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# area of a rectangle
def area_of_rectangle(length, width):
    return length * width

# area of a circle
def area_of_circle(radius):
    """Returns the area of a circle given its radius."""
    return math.pi * radius ** 2

# perimeter of a rectangle
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

# circumference of a circle
def circumference_of_circle(radius):
    """Returns the circumference of a circle given its radius."""
    return 2 * math.pi * radius

# perimeter of a triangle
def perimeter_of_triangle(side1, side2, side3):
    return side1 + side2 + side3
