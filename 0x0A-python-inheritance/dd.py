#!/usr/bin/python3

class GOGO:
    def __init__(self, width, height):
        self.deep = width
        self.long = height
    def __str__(self):
        return(f"[Rectangle] {self.deep}/{self.long}")
        
r = GOGO(2, 5)
print(r)
    