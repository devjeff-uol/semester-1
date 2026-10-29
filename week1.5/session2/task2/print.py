# Week 1.5, Session 2: Task 2

# Write code here to create and print a Point object,
# then create and print a Circle object

import geometry as geo
point = geo.Point(5.0, 5.0) 
circle = geo.Circle(20, point)

print(f"point: {point}")
print(f"circle: {circle}")