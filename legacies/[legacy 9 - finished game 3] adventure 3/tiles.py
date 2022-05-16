"""
Panagiotis Torabi , Asher Arya, Hien Minh Le
Friday , May 13
R. Vincent , instructor
Final Project
"""

from random import randint
from enemies import *

class Level(object):
    """Class that represents a level/floor"""
    class Tile(object):
        """Class that represents a tile. Generated level + 3 times per level"""
        def __init__(self, direction_from_previous = None, previousTile = None, location = '', pathto = '', tiletype = 'Enemy', stage = 1):
            self.tiletype = tiletype
            self.paths = {'n': None, 's': None, 'e': None, 'w': None}
            if direction_from_previous!=None:
                self.direction_to_previous = Level.Tile.antipath(direction_from_previous)
            else:
                self.direction_to_previous = None
            #creating link to tile that came before
            if previousTile != None and direction_from_previous!=None:
                self.paths[Level.Tile.antipath(direction_from_previous)] = previousTile
            #generating enemies. temporary until enemies are actually coded
            self.enemies = list()
            if tiletype=='Enemy':
                for _ in range(randint(1, stage+1)):
                    self.enemies.append(enemyMaker(stage))
            elif tiletype == 'Boss':
                self.enemies.append(enemyMaker(stage, "Boss"))
            self.loot = list()
            
            #LOCATIONS
            self.location = location
            self.pathto = pathto
        def __str__(self): #works
            """Returns a string with the tiletype, location (if tiltype not Start), enemies, paths you can take from the tile, and the path to get to the tile from Start"""
            rep = ''
            if self.tiletype!='Start':
                rep += '| Location: {} '.format(self.location)
            rep += "| Type: {} | ".format(self.tiletype)
            rep += "Enemies: "
            if self.enemies:
                for enemy in self.enemies:
                    rep += (str(enemy) + ", ")
            else:
                rep += 'None '
            rep += "| Paths: "
            for path in self.paths:
                if self.paths[path]!=None:
                    rep += (path + ', ')
            rep += "| PathTo: {}".format(self.pathto)

            return rep

        @staticmethod
        def locationparser(location):
            """Turns an extended location into a compressed one"""
            directions_l = []
            for direction in location:
                antidirection = Level.Tile.antipath(direction)
                if antidirection in directions_l:
                    directions_l.remove(antidirection)
                else:
                    directions_l.append(direction)
            return "".join(sorted(directions_l))

        @staticmethod
        def antipath(path):
            """Returns the opposite of a cardinal direction"""
            for pathpair in [['n', 's'], ['e','w']]:
                if path in pathpair:
                    pathpair.remove(path)
                    return pathpair[0]
            raise ValueError('No such path exists')

        def showLoot(self):
            """Returns a string of the tile's loot"""
            rep = "Tile's loot: "
            if len(self.loot)==0:
                rep += 'None.'
                return rep
            else:
                for loot in self.loot:
                    rep += "\n" + str(loot)
            return rep



    def __init__(self, stage): #stage will start at 1
        """Intializes a level's stage, maxdepth, boss slayed state, and number of tiles. Also generates a level, initializes path to boss, locations, center tile"""
        self.stage = stage
        self.maxdepth = 3
        self.boss_slayed = False

        #generator
        self.n_tiles = 1
        if self.n_tiles<3:
            self.path_to_boss = ''
            self.locations = {'':'',}
            self.n_tiles = 1
            self.center_tile = Level.Tile(tiletype = "Start", stage = stage)
            self.r_generate()

    def __str__(self):
        """Returns the number of tiles in a level and the path to the boss."""
        return "Number of tiles: {}".format(str(self.n_tiles)) + "\nPath to boss: {}".format(self.path_to_boss) 
        

    @staticmethod
    def is_deadend(tile):
        """Checks if a tile is a dead end or not. Unused"""
        pathcounter = Level.n_paths_out(tile)
        if pathcounter == 1 and tile.direction_to_previous != None:
            return True
        else: 
            return False

    @staticmethod
    def n_paths_out(tile):
        """Checks how many paths come out of a tile"""
        pathcounter = 0
        for path in tile.paths:
            if tile.paths[path]!=None:
                pathcounter +=1
        return pathcounter

            
    def r_generate(self):
        """Generates a level based on the initialized max depth and starting tile. Also creates boss room."""
        startingTile = self.center_tile
        startingDepth = 0
        maxDepth = self.maxdepth
        def _r_generate(tile, depth):
            """Recursively generates a level."""
            from random import randint
            nonlocal maxDepth
            if depth == maxDepth:
                return
            else:
                for path in tile.paths:
                    if tile.paths[path] == None and randint(0,1) == 1:
                        location_next = Level.Tile.locationparser(tile.location + path) #staticmethod so valid
                        path_next = tile.pathto + path
                        if location_next in self.locations:
                            existing_tile = self.center_tile
                            path_to_existing = self.locations[location_next]
                            for direction in path_to_existing:
                                if existing_tile.paths[direction] != None:
                                    existing_tile = existing_tile.paths[direction]
                            if existing_tile.location == location_next:
                                tile.paths[path] = existing_tile
                                existing_tile.paths[Level.Tile.antipath(path)] = tile #staticmethod so valid
                            else:
                                print('Mismatched existing tile location {} and location next {}'.format(existing_tile.location, location_next))

                        else:
                            self.locations[location_next] = path_next
                            self.n_tiles += 1 #counting tiles
                            tile.paths[path] = Level.Tile(path, tile, location_next, path_next, stage = self.stage)
                            _r_generate(tile.paths[path], depth+1)
        
        _r_generate(startingTile, startingDepth)
        current_tile = self.center_tile
        directions = list(current_tile.paths.keys())
        while True:
            direction = directions[randint(0,3)]
            if (Level.Tile.locationparser(current_tile.location + direction) not in self.locations) and (current_tile.paths[direction]==None): #the first part should be enough but just to be safe i'll add the and none whatever
                current_tile.paths[direction] = Level.Tile(direction, current_tile, Level.Tile.locationparser(current_tile.location + direction), current_tile.pathto + direction, tiletype='Boss', stage = self.stage)
                self.path_to_boss = current_tile.pathto + direction
                break
            elif current_tile.paths[direction]!=None:
                current_tile = current_tile.paths[direction]


        
    
            
        

        
