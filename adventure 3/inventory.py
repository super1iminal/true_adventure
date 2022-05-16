"""
Panagiotis Torabi , Asher Arya, Hien Minh Le
Friday , May 13
R. Vincent , instructor
Final Project
"""
from items import *

class Inventory(object):
    def __init__(self):
        self.equipped = {'Armor': {'Head': None, 'Torso': Armor('Torso', 'Leather Chestpiece', 1, resistance = 1), 'Arms': None, 'Legs': Armor('Legs', 'Ripped Pants', 1, resistance = 1)}, 
                            'Weapons': {'RHand': None, 'LHand': None}}
        self.backpack = Backpack(itemname = "Toad's Backpack", starteritem = consumableMaker(2))


    def checknames(self):
        armornames = {}
        weaponnames = {}
        for itemtype in self.equipped:
            for location in self.equipped[itemtype]:
                if self.equipped[itemtype][location]!=None:
                    armornames[location] = self.equipped[itemtype][location].name
        return {'Armor': armornames, 'Weapons': weaponnames}

    def equip(self, itemname = None,):
        item = self.backpack.remove_item(itemname)
        if item.itemtype == 'Weapons':
            if self.equipped[item.itemtype]['RHand'] and self.equipped[item.itemtype]['LHand']:
                print('Both of your hands are equipped: ')
                print(self.showWeapons())
                choice = input('What hand would you like to equip the weapon in? (right/left): ').strip().lower()
                if choice == 'right':
                    self.backpack.add_item(self.equipped[item.itemtype]['RHand'])
                    ('{} put in backpack and {} equipped in right hand'.format(self.equipped['Weapons']['RHand'].name, item.name))
                    self.equipped[item.itemtype]['RHand'] = item
                if choice == 'left':
                    self.backpack.add_item(self.equipped[item.itemtype]['LHand'])
                    ('{} put in backpack and {} equipped in left hand'.format(self.equipped['Weapons']['LHand'].name, item.name))
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
                self.backpack.add_item(self.equipped[item.itemtype][item.equipslot])
                self.equipped[item.itemtype][item.equipslot] = item
                print('{} put in backpack and {} equipped on {}'.format(self.equipped[item.itemtype][item.equipslot].name, item.name, item.equipslot))
            else:
                self.equipped[item.itemtype][item.equipslot] = item
                print('{} equipped on {}'.format(item.name, item.equipslot))

    def drop(self, itemname, tile):
        tile.loot += [(self.backpack.remove_item(itemname))]
    
    def openSlots(self):
        opnslots = self.backpack.size - len(self.backpack.binventory)
        if opnslots > 0:
            return opnslots
        else:
            return 0

    def weapon_damage(self):
        damage = 0
        for location in self.equipped['Weapons']:
            if self.equipped['Weapons'][location]!=None:
                damage += self.equipped['Weapons'][location].damage
        return damage

    def armor_resistance(self):
        resistance = 0
        for location in self.equipped['Armor']:
            if self.equipped['Armor'][location]!=None:
                resistance += self.equipped['Armor'][location].resistance
        return resistance

    def showArmor(self):
        return "-Head: {}\n-Torso: {}\n-Arms: {}\n-Legs: {}".format(str(self.equipped['Armor']['Head']), str(self.equipped['Armor']['Torso']), str(self.equipped['Armor']['Arms']), str(self.equipped['Armor']['Legs']))

    def showWeapons(self):
        return "-RHand: {}\n-LHand: {}".format(str(self.equipped['Weapons']['RHand']), str(self.equipped['Weapons']['LHand']))

    def showBackpack(self):
        rep = ""
        for item in self.backpack.binventory:
            rep += "-" + str(item) + "\n"
        if not rep:
            rep = 'None.'
        return rep

        



            










