from random import randint


class Level(object):
    """Class that represents a level/floor"""
    class Tile(object):
        """Class that represents a tile. Generated level + 3 times per level"""
        def __init__(self, direction_from_previous = None, previousTile = None, location = '', pathto = '', tiletype = 'Enemy'):
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
            if tiletype!='Start':
                self.enemies = [0]*randint(0,10)
            else:
                self.enemies = list()
            
            #LOCATIONS
            self.location = location
            self.pathto = pathto
        def __str__(self): #works
            if self.tiletype == 'Start':
                rep = "| Location: Start "
            else:
                rep = "| Location: {} | ".format(self.location)
                rep += "Enemies: "
                for enemy in self.enemies:
                    rep += (str(enemy) + ", ")
            rep += "| Paths: "
            for path in self.paths:
                if self.paths[path]!=None:
                    rep += (path + ', ')
            rep += "| PathTo: {}".format(self.pathto)

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
        self.maxdepth = 3
        self.n_tiles = 1
        self.locations = {'':'',}
        self.r_generate()
        #number of iterations around center

    def __str__(self):
        #basically, I need this to go through every tile recursively
        # this is like a virus, if a tile has already been 'infected' (visited), then skip it. the problem is, i need a central data storage,
        # here it's visited locations, to store the data of where the virus has been
        return str(self.n_tiles)
        """      
        def all_visited(tile, v_locations):
            v_counter = 0
            for path in tile.paths:
                if Level.Tile.locationparser(path + tile.location) in v_locations or tile.paths[path]==None:
                    v_counter += 1
            if v_counter == 4:
                return True
            else: return False
        repre = ''
        visited_locations = ['',]
        def strHelper(tile):
            nonlocal visited_locations
            nonlocal repre
            repre += (str(tile) + "\n" )
            for path in tile.paths:
                if tile.paths[path]!=None and (Level.Tile.locationparser(tile.location + path) not in visited_locations):
                    visited_locations += [Level.Tile.locationparser(tile.location + path)] #adding location of tile currently about to expand into to repetoire
                    strHelper(tile.paths[path])
        strHelper(self.center_tile)
        return repre"""
        

    @staticmethod
    def tilecounter(tile):
        pass

    @staticmethod
    def is_deadend(tile):
        """Checks if a tile is a dead end or not"""
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
        startingTile = self.center_tile
        startingDepth = 0
        maxDepth = self.maxdepth
        def _r_generate(tile, depth):
            from random import randint
            nonlocal maxDepth
            if depth == maxDepth:
                print('Max Depth Reached. Returning')
                return
            else:
                print("Generating...")
                for path in tile.paths:
                    if tile.paths[path] == None and randint(0,1) == 1:
                        location_next = Level.Tile.locationparser(tile.location + path) #staticmethod so valid
                        path_next = tile.pathto + path
                        if location_next in self.locations:
                            existing_tile = self.center_tile
                            path_to_existing = self.locations[location_next]
                            print('Tile exists at {}, trying to get there through {}'.format(location_next, path_to_existing))
                            for direction in path_to_existing:
                                if existing_tile.paths[direction] != None:
                                    existing_tile = existing_tile.paths[direction]
                            if existing_tile.location == location_next:
                                print('Correctly matched existing tile location {} and location next {}'.format(existing_tile.location, location_next))
                                tile.paths[path] = existing_tile
                                existing_tile.paths[Level.Tile.antipath(path)] = tile #staticmethod so valid
                            else:
                                print('Mismatched existing tile location {} and location next {}'.format(existing_tile.location, location_next))

                        else:
                            self.locations[location_next] = path_next
                            self.n_tiles += 1 #counting tiles
                            tile.paths[path] = Level.Tile(path, tile, location_next, path_next)
                            _r_generate(tile.paths[path], depth+1)
        _r_generate(startingTile, startingDepth)


    @staticmethod
    def tile_from_direction(tile, direction):
        return tile.paths[direction]




#we know have a level generator that generates a tile map, starting with the center tile and going outwards from there. 


        
    
            
        

        
