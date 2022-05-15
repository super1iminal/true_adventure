def enemyMaker(stage, en_type = 'Enemy'):
    """Boss or Enemy. Default is enemy"""
    from name_gen import enemy_gen
    return Enemy(name = enemy_gen(en_type), stage = stage, en_type = en_type)


class Enemy(object):
    def __init__(self, name, stage, en_type = "Enemy"):
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
        self.damage = randint(1, stage+1) + multiplier
        self.xp = self.health + self.damage

        #loot creater
        from items import weaponMaker, armorMaker, consumableMaker
        self.loot = list()
        for _ in range(randint(0, stage + (multiplier))):
            choice = randint(1,3)
            if choice==1:
                self.loot.append(weaponMaker(stage))
            if choice==2:
                self.loot.append(consumableMaker(stage))
            if choice==3:
                location = ['Head', 'Torso', 'Arms', 'Legs'][randint(0, 3)]
                self.loot.append(armorMaker(stage, location))
    
    def __str__(self):
        return "{} (Health: {}, Damage: {})".format(self.name, self.health, self.damage)

    def showLoot(self):
        rep = "{}'s loot: ".format(self.name)
        if len(self.loot)==0:
            rep += 'None.'
            return rep
        else:
            for loot in self.loot:
                rep += "\n" + str(loot)
        return rep


    def is_dead(self):
        if self.health<=0:
            return True
        else:
            return False
        
    def damage_dealt(self):
        return int(self.damage)

    def damage_taken(self, true_damage):
        """Deals damage to the player. Returns boolean of if the enemy is dead or not"""
        self.health = self.health - (true_damage - self.resistance)
        self.resistance - 1
        return self.is_dead()

    def showHealth(self):
        return str(self.health)

    def showDamage(self):
        return str(self.damage)

    def showName(self):
        return str(self.name)

    def showResistance(self):
        return str(self.resistance)

    
        