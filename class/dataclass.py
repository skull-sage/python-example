""" data class helps emulating d structure"""

from dataclasses import dataclass

@dataclass
class Human:
    name: str
    age: int
    score: float
    
    def __str__(self):
        return f"{self.name} is {self.age} years old and has score {self.score}"
    
chinese = Human("Xing Xang Pi", 12, 52)
korean = Human("Samsung", 222, 99.999999)
print(chinese)
print(korean)
