# hero.py
#Beckham Kwan


import random

from Ability import Ability

from Armor import Armor



class Hero:
 
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
   
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armors = []
        self.abilities = []

    def battle(self, opponent):
    # '''Fight another hero and randomly declare a winner'''
        print(f"{self.name} is attacking {opponent.name}")
        
        winner = random.choice([self.name, opponent])
 
        print(f"The winner of this battle is {winner}")


    def add_ability(self ,ability):

        self.abilities.append(ability)

        print(f"{ability.name} has added to {self.name}'s list") 


    def sum_of_attacks(self):

        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage  
    
    
    def add_armor(self ,armor):
        
        self.armor.append(armor)
        
        print(f"{armor.name} has added to {self.name}'s list") 

    def defend(self):
         
        total_block = 0

        for armor in self.armors:
            total_block += armor.block()
        return total_block 

if __name__ == "__main__":
        my_hero1 = Hero("Kaiser", 200)
        my_hero2 = Hero("Isagi", 200)
print(my_hero1.name)
print(my_hero1.current_health)

print(my_hero2.name)
print(my_hero2.current_health)


  
my_hero2.battle(my_hero1) 

    