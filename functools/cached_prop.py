from functools import cached_property

class SillyHero:
    def __init__(self, factorialPower):
        self.factorialPower = factorialPower
        pass
    
    @cached_property
    def power(self):
        power = 1
        print(" Not Cached! Lets Compute factorial power once")
        for idx in range(1, self.factorialPower+1):
            power = power * idx
        
        return power
    
silly_instance = SillyHero(5)
# without @cached_property decorator, "power" prop work as a getter function/read only prop
print("Silly can kill all the enemy whose life ≤ :", silly_instance.power)

print("Silly can kill all the enemy whose life ≤ :", silly_instance.power)


    

    