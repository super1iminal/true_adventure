from random import randint

class Level(object):
    """Class that represents a level/floor"""
    class Tile(object):
        """Class that represents a tile. Generated level + 3 times per level"""
        def __init__(self, direction_from_previous = None, previousTile = None, location = '', tiletype = 'Enemy'):
            self.paths = {'n': None, 's': None, 'e': None, 'w': None}
            #creating link to tile that came before
            if previousTile != None and direction_from_previous!=None:
                self.paths[Level.Tile.antipath(direction_from_previous)] = previousTile
            #generating enemies. temporary until enemies are actually coded
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



    def __str__(self):
        locations_visited = list()
        represent = str(self.center_tile)
        def r_strHelper(tile, location):
            nonlocal locations_visited
            nonlocal represent
            if Level.is_deadend(tile):
                return
            else:             
                for path in tile.paths:
                    location_next = Level.Tile.locationparser(location+path) #staticmethod so valid
                    if not location_next in locations_visited and tile.paths[path]!=None: #if we haven't already visited the tile and if there's a tile there
                        locations_visited += location_next
                        represent += str(tile.paths[path])
                        r_strHelper(tile.paths[path], location_next)
        center_tile_rep = str(self.center_tile)
        represent = r_strHelper(self.center_tile, '')
        return (center_tile_rep + represent)



    @staticmethod
    def is_deadend(tile):
        pathcounter = 0
        for path in tile.paths:
            if tile.paths[path]!=None:
                pathcounter+=1
        if pathcounter == 1:
            return True
        else: 
            return False

            
        
    def r_generate(self, tile, location, depth):
        if depth == self.maxdepth:
            return
        else:
            for path in tile.paths:
                location_next = Level.Tile.locationparser(location + path) #staticmethod so valid
                if tile.paths[path] == None:
                    if randint(0,1) == 1:
                        if location_next in self.locations:

                            existing_tile = self.center_tile
                            for direction in location_next:
                                if existing_tile.paths[direction] != None:
                                    existing_tile = existing_tile.paths[direction]
                            
                            tile.paths[path] = existing_tile
                            existing_tile.paths[Level.Tile.antipath(path)] = tile #staticmethod so valid
                        else:
                            self.locations += location_next
                            self.tiles += 1 #counting tiles
                            tile.paths[path] = Level.Tile(path, tile, location_next)
                            self.r_generate(self, tile.paths[path], location_next, depth+1)

level = Level(1)



#we know have a level generator that generates a tile map, starting with the center tile and going outwards from there. 


        
    
            
        

        
