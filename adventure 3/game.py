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

ok I made combat fully working. enemies drop items into current_tile.loot now. no looting yet, but here's what i'm thinking: instead of 'loot' we just have an action called look.

look has 3 main components:
look inventory: checks your inventory and equipment player.showLoot()
look enemy: looks at an enemy's loot. enemy.showLoot()
look ground: looks at ground an enables looting. current_tile.showLoot()

****i made all the show loot stuff already so just implement it in the game


YOU ALSO need to make it so that the player is able to pick up items and put them in the backpack from the ground.
    make a new command called take
    make it seperate from the look command or implement it if the player looks at the ground idc
    make the take command remove an item from the current_tile by name - look at my other code for adding and removing code by name to figure this out if u dont know how
            for this you don't need to make a method in any other files, you can do it from this file only
    and then put that item in the backpack by doing inventory.backpack.add_item(item) or whatever

i also made it so if u beat the boss u can write continue to go to next level

i also made it so that u level up

i also made it so that u have to kill all enemies in a tile before u can continue

THEN WE'RE DONE BABY

**************************
insect command is down, now doing take












"""
#here is where you'll get all the inputs and interpret them

print("\nWelcome to our ADVENTURE GAME")
print("PROCEED WITH CAUTION ( ͡° ͜ʖ ͡°)")
print("\nyell HELP quick instructions!")

gamer = Player()

mcommands = ("move", "equip", "attack", "consume", "help", 'continue', "inspect", "take", "drop") #main commands
directions = ('n', 's', 'w', 'e')

helpmsg = '''
List of commands: {}

Type a main command to get all possible actions

or excute command right away

            |
            |
            V

move + (n,e,s,w)
e.g. move n
e.g. inspect floor
'''.format(mcommands)

ccommands = ('attack', 'consume', 'help')


helpmsg_c = '''
You're in combat. Doing any action (except help) will end your turn.

list of combat commands: {}
Type a combat command to get all possible actions. 
'''

boss_slayed_msg = """
Congratulations, adventuer! You've slayed the boss!


