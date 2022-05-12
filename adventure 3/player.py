from inventory import *
from items import *

class Player(object):
    """Class representing a player"""
    def __init__(self, hp = 10, damage = 1):
        self.maxhealth = hp
        self.health = self.maxhealth
        self.bdamage = damage #base damage
        self.inventory = Inventory()

    def levelUp(self):
        self.maxhealth += 1
        self.bdamage += 1

    def damage_dealt(self):
        return self.bdamage + self.inventory.weapon_damage()

    def damage_taken(self, true_damage):
        self.health = self.health - (true_damage - self.inventory.armor_resistance())
        return 

    def is_dead(self):
        if self.health<=0:
            return True
        else:
            return False
