class Items(object):
    def __init__(self):
        pass
    pass


class Consumables(Items):
    itemtype = 'Consumable'
    def __init__(self, itemname = "Consumable", itemsize = 'Small', instant_hp = 0, buff_type = None, buff_amount = 0):
        self.heal = instant_hp
        self.buff = (buff_type, buff_amount)
        self.name = itemname
        self.size = itemsize
    
    def __str__(self):
        rep = "| {} | ".format(self.name)
        if self.heal:
            rep += "Instant HP: {} | ".format(self.heal)
        if self.buff[0]:
            rep += "Buff Type: {}, Buff Strength: {} | ".format(self.buff[0], self.buff[1])
        return rep


class Armor(Items):
    itemtype = 'Armor'
    def __init__(self, equipslot = "Torso", itemname = 'Armor', stage = 1, resistance = None, charmslots = None):
        from math import exp
        from random import randint
        if resistance == None and charmslots == None:
            self.resistance = randint(0, int(stage)+1)
            self.charmslots = randint(0, round(6/(1+exp((-(1/2)*stage)+2)))) #1 at 1, 2 at 4, 3 at 6, maxes out at 6
        else:
            self.resistance = resistance
            self.charmslots = charmslots
        self.charms = ()
        self.name = itemname
        self.level = stage
        self.equipslot = equipslot

    def __str__(self):
        rep = "| {} | Slot: {} | Charmslots: {} | Resistance: {} |".format(self.name, self.equipslot, self.charmslots, self.resistance)
        if self.charmslots>0:
            rep += 'Charms: \n'
            for charm in self.charms:
                rep += str(charm) + '\n'
        return rep

    def addcharm(self, charm):
        if len(self.charms) < self.charmslots and self.charmslots:
            self.charms = tuple(list(self.charms).append(charm))
        else:
            raise ValueError('Charm overflow')

    def removecharm(self, charmname):
        """Remove a charm. Returns the charm object"""
        if len(self.charms) == 0:
            raise ValueError('Charm underflow')
        for charm in self.charms:
            if charm.name.lower() == charmname.lower():
                self.charms = tuple(list(self.charms).remove(charm))
                return charm


class Backpack(Items):
    itemtype = 'Backpack'
    def __init__(self, itemname = 'Backpack', stage = 1, starteritem = None):
        from random import randint
        from math import exp
        self.name = itemname
        self.size = randint(round(30/(1+exp((-(1/5)*stage)+2))), round(30/(1+exp((-(1/3)*stage)+2)))) #number between blah and blah, inclusive
        self.binventory = tuple()
        if starteritem:
            self.binventory = tuple(list(self.binventory).append(starteritem))
    
    def add_item(self, item):
        self.binventory = tuple(list(self.binventory).append(item))

    def remove_item(self, itemname): 
        if len(self.binventory) == 0:
            raise ValueError('Binventory underflow')
        for item in self.binventory:
            if item.name.lower() == itemname.lower():
                self.binventory = tuple(list(self.binventory).remove(item))
                return item

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





class Charm(Items):
    itemtype = 'Charm'
    def __init__(self, itemname = "Charm", buff_type = None, stage = 1):
        from random import randint
        from math import exp
        self.name = itemname
        buff_strength = randint(1, round(6/(1+exp((-(1/2)*stage)+2))))
        self.buff = (buff_type, buff_strength)

    def __str__(self):
        return "| {} | Buff: {} | Buff Strength: {} |".format(self.name, self.buff[0], self.buff[1])
        
class Weapon(Items):
    itemtype = 'Weapon'
    def __init__(self, itemname = "Weapon", stage = 1, damage = None):
        from random import randint
        from math import exp
        self.name = itemname
        if damage == None:
            self.damage = randint((30/(1+exp((-(1/5)*stage)))), (30/(1+exp((-(1/4)*stage)+2))))
        else:
            self.damage = damage
        self.equipslot = 'Hands'

    def __str__(self):
        return "| {} | Damage: {} |".format(self.name, self.damage)



