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

        #loot creater
        from items import weaponMaker, armorMaker, consumableMaker
        self.loot = []
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
        rep = "| {} | Health: {} | Damage: {} | ".format(self.name, self.health, self.damage)
        rep += "Loot: "
        for loot in self.loot:
            rep += str(loot) + ", "
        if not self.loot:
            rep += "None | "

        return rep

    def _is_dead(self):
        if self.hp<=0:
            return True
        else:
            return False
        
    def damage_dealt(self):
        return self.damage

    def damage_taken(self, true_damage):
        """Deals damage to the player. Returns boolean of if the enemy is dead or not"""
        self.health = self.health - (true_damage - self.resistance)
        self.resistance - 1
        return self._is_dead()

    
        