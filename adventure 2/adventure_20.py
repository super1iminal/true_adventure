class Stats(object):
    def __init__(self, strength = 1, perception = 0, endurance = 1, charisma = 0, intelligence = 1, agility = 1, luck = 0):
        stats = (strength, perception, endurance, charisma, intelligence, agility, luck)
    def __add__(self, x):
        return tuple([v+x for v in self.stats])
    def __repr__(self) -> str:
        return zip(('Strength', 'Perception', 'Endurance', 'Charisma', 'Intelligence', 'Agility', 'Luck'),self.stats)
        

class Player():
    def __init__(self, freepoints = 14):
        player_stats = Stats(10, 10, 10, 10, 10, 10, 10)
        freepoints = freepoints
        
class Enemy():
    def __init__(self):
        stats = Stats()
        name = "Justin Fisher"
    def stats_adjuster(self, level, loop):
        self.stats += (level*loop)
    def __repr__(self):
        return "Name: " + self.name + "Stats: " + str(self.stats)
        
class Boss():
    def __init__(self):
        stats = Stats()
        name = "DBU"
    def stats_adjuster(self, level, loop):
        self.stats += (loop**2)
        
        
    
    
class Game():
    loop = 1
    level = 1
    def enemyMaker(self, lvl=level, lop=loop):
        enemy = Enemy()
        enemy.stats_adjuster(lvl, lop)
        return enemy
    class Room():
        def __init__(self):
            enemies = []
            interactables = []
            items = []
            room_n = None
            room_e = None
            room_w = None
            room_s = None
    class BossRoom():
        def __init__(self):
            room = Game.Room()
            bosses = []
            from math import log10
            for _ in range(Game.level*log10(Game.level)):
                room.enemies += [Game.enemyMaker]
            
            
    class ItemRoom():
        def __init__(self):
            room = Game.Room()
        def itemmaker(self):
                
                
               
           
            
        
        
            
            
