##
import math

def distance(a, b):
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)
#example
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = Point(1, 2)
b = Point(4, 6)
print(distance(a, b))  
