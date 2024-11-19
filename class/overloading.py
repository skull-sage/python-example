class SuperMan:

  def __init__(self, powerPoint=(10, 20)) -> None:
    self.trueName = 'Rashed'
    self.grandEnemy = 'Purple Thanos'
    self.powerPoint = powerPoint

  # overloading toString for print
  def __str__(self):
    return "%s has enemy %s with power %s"   % (self.trueName, self.grandEnemy, self.powerPoint)

  def __add__(self, other):
    # trying tupple addition
    newPower = tuple( x + y 
                     for x, y in zip(self.powerPoint, other.powerPoint))
    return SuperMan(newPower)

aMan = SuperMan()
powerMan = SuperMan((100, 100))

poweredUp1 = aMan + powerMan
poweredUp2 = powerMan + aMan;

print(" POWER ADDED ")
print(poweredUp1)
print(poweredUp2)
