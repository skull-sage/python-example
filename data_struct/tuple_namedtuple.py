"""
namedtuple() function allows to create a named tuple where items of tuple 
can be accessed with name instead of positinal index(i.e., [idx]) 
"""
from collections import namedtuple

Pos = namedtuple("Pos", ["x", "y"])

pos = Pos(10, 20)

print("positional access", pos[0] + pos[1]) 
print(f"named acces: x:{pos.x} y:{pos.y}")

x, y = pos
