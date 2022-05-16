"""
Panagiotis Torabi , Asher Arya, Hien Minh Le
Friday , May 13
R. Vincent , instructor
Final Project
"""
from items import *

class Inventory(object):
    def __init__(self):
        """Initializes equipped items and backpack. By default, armor on the torso and legs is equipped, and a stage 2 consumable is placed in the backpack"""
        self.equipped = {'Armor': {'Head': None, 'Torso': Armor('Torso', 'Leather Chestpiece', 1, resistance = 1), 'Arms': None, 'Legs': Armor('Legs', 'Ripped Pants', 1, resistance = 1)}, 
                            'Weapons': {'RHand': None, 'LHand': None}}
        self.backpack = Backpack(itemname = "Toad's Backpack", starteritem = consumableMaker(2))

    def equip(self, itemname = None,):
        """Equips an item by name. If an item is already equipped in that slot, it replaces it and places the existing item in the backpack"""
        item = self.backpack.remove_item(itemname)
        if item.itemtype == 'Weapons':
            if self.equipped[item.itemtype]['RHand'] and self.equipped[item.itemtype]['LHand']:
                print('Both of your hands are equipped: ')
                print(self.showWeapons())
                choice = input('What hand would you like to equip the weapon in? (right/left): ').strip().lower()
                if choice == 'right':
                    ('{} put in backpack and {} equipped in right hand'.format(self.equipped['Weapons']['RHand'].name, item.name))
                    self.backpack.add_item(self.equipped[item.itemtype]['RHand'])
                    self.equipped[item.itemtype]['RHand'] = item
                if choice == 'left':
                    ('{} put in backpack and {} equipped in left hand'.format(self.equipped['Weapons']['LHand'].name, item.name))
                    self.backpack.add_item(self.equipped[item.itemtype]['LHand'])
                    self.equipped[item.itemtype]['LHand'] = item
                else:
                    print('invalid choice')
            else:
                if self.equipped[item.itemtype]['RHand']:
                    print(f'{item.name} equipped in left hand')
                    self.equipped[item.itemtype]['LHand'] = item
                else:
                    print(f'{item.name} equipped in right hand')
                    self.equipped[item.itemtype]['RHand'] = item

        if item.itemtype == 'Armor':
            if self.equipped[item.itemtype][item.equipslot] != None:
                print('{} put in backpack and {} equipped on {}'.format(self.equipped[item.itemtype][item.equipslot].name, item.name, item.equipslot))
                self.backpack.add_item(self.equipped[item.itemtype][item.equipslot])
                self.equipped[item.itemtype][item.equipslot] = item
            else:
                self.equipped[item.itemtype][item.equipslot] = item
                print('{} equipped on {}'.format(item.name, item.equipslot))

    def drop(self, itemname, tile):
        """Drops an item on a designated tile and removes it from the player backpack"""
        tile.loot += [(self.backpack.remove_item(itemname))]
    
    def openSlots(self):
        """Returns an integer of the number of open slots in the player backpack"""
        opnslots = self.backpack.size - len(self.backpack.binventory)
        if opnslots > 0:
            return opnslots
        else:
            return 0

    def weapon_damage(self):
        """Returns an integer of the  damage of the equipped weapons"""
        damage = 0
        for location in self.equipped['Weapons']:
            if self.equipped['Weapons'][location]!=None:
                damage += self.equipped['Weapons'][location].damage
        return damage

    def armor_resistance(self):
        """Returns an integer of the resistance of the equipped armor"""
        resistance = 0
        for location in self.equipped['Armor']:
            if self.equipped['Armor'][location]!=None:
                resistance += self.equipped['Armor'][location].resistance
        return resistance

    def showArmor(self):
        """Returns a string of all equipped armor"""
        return "-Head: {}\n-Torso: {}\n-Arms: {}\n-Legs: {}".format(str(self.equipped['Armor']['Head']), str(self.equipped['Armor']['Torso']), str(self.equipped['Armor']['Arms']), str(self.equipped['Armor']['Legs']))

    def showWeapons(self):
        """Returns a string of all equipped weapons"""
        return "-RHand: {}\n-LHand: {}".format(str(self.equipped['Weapons']['RHand']), str(self.equipped['Weapons']['LHand']))

    def showBackpack(self):
        """Returns a string of all items in backpack"""
        rep = ""
        for item in self.backpack.binventory:
            rep += "-" + str(item) + "\n"
        if not rep:
            rep = 'None.'
        return rep

        



            










