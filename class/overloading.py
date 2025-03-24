"""
  Following operator overloading is supported: 
  Addition	            p1 + p2	    p1.__add__(p2)
  Subtraction	          p1 - p2	    p1.__sub__(p2)
  Multiplication	      p1 * p2	    p1.__mul__(p2)
  Power	                p1 ** p2	  p1.__pow__(p2)
  Division	            p1 / p2	    p1.__truediv__(p2)
  Floor Division	      p1 // p2	  p1.__floordiv__(p2)
  Remainder (modulo)	  p1 % p2	    p1.__mod__(p2)
"""

class GameChar:
  def __init__(self, name, diffence):
    self.name = name
    self.diffence = diffence
    self.attack_power = 50
    
  def __add__(self, attack_power):
    self.attack_power += attack_power
    print("Power up: ", self.attack_power)
    return self
  
  def __truediv__(self, scale):
    self.attack_power /= scale
    
  def __floordiv__(self, scale):
    self.attack_power //= scale
    
  def __sub__(self, attack_power):
    self.attack_power -= attack_power
    print("Power down: ", self.attack_power)
    return self
    
  def attack(self, enemy: 'GameChar'):
    if(enemy.diffence >= self.attack_power):
      print(f"Urrgh! {enemy.name} is too strong to get a scratch")
    else:
      print(f"Yah ha ha! {enemy.name} is dead")
  
    pass
  #class GameChar
  
fire_hero = GameChar("Fire Bistral", 50)
minion = GameChar("minion", 40)
boss = GameChar("mini-boss", 60)

fire_hero.attack(minion)
fire_hero.attack(boss)

fire_hero = fire_hero + 20
fire_hero.attack(boss)

fire_hero = fire_hero - 50
fire_hero.attack(minion)
 