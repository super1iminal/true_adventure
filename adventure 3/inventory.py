class Equipped(object):
    def __init__(self):
        self.chest = None
        self.arms = None
        self.legs = None
        self.rhand = None
        self.lhand = None
        self.head = None
    def equip(self, location, item):
        previtem = self.location
        self.location = item
        return previtem
    def unequip(self, location):
        previtem = self.location
        self.location = None
        return previtem

class Inventory(object):
    def __init__(self, inventory):
        self.inventory = [] #[item1, item2, item3]
        self.equipment = Equipped()
        self.gold = 0
    def equipItem(self, item):
        if self.equipment.item.location:
            self.inventory.append(self.equipment.item.location)
            self.equipment.item.location = item
        else:
            self.equipment.item.location = item
    
    def __repr__(self):
        representation = ''
        representation += ('Gold: ' + str(self.gold))
        for locat in ('chest')
        for item in self.inventory:
            representation += item
            representation += '\n'
            
        return 
            
            
            
        
class Item(object):
    def __init__(self, location):
        self.location = location
        