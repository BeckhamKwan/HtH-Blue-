
import random


class Armor: 
    def __init__(self, name, max_block):
        self.name = name
        self.max_damage = max_block
        
    def block(self):
        
        return random.randint(0, self.max_block)
    
if __name__ == "__main__":
    shield = Armor("shield", 50)
        
    print(shield.block())