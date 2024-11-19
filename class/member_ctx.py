# sub class __init__ will overwrite super __init__
# method without self is class's static method


class Hero:
  heroName = "Base Hero"

  def __init__(self, name='Hero Instance'):  # this is python constructor
    self.name = name
    self.role = 'To Duck the universe'

  # first argument is always this (self) invoking instance
  # allow accessing class data fields
  def attackEvil(self, evilMan):
    print(self.name, "attacks ", evilMan)

  @classmethod
  def setCtxName(cls, name):
    cls.heroName = name


aHero = Hero()
aHero.heroName = "Instance Hero"

# global access to heroName
print(Hero.heroName)  # print "this is class global"
print(aHero.heroName)  # print "this is instance global"

# Arbitrary property declaration is not supported in python
# manObj.arbitrary = "This is compile time error"

aHero.attackEvil("Thanos")


class SuperMan(Hero):

  def setRole(self):
    # without super().__init()__ member varialbe remain undefined
    #super().__init__()
    self.role = " to destroy the sun"


sonObj = SuperMan("Monkey Luffy")
sonObj.setRole()
print(sonObj.name, "has role: ", sonObj.role)

SuperMan.setCtxName("Super Man")
print(f"{SuperMan.heroName} is no {Hero.heroName} ?")