"""

level = Level(1)
current_tile = level.center_tile

while True:
    if gamer.is_dead():
        tryagain = input('Game Over! Try again? y/n\n').strip().lower()
        if tryagain == "y":
            gamer = Player()
            level = Level(1)
            current_tile = level.center_tile
            continue
        else:
            print('Thanks for playing!')
            break

    print(str(current_tile))

    action = input("\nWhat would you like to do? ").strip().lower()
    action_s = action.split()

    if action_s[0] not in mcommands:
        print("Invalid command")
        continue

    if action_s[0] == "help": #prints instructions for player
        print(helpmsg)
        continue

    if action_s[0] == 'continue':
        if level.boss_slayed:
            print('Good luck on the next level!')
            current_stage = level.stage
            level = Level(current_stage+1)
            current_tile = level.center_tile
            continue
        else:
            print("You haven't beat the boss yet!")
            continue

    if action_s[0] == "move":
        if gamer.inventory.backpack.is_over():
            print("You are too heavy to move, empty some of your inventory")
            continue
        
        if len(current_tile.enemies) > 0:
            print('There are enemies. You must kill them to move on.')
            continue

        if len(action_s[0]) == 1: 
            dir = input("In which direction do you move? ")
            if dir in directions:
                if current_tile.paths[dir]!=None:
                    if current_tile.paths[dir].tiletype == 'Boss':
                        yn = input('Warning! That tile is the boss! Do you still want to continue? y/n\n')
                        if yn!='y':
                            print('Fair choice.')
                            continue
                        else:
                            print('Good luck.')
                    current_tile = current_tile.paths[dir]
                    continue
                else:
                    print("You can't go that way!")
                    continue

        
        if action_s[1] in directions:
            if current_tile.paths[action_s[1]]!=None:
                if current_tile.paths[action_s[1]].tiletype == 'Boss':
                    yn = input('Warning! That tile is the boss! Do you still want to continue? y/n\n')
                    if yn!='y':
                        print('Fair choice.')
                        continue
                    else:
                        print('Good luck.')
                current_tile = current_tile.paths[action_s[1]]
                continue
            else:
                print("You can't go that way!")
                continue
        else:
            print("Invalid direction")
            continue




    if action_s[0] == "take":
        print(current_tile.showLoot())
        taken = input("What would you like to pick up? ").lower()
            
            
        checker = 0
        for item in current_tile.loot:
            if taken == item.name.lower():
                gamer.inventory.backpack.add_item(item)
                current_tile.loot.remove(item)
                print("Picked up!")
                checker += 1
        if checker == 1:
            continue

        else:
            print("Could not find that item")
            continue


    if action_s[0] == "drop":
        print("Inventory:")
        for item in gamer.inventory.backpack.binventory:
                print(item)
        drop = input("Choose item to drop or none: ").lower()

        if drop == "none":
            continue
        
        checker = 0
        for item in gamer.inventory.backpack.binventory:
            if drop == item.name.lower():
                current_tile.loot.append(item)
                gamer.inventory.backpack.remove_item(item)
                checker +=1
                break
        if checker == 1:
            continue
        else:
            print("Could not find that item")
            continue



    if action_s[0] == "attack":
        enemies_d = {}
        enemies_l = []
        for enemy_instance in current_tile.enemies:
            enemies_d[(enemy_instance.showName()).lower()] = enemy_instance
            enemies_l.append(enemy_instance.showName())
        if len(action_s)==1:
            en_choice = input('What enemy would you like to fight?: ' + str(list(enemies_l)) + "\n").strip().lower()
        else:
            en_choice = " ".join(action_s[1:])
        if en_choice not in list(enemies_d.keys()):
            print("Tha enemy is not one you can fight right now. ({})".format(en_choice))
            continue
        
        #enemy being assigned:
        enemy = enemies_d[en_choice]

        #combat start:
        while True:
            if gamer.is_dead():
                print('You died.')
                break
            if enemy.is_dead():
                if enemy.en_type == 'Boss':
                    level.boss_slayed = True
                    print('You killed the level boss!')
                else:
                    print("You killed the enemy!")
                gamer.xpIncrease(enemy.xp)
                current_tile.loot += enemy.loot
                current_tile.enemies.remove(enemy)
                break


            print("You: ", str(gamer))
            print("Enemy: ", str(enemy))
            command_s = input('What would you like to do? ').strip().lower().split()
            if command_s[0] == "help": #prints instructions for player
                print(helpmsg_c)
                continue


            if command_s[0] == 'attack':
                player_damage = gamer.damage_dealt()
                enemy_dead = enemy.damage_taken(player_damage)
                print('You deal {} damage.'.format(player_damage))
                if enemy_dead:
                    continue

            elif command_s[0] == 'consume':
                print("Consumables in Backpack: ")
                consumable_list = []
                for item in gamer.inventory.backpack.binventory:
                    if item.itemtype == 'Consumable':
                        consumable_list.append(item.name)
                        print(item)
                eat = input("What would you like the consume? ")
                if eat in consumable_list:
                    gamer.consume_item(eat)
                else:
                    print("Could not find that item")
                    continue

            elif command_s[0] == 'wait':
                print('Okay...')

            else:
                print('Invalid command')
                continue

            enemy_damage = enemy.damage_dealt()
            player_dead = gamer.damage_taken(enemy_damage)
            print('The {} deals {} damage to you.'.format(enemy.showName(), enemy_damage))
            if player_dead:
                continue
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
        eat = input("What would you like the consume? ").title()
        if eat in consumable_list:
            gamer.consume_item(eat)
            continue
        else:
            print("Could not find that item")
            continue

    if action_s[0] == "inspect":
        if len(action_s) > 1:
            if action_s[1] == "floor":
                print(current_tile.showLoot())
                continue

            if action_s[1] == "inventory":
                print(gamer.showLoot())
                continue

            checker = 0
            for e in current_tile.enemies:
                if " ".join(action_s[1:]) == e.name.lower():
                    print(e.showLoot())
                    checker += 1
                    break
            if checker == 1:
                continue
                
            else:
                print("Could not inspect")
                continue
        


        inspected = input("Inventory, Enemy, or  Floor? ").lower()
        if inspected == "inventory":
            print(gamer.showLoot())
            continue
        if inspected == "enemy":
            print("Enemies in tile: ")
            for e in current_tile.enemies:
                print(e.name)
            enem = input("Inspect which enemy? ")
            checker = 0
            for e in current_tile.enemies:
                if enem == e.name:
                    print(e.showLoot())
                    checker += 1
                    break
            if checker == 1:
                continue
            else:
                print("Could not find that enemy")
                continue
        if inspected == "floor":
            print(current_tile.showLoot())
            continue








        

           





            
        




        
        
        





        


    


    

    
    

    
