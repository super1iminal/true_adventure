from random import randint

class Level(object):
    """Class that represents a level/floor"""
    class Tile(object):
        """Class that represents a tile. Generated level + 3 times per level"""
        def __init__(self, previousDirection = None, previousTile = None, location = '', tiletype = 'Enemy'):
            self.paths = {'n': None, 's': None, 'e': None, 'w': None}
            if previousTile != None and previousDirection!=None:
                self.paths[Level.Tile.antipath(previousDirection)] = previousTile



            if tiletype!='Start':
                self.enemies = [0]*randint(0,10)
            self.location = location

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

        @staticmethod
        def locationparser(location):
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
            for pathpair in [['n', 's'], ['e','w']]:
                if path in pathpair:
                    pathpair.remove(path)
                    return pathpair[0]
            raise ValueError('No such path exists')

            


    def __init__(self, stage): #stage will start at 1
        self.center_tile = Level.Tile(tiletype = "Start")
        self.stage = stage
        self.maxdepth = randint(3, int(stage) + 5)
        self.tiles = 1
        self.locations = []
        #number of iterations around center
        
    def r_generate(self, tile, location, depth):
        if depth == self.maxdepth:
            return
        else:
            for path in tile.paths:
                location_next = Level.Tile.locationparser(location + path)
                if tile.paths[path] == None:
                    if randint(0,1) == 1:
                        if location_next in self.locations:
                            existing_tile = Level.find_tile_from_plocation(location_next)
                            tile.paths[path] = existing_tile
                            existing_tile.paths[Level.Tile.antipath(path)] = tile
                        else:
                            self.locations += location_next
                            self.tiles += 1 #counting tiles
                            tile.paths[path] = Level.Tile(path, tile, location_next)
                            Level.r_generate(self, tile.paths[path], location_next, depth+1)

    def find_tile_from_plocation(self, plocation):
        """Finds a tile from the center using a parsed location"""
        current_tile = self.center_tile
        for direction in plocation:
            if current_tile.paths[direction] != None:
                current_tile = current_tile.paths[direction]
            else:
                raise ValueError("There is no tile at that location")
        return current_tile

#we know have a level generator that generates a tile map, starting with the center tile and going outwards from there. 


        
    
            
        

        
