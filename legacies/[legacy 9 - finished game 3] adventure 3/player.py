"""
Panagiotis Torabi , Asher Arya, Hien Minh Le
Friday , May 13
R. Vincent , instructor
Final Project
"""

from inventory import *
from items import *

class Player(object):
    """Class representing a player"""
    def __init__(self, username='Player', hp = 10, damage = 1, xp = 0):
        """Initializes player name, max health, heal, base damage, inventory, killed enemies, experience and level"""
        self.name = username
        self.maxhealth = hp
        self.health = self.maxhealth
        self.bdamage = damage #base damage
        self.inventory = Inventory()
        self.enemies_killed = 0
        self.xp = xp
        self.level = xp//20

    def xpIncrease(self, xp):
        """Increases the player's experience points and levels the player up if they've reached enough experience"""
        self.xp += xp
        prevlevel = self.level
        self.level = xp//20
        if self.level > prevlevel:
            print("You levelled up! Level: {}. Health restored.".format(self.level))
            self._levelUp()

    def _levelUp(self):
        """Increases the player's max health and base damage by 1"""
        self.maxhealth += 1
        self.bdamage += 1
        self._heal(maxHeal = True)

    def damage_dealt(self):
        """Returns an integer of of the damage the player deals"""
        return int(self.bdamage) + int(self.inventory.weapon_damage())

    def damage_taken(self, true_damage):
        """Deals damage to the player. Returns boolean of if the player is dead or not"""
        actual_damage = true_damage - self.inventory.armor_resistance()
        if actual_damage>0:
            self.health = self.health - actual_damage
            return actual_damage
        return 0

        

    def is_dead(self):
        """Returns a boolean of if the player is dead or not. True if dead"""
        if self.health<=0:
            return True
        else:
            return False

    def _heal(self, healpower = 0, maxHeal = False):
        """Heals the player by a certain amount. maxHeal heals the player fully"""
        self.health = self.health + healpower
        if self.health > self.maxhealth or maxHeal == True:
            self.health = self.maxhealth
        return
    
    def consume_item(self, itemname):
        """Consumes an item and increases the player's health"""
        item_con = self.inventory.backpack.remove_item(itemname=itemname)
        healpower = item_con.heal
        self._heal(healpower=healpower)
        return

    def showLoot(self):
        """Returns a string of the player's equipped loot and backpack loot"""
        rep = "Equipped armor:\n"
        rep += self.inventory.showArmor()
        rep += "\nEquipped weapons:\n"
        rep += self.inventory.showWeapons()
        rep += '\nGear in backpack:\n'
        rep += self.inventory.showBackpack()
        return rep

    def showCHealth(self):
        """Returns a string of the player's current health"""
        return str(self.health)
    
    def showMHealth(self):
        """Returns a string of the player's maximum health"""
        return str(self.maxhealth)

    def showDamage(self):
        """Returns a string of the player's damage output"""
        return str(int(self.bdamage) + int(self.inventory.weapon_damage()))

    def showResistance(self):
        """Returns a string of the player's resistance"""
        return str(self.inventory.armor_resistance())

    def showName(self):
        """Returns the player's name"""
        return str(self.name)

    def __str__(self):
        """Returns the player name, level, maximum health, current health, damage, resistance and open backpack slots"""
        return '| {} | Level: {} | MHealth: {} | CHealth: {} | Damage: {} | Resistance: {} | Open Backpack Slots: {} |'.format(self.name, self.level, self.maxhealth, self.health, self.showDamage(), self.showResistance(), self.inventory.openSlots())
