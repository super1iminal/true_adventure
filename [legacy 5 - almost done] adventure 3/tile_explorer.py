from tiles import *

def Explore():
    level = Level(1)
    current_tile = level.center_tile
    commands = ('n', 's', 'w', 'e')
    print(level)
    while True:
        print(current_tile)
        command = input('directional command: ')
        if command in commands:
            if current_tile.paths[command]!=None:
                current_tile = current_tile.paths[command]
                continue
            else:
                print("You can't go that way!")
                continue
        else:
            break

Explore()
