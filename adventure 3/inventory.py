from items import *

class Inventory(object):
    def __init__(self):
        self.equipped = {'Armor': {'Head': None, 'Torso': Armor('Torso', 'Leather Chestpiece', 1, 1), 'Arms': None, 'Legs': Armor('Legs', 'Ripped Pants', 1, 1)}, 
                            'Weapons': {'RHand': Weapon(itemname = "Lilith"), 'LHand': None}}
        self.backpack = Backpack(itemname = "Toad's Backpack", starteritem = consumableMaker(2))


    def checknames(self):
        armornames = {}
        weaponnames = {}
        for itemtype in self.equipped:
            for location in self.equipped[itemtype]:
                if self.equipped[itemtype][location]!=None:
                    armornames[location] = self.equipped[itemtype][location].name
        return {'Armor': armornames, 'Weapons': weaponnames}

    def unequip(self, itemname = None, item_location = None):
        if itemname == None and location == None:
            raise ValueError("No location/item specified to uneequip")
        elif itemname!= None:
            armorweapon_d = Inventory.checknames()
            for itemtype in armorweapon_d:
                for location in armorweapon_d[itemtype]:
                    if armorweapon_d[itemtype][location] == itemname:
                        item = self.equipped[itemtype][location]
                        self.equipped[itemtype][location] = None
                        self.backpack.add_item(item)
                        return
            raise ValueError('You either do not have that weapon equipped or it is an invalid name')
        elif location!=None:
            for itemtype in self.equipped:
                for location in self.equipped[itemtype]:
                    if item_location == location:
                        if self.equipped[itemtype][location]!=None: #if theres actually an item there
                            item = self.equipped[itemtype][location]
                            self.equipped[itemtype][location] = None
                            self.backpack.add_item(item)
                            return
                        else:
                            raise ValueError('There is no item equipped there')
            raise ValueError('Invalid location')

    def equip(self, itemname = None,):
        if itemname == None:
            raise ValueError('No item name specified to equip')
        item = self.backpack.remove_item(itemname)
        for itemtype in self.equipped:
            if item.itemtype == itemtype:
                for location in self.equipped[itemtype]:
                    if item.equipslot == location:
                        if self.equipped[itemtype][location] == None:
                            self.equipped[itemtype][location] = item
                        else: #if theres already an item equipped just switch it with the one in the backpack
                            equippeditem = self.equipped[itemtype][location]
                            self.backpack.add_item(equippeditem)
                            self.equipped[itemtype][location] = item

    def drop(self, itemname, tile):
        tile.loot.append(self.backpack.remove_item(itemname))

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

        



            










