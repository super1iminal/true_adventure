from inventory import *
from items import *

class Player(object):
    """Class representing a player"""
    def __init__(self, username='Player', hp = 10, damage = 1, xp = 0):
        self.name = username
        self.maxhealth = hp
        self.health = self.maxhealth
        self.bdamage = damage #base damage
        self.inventory = Inventory()
        self.enemies_killed = 0
        self.xp = xp
        self.level = round(xp/20)

    def xpIncrease(self, xp):
        self.xp += xp
        prevlevel = self.level
        self.level = round(xp/20)
        if self.level > prevlevel:
            self._levelUp()

    def _levelUp(self):
        self._heal(maxHeal = True)
        self.maxhealth += 1
        self.bdamage += 1

    def damage_dealt(self):
        return self.bdamage + self.inventory.weapon_damage()

    def damage_taken(self, true_damage):
        """Deals damage to the player. Returns boolean of if the player is dead or not"""
        self.health = self.health - (true_damage - self.inventory.armor_resistance())
        return self._is_dead()

    def _is_dead(self):
        if self.health<=0:
            return True
        else:
            return False

    def killed_enemy(self):
        self.enemies_killed += 1

    def _heal(self, healpower = 0, maxHeal = False):
        self.health = self.health + healpower
        if self.health > self.maxhealth or maxHeal == True:
            self.health = self.maxhealth
        return
    
    def consume_item(self, itemname):
        item_con = self.inventory.backpack.remove_item(itemname=itemname)
        healpower = item_con.heal
        self._heal(healpower=healpower)
        return

    def showCHealth(self):
        return str(self.health)
    
    def showMHealth(self):
        return str(self.maxhealth)

    def showDamage(self):
        return str(self.bdamage) + int(self.inventory.weapon_damage())

    def showResistance(self):
        return str(self.inventory.armor_resistance())

    def showName(self):
        return str(self.name)

    def __str__(self):
        return '| {} | Max Health: {} | Current Health: {} | Base Damage: {} | Total Damage with Weapons: {} |'.format(self.name, self.maxhealth, self.health, self.bdamage, Player.damage_dealt())
