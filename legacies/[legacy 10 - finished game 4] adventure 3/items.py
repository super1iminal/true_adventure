"""
Panagiotis Torabi , Asher Arya, Hien Minh Le
Friday , May 13
R. Vincent , instructor
Final Project
"""

def weaponMaker(stage):
    """Generates a weapon based on stage. Automatically generates name"""
    from name_gen import weapon_gen
    return Weapon(itemname = weapon_gen(), stage = stage)

def armorMaker(stage, location):
    """Generates armor based on stage and location. Location can be Head, Torso, Arms or Legs. Automatically generates name."""
    from name_gen import armor_gen
    return Armor(equipslot=location, itemname=armor_gen(location), stage = stage)

def consumableMaker(stage):
    """Generates a consumable based on stage. Automatically generates name"""
    from name_gen import consumable_gen
    return Consumable(itemname=consumable_gen(), stage = stage)



class Items(object):
    def __init__(self):
        """Create an item. DO NOT USE DIRECTLY"""
        pass
    pass


class Consumable(Items):
    itemtype = 'Consumable'
    def __init__(self, itemname = "Consumable", stage = 1, instant_hp = None):
        """Create a consumable. Initiales name, stage, and healin power"""
        from random import randint
        if instant_hp==None:
            self.heal = randint(1, stage+10)
        else:
            self.heal = instant_hp
        self.name = itemname
    
    def __str__(self):
        rep = "| {} | Heal: {} |".format(self.name, self.heal)
        return rep


class Armor(Items):
    itemtype = 'Armor'
    def __init__(self, equipslot = "Torso", itemname = 'Armor', stage = 1, resistance = None):
        """Create an armor object. Initializes equipslot, name, resistance and level"""
        from random import randint
        if resistance == None:
            self.resistance = randint(1, stage + 5)
        else:
            self.resistance = resistance
        self.name = itemname
        self.level = stage
        self.equipslot = equipslot

    def __str__(self):
        """Returns string of armor name, equipslot and resistance"""
        rep = "| {} | Slot: {} | Resistance: {} |".format(self.name, self.equipslot, self.resistance)
        return rep


class Backpack(Items):
    itemtype = 'Backpack'
    def __init__(self, itemname = 'Backpack', stage = 1, starteritem = None):
        """Create backpack object. Initializes backpack inventory, name, size, and puts starter item in inventory if set"""
        from random import randint
        self.name = itemname
        self.size = randint(4, stage+5) #number between blah and blah, inclusive
        self.binventory = list()
        if starteritem:
            self.binventory = self.binventory + [starteritem]
    
    def add_item(self, item):
        """Adds an item to the backpack"""
        self.binventory += [item]

    def remove_item(self, itemname): 
        """Removes an item from the backpack based on item name"""
        for item in self.binventory:
            if str(item.name).lower() == str(itemname).lower():
                self.binventory.remove(item)
                return item
        return None

    def is_over(self):
        """Checks if the backpack is over capacity. True if over capacity"""
        if len(self.binventory) > self.size:
            return True
        else:
            return False

        
class Weapon(Items):
    itemtype = 'Weapons'
    def __init__(self, itemname = "Weapon", stage = 5, damage = None):
        """Create a weapon. Initializes name, level, damage and equipslot"""
        from random import randint
        self.name = itemname
        if damage == None:
            self.damage = randint(1,stage+5)
        else:
            self.damage = damage
        self.equipslot = 'Hands'

    def __str__(self):
        """Returns weapon name and damage"""
        return "| {} | Damage: {} |".format(self.name, self.damage)



