"""
    in python functions are also object and referencable as object
    
    Rules: 
        python doesn't support multiple constructor
        instance member method always receives 'self' as first argument
        class member method @classmethod always receives 'cls' itself as first argument
        
        class attribute should be used with care especially collecion type: list, tuple etc 
        because for an attribute 'attr' of a class, and two instance a, b;  a.attr and b.attr 
        generally has the risk to refer same attr  
              
""" 

class Hero:
    title = "Normal Hero" # class attribute
    
    def __init__(self) -> None:
      self.team = []
      
  
    def add_partner(self, partner):
        self.team.append(partner)
        
    def attack(self, enemy):
        print(f"{self.title} is attacking:", enemy)  

 
    @classmethod
    def attackMinion(clz):
        print(f"any {clz.title} can attack the minion")
        pass

print("### Class Attribute can be overwritten by instance:")
punch_man = Hero()
punch_man.title = "Pnch Hero"
panty_man = Hero()
print(f"punch man's hero title: {punch_man.title}  but panty man's title is still: {panty_man.title}")

#lets set the name now
panty_man.title = "Panty hero"

print("### invoke method")
panty_man.attack("6 Eyed monster") # single parameter but instance method as two arg: self and other arg as required
# class can also invoke by passing instance as first argument in addition to other argument:
Hero.attack(panty_man, "Monster Hero Class despise")