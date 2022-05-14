from items import *
from player import *
from inventory import *
from tiles import *


#here is where you'll get all the inputs and interpret them

print("\nWelcome to our ADVENTURE GAME")
print("PROCEED WITH CAUTION ( ͡° ͜ʖ ͡°)")
print("\nyell HELP quick instructions!")

gamer = Player()


mcommands = ["move", "equip", "attack", "loot", "HELP"] #main commands
directions = ('n', 's', 'w', 'e')

level = Level(1)
current_tile = level.center_tile

while True:
    
    print(current_tile)
    for path in current_tile.paths:
        if current_tile.paths[path]!=None:
            print(path, current_tile.paths[path])
            

    action = input("\nWhat would you like to do? ") 

    action_s = action.split()
    if not action_s[0] in mcommands:
        print("Invalid command")
        continue

    if action == "HELP": #prints instructions for player
        helper = '''

        list of commands: [move, equip, attack, loot]
        
        just type a command to get all possible actions
        
        or excute command right away
        |
        |
        V

        move: DIRECTION (n,e,s,w)
        e.g. move n

        equip: ITEM
        e.g. equip axe
        --> on: LOCATION
            e.g. on left hand
        
        attack: ENEMY
        e.g. attack blue goblin

        loot: LOCATION
        e.g. loot floor
        '''
        print(helper)
        continue



    if action_s[0] == "move":
        if gamer.inventory.backpack.is_over():
            print("You are too heavy to move, empty some of your inventory")
            continue
        

    
        if action == "move": 

            dir = input("In which direction do you move? ")
            if dir in directions:
                if current_tile.paths[dir]!=None:
                    current_tile = current_tile.paths[dir]
                    continue
                else:
                    print("You can't go that way!")
                    continue

        
        if action_s[1] in directions:
            if current_tile.paths[action_s[1]]!=None:
                    current_tile = current_tile.paths[action_s[1]]
                    continue
            else:
                print("You can't go that way!")
                continue
           
               
        else:
            print("Invalid direction")
            continue








    if action_s[0] == "loot":
        if action == "loot":
            print("x") #CODE TO LIST ALL POSSIBLE LOOTABLE THINGS
            lootc = input("What would you like to loot? ")
            #CHECK IF INPUT IS VALID THEN EXCUTE LOOT ACTION
            continue

        lootable = " ".join(action_s[1:])
        #CHECK IF LOOTABLE THING IS VALID THEN EXECUTE LOOT
        continue




    if action_s[0] == "attack":
        if action == "attack":
            print('x') #CODE TO LIST ALL POSSIBLE ATTACKIBLES
            attackc = input("What would you like to attack? ")
            #CHECK IF INPUT IS VALID THEN EXCUTE ATTACK ACTION
            continue

        attackable = " ".join(action_s[1:])
        #CHECK IF LOOTABLE THING IS VALID THEN EXECUTE ATTACK
        continue

    if action_s[0] == "equip":
        if action == "equip":
            print("In Backpack: ")
            for item in gamer.inventory.backpack.binventory:
                print(item)
            equipc = input("What would you like to equip? ")
            for item in gamer.inventory.backpack.binventory:
                if equipc == item.name:
            
                    if type(equipc) is Armor:
                        gamer.inventory.equip(equipc)
                        continue
                    
                    if type(equipc) is Weapon:
                        gamer.inventory.equip(equipc)
                        continue
                    else:
                        print("Could not equip that item")
                        continue
                    

                else:
                    print("Could not find that item")
                    continue

           





            
        




        
        
        





        


    


    

    
    

    
