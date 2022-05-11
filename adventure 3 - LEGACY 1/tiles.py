

class Level(object):
    """Class that represents a level. Generated once per level."""
    class Tile(object):
        """Class that represents a tile. Generated level + 3 times per level"""
        def __init__(self):
            self.paths = {'n': None, 's': None, 'e': None, 'w': None}
            self.enemies = ()
            self.location = ''

        def __str__(self):
            rep = "Location: {}, ".format(self.location)
            rep += "Enemies: "
            for enemy in self.enemies:
                rep += (str(enemy) + ", ")
            rep += 'Paths: '
            for path in self.paths:
                if self.paths[path]!=None:
                    rep += (path + ', ')

            return rep

        def __add__(self, other):
            if len(self.enemies)>len(other.enemies):
                return self
            else:
                return other

    def __init__(self, stage): #stage starts at 0? or 1? whatever
        from random import randint
        self.center_tile = Level.Tile()
        iterations = randint(1, int(stage) + 2)
        #number of iterations around center
        for _ in range(iterations):
            
        

        
