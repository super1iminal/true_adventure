#we need enemy item drop randomizer
class Enemy(object):
    def __init__(self, name, hp, damage, loot, resistance = 0):
        self.health = hp
        self.damage = damage
        self.loot = loot
        self.resistance = resistance
        self.name = name
    
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
        return self._is_dead()

    

    
        