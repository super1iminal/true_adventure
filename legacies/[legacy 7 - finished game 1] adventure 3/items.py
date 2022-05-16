def weaponMaker(stage):
    from name_gen import weapon_gen
    return Weapon(itemname = weapon_gen(), stage = stage)

def armorMaker(stage, location):
    """Helmet, Torso, Arms, Legs"""
    from name_gen import armor_gen
    return Armor(equipslot=location, itemname=armor_gen(location), stage = stage)

def consumableMaker(stage):
    from name_gen import consumable_gen
    return Consumable(itemname=consumable_gen(), stage = stage)



class Items(object):
    def __init__(self):
        pass
    pass


class Consumable(Items):
    itemtype = 'Consumable'
    def __init__(self, itemname = "Consumable", stage = 1, instant_hp = None):
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
        from math import exp
        from random import randint
        if resistance == None:
            self.resistance = randint(1, stage + 5)
        else:
            self.resistance = resistance
        self.charms = ()
        self.name = itemname
        self.level = stage
        self.equipslot = equipslot

    def __str__(self):
        rep = "| {} | Slot: {} | Resistance: {} |".format(self.name, self.equipslot, self.resistance)
        return rep


class Backpack(Items):
    itemtype = 'Backpack'
    def __init__(self, itemname = 'Backpack', stage = 1, starteritem = None):
        from random import randint
        from math import exp
        self.name = itemname
        self.size = randint(1, stage+5) #number between blah and blah, inclusive
        self.binventory = list()
        if starteritem:
            self.binventory = self.binventory + [starteritem]
    
    def add_item(self, item):
        self.binventory += [item]

    def remove_item(self, itemname): 
        for item in self.binventory:
            if str(item.name).lower() == str(itemname).lower():
                self.binventory.remove(item)
                return item
        return None

    def is_over(self):
        if len(self.binventory) > self.size:
            return True
        else:
            return False
    
    def __str__(self):
        rep = "| {} | Slot: {} | Charmslots: {} | Resistance: {} |"
        if self.charmslots>0:
            rep += 'Charms: \n'
            for charm in self.charms:
                rep += str(charm) + '\n'
        rep += 'Items: \n'
        for item in self.binventory:
            rep += str(item) + '\n'

        
class Weapon(Items):
    itemtype = 'Weapons'
    def __init__(self, itemname = "Weapon", stage = 5, damage = None):
        from random import randint
        self.name = itemname
        if damage == None:
            self.damage = randint(1,stage+5)
        else:
            self.damage = damage
        self.equipslot = 'Hands'

    def __str__(self):
        return "| {} | Damage: {} |".format(self.name, self.damage)



