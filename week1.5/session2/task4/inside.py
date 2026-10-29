# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
from geometry import Circle, Point

point = Point(5,5)
circle = Circle(10, Point(10,10))
print(f"point {point} is{" " if point in circle else " not "}in circle {circle}")