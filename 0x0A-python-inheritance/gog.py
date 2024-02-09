#!/usr/bin/python3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
         return self.x == other.x and self.y == other.y

# Creating two Point objects
p1 = Point(1, 2)
p2 = Point(1, 2)

# Using the equality operator to compare the objects
print(p1 == p2)  # Output: True