"""
namedtuple() function allows to create a named tuple where items of tuple 
can be accessed with name instead of positinal index(i.e., [idx]) 
"""
from collections import namedtuple

# Point = namedtuple("Point", ("x", "y")) # better approach to use ["x", "y"]
#or 
Point = namedtuple("Point", "x, y")
point = Point(10, 30)

print(f"access by position: [0]={point[0]} [1]={point[1]}")
print(f"access by key: x={point.x}, y={point.y}")

