from items import *
from player import *
from inventory import *
from tiles import *
from enemies import *
from combat import *

"""


read me



this is good :)

you should also add a look command. im eventually gonna change inventory repr to just print item names, so you'd need to look at an item to see its stats
also able to look at enemies to see their stats so u can see if u can beat them before u attack
also if there are enemies we can either be locked into fighting them or we can make it so that we're able to go back to the tile that we came from. your choice.
to find the tile we came from, just keep track of previous_tile as well as current_tile. if the current_tile.paths[direction] == previous_tile, let the player do it

i made enemies fully working btw. 
 
**************FROM PANA******************
-i think we should keep things as simple as possible for now until we get a working, submitable game
i dont want to stress over this too much tmrw since i got a final exam on monday
-i think the look command should be called "inspect"
<3 u asher, also <3 u hien
*****************************************












"""
#here is where you'll get all the inputs and interpret them

print("\nWelcome to our ADVENTURE GAME")
print("PROCEED WITH CAUTION ( ͡° ͜ʖ ͡°)")
print("\nyell HELP quick instructions!")

gamer = Player()


mcommands = ("move", "equip", "attack", "loot", "consume", "HELP") #main commands
directions = ('n', 's', 'w', 'e')

helpmsg = '''
list of main commands: {}

type a main command to get all possible actions

or excute command right away

            |
            |
            V

move + (n,e,s,w)
e.g. move n'''



level = Level(1)
current_tile = level.center_tile

while True:
    print("You're here: ", str(current_tile))

    action = input("\nWhat would you like to do? ").strip().lower()
    action_s = action.split()

    if action_s[0] not in mcommands:
        print("Invalid command")
        continue

    if action_s[0] == "help": #prints instructions for player
        print(helpmsg)
        continue



    if action_s[0] == "move":
        if gamer.inventory.backpack.is_over():
            print("You are too heavy to move, empty some of your inventory")
            continue

        if len(action_s[0]) == 1: 
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
        if len(action_s[0]) == 1:
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



    if action == "equip":
        print("In Backpack: ")
        for item in gamer.inventory.backpack.binventory:
            print(item)
        equipc = input("What would you like to equip? ")
        for item in gamer.inventory.backpack.binventory:
            if equipc == item.name:
            
                if (type(equipc) is Armor) or (type(equipc) is Weapon):
                    gamer.inventory.equip(equipc)
                    continue
                    
                else:
                    print("Could not equip that item")
                    continue
                
            else:
                print("Could not find that item")
                continue


    
    if action == "consume":
        print("Consumables in Backpack: ")
        consumable_list = []
        for item in gamer.inventory.backpack.binventory:
            if item.itemtype == 'Consumable':
                consumable_list.append(item.name)
                print(item)
        eat = input("What would you like the consume? ")
        if eat in consumable_list:
            gamer.consume_item(eat)
            continue
        else:
            print("Could not find that item")
            continue





        

           





            
        




        
        
        





        


    


    

    
    

    
