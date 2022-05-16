"""
Panagiotis Torabi , Asher Arya, Hien Minh Le
Friday , May 13
R. Vincent , instructor
Final Project
"""


def enemyMaker(stage, en_type = 'Enemy'):
    """Boss or Enemy. Default is enemy"""
    from name_gen import enemy_gen
    return Enemy(name = enemy_gen(en_type), stage = stage, en_type = en_type)


class Enemy(object):
    def __init__(self, name, stage, en_type = "Enemy"):
        """Create an enemy, initializes typem name, health, damage, xp reward, and loot"""
        from random import randint
        self.en_type = en_type
        self.name = name

        if self.en_type == 'Enemy':
            multiplier = 0
            self.resistance = 0
        else:
            multiplier = stage + 3
            self.resistance = randint(0, stage+2)
        self.health = randint(1, stage+3) + multiplier
        self.damage = randint(3, stage+3) + multiplier
        self.xp = self.health + self.damage

        #loot creater
        from items import weaponMaker, armorMaker, consumableMaker
        self.loot = list()
        for _ in range(randint(1, stage + (multiplier))):
            choice = randint(1,3)
            if choice==1:
                self.loot.append(weaponMaker(stage))
            if choice==2:
                self.loot.append(consumableMaker(stage))
            if choice==3:
                location = ['Head', 'Torso', 'Arms', 'Legs'][randint(0, 3)]
                self.loot.append(armorMaker(stage, location))
    
    def __str__(self):
        """Returns a string of enemy name, health, damage and resistance"""
        return "{} (Health: {}, Damage: {}, Resistance: {})".format(self.name, self.health, self.damage, self.resistance)

    def showLoot(self):
        """Returns a list of the enemy's loot"""
        rep = "{}'s loot: ".format(self.name)
        if len(self.loot)==0:
            rep += 'None.'
            return rep
        else:
            for loot in self.loot:
                rep += "\n-" + str(loot)
        return rep


    def is_dead(self):
        """Returns a boolean as to if the enemy is dead or not. True if dead"""
        if self.health<=0:
            return True
        else:
            return False
        
    def damage_dealt(self):
        """Returns an integer of the damage the enemy deals"""
        return int(self.damage)

    def damage_taken(self, true_damage):
        """Deals damage to the enemy. Returns boolean of if the enemy is dead or not"""
        self.resistance += -1
        actual_damage = true_damage - self.resistance
        if actual_damage > 0:
            self.health = self.health - actual_damage
            return actual_damage
        return 0

    def showHealth(self):
        """Returns a string of the enemy's health"""
        return str(self.health)

    def showDamage(self):
        """Returns a string of the enemy's damage"""
        return str(self.damage)

    def showName(self):
        """Returns a string of the enemy's name"""
        return str(self.name)

    def showResistance(self):
        """Returns a string of the enemy's resistance"""
        return str(self.resistance)

    
        