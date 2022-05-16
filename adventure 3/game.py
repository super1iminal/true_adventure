"""
Panagiotis Torabi , Asher Arya, Hien Minh Le
Friday , May 13
R. Vincent , instructor
Final Project
"""
from items import *
from player import *
from inventory import *
from tiles import *
from enemies import *
from combat import *

"""


"""
#here is where you'll get all the inputs and interpret them

print("\nWelcome to our ADVENTURE GAME")
print("PROCEED WITH CAUTION ( ͡° ͜ʖ ͡°)")
print("\nyell HELP quick instructions!")

gamer = Player()

mcommands = ("move", "equip", "attack", "consume", "help", 'continue', "inspect", "take", "drop", 'location') #main commands
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

ccommands = ('attack', 'consume', 'help') #combat commands


helpmsg_c = '''
You're in combat. Doing any action (except help) will end your turn.

list of combat commands: {}
Type a combat command to get all possible actions. 
'''.format(ccommands)


boss_slayed_msg = """
Congratulations, adventuer! You've slayed the boss!


"""

level = Level(1)
current_tile = level.center_tile
print(str(current_tile))


while True:
    if gamer.is_dead():
        tryagain = input(f'Game Over! You killed {gamer.enemies_killed} enemies. Try again? y/n\n').strip().lower()
        if tryagain == "y":
            gamer = Player()
            level = Level(1)
            current_tile = level.center_tile
            continue
        else:
            print('Thanks for playing!')
            break

    action = input("\nWhat would you like to do? ").strip().lower()
    action_s = action.split()

    if action_s[0] not in mcommands:
        print("Invalid command")
        continue

    if action_s[0] == "help": #prints instructions for player
        print(helpmsg)
        continue
    
    if action_s[0] == 'location': #prints current location
        print(str(current_tile))

    if action_s[0] == 'continue': #to advance to next level
        if level.boss_slayed:
            print('Good luck on the next level!')
            current_stage = level.stage
            level = Level(current_stage+1)
            current_tile = level.center_tile
            continue
        else:
            print("You haven't beat the boss yet!")
            continue

    if action_s[0] == "move": #to move between tiles
        if gamer.inventory.backpack.is_over():
            print("You are too heavy to move, empty some of your inventory")
            continue
        
        if len(current_tile.enemies) > 0:
            print('There are enemies. You must kill them to move on.')
            continue

        if len(action_s) == 1: 
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
                    print(str(current_tile))
                    continue
                else:
                    print("You can't go that way!")
                    continue

        
        elif action_s[1] in directions:
            if current_tile.paths[action_s[1]]!=None:
                if current_tile.paths[action_s[1]].tiletype == 'Boss':
                    yn = input('Warning! That tile is the boss! Do you still want to continue? y/n\n')
                    if yn!='y':
                        print('Fair choice.')
                        continue
                    else:
                        print('Good luck.')
                current_tile = current_tile.paths[action_s[1]]
                print(str(current_tile))
                continue
            else:
                print("You can't go that way!")
                continue
        else:
            print("Invalid direction")
            continue

    if action_s[0] == "take": #to pick up loot from floor
        if len(action_s) == 1:
            print(current_tile.showLoot())
            taken = input("What would you like to pick up? ").lower()
        else:
            taken = " ".join(action_s[1:])
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


    if action_s[0] == "drop": #to drop item from inventory onto floor
        if len(action_s) == 1:
            print("Inventory:")
            print(gamer.inventory.showBackpack())
            drop = input("Choose item to drop or none: ").lower()
        else:
            drop = " ".join(action_s[1:])
        checker = 0
        for item in gamer.inventory.backpack.binventory:
            if drop == str(item.name).lower():
                gamer.inventory.drop(item.name, current_tile)
                print('Dropping {}'.format(item.name))
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
                if enemy.loot:
                    print('The enemy dropped some loot.')
                gamer.enemies_killed += 1
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
                enemy_damage_taken = enemy.damage_taken(player_damage)
                print('You deal {} damage.'.format(enemy_damage_taken))
                if enemy.is_dead():
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
                    print('{} Consumed!'.format(eat))
                else:
                    print("Could not find that item")
                    continue

            elif command_s[0] == 'wait':
                print('Okay...')

            else:
                print('Invalid command')
                continue

            enemy_damage = enemy.damage_dealt()
            player_damage_taken = gamer.damage_taken(enemy_damage)
            print('The {} deals {} damage to you.'.format(enemy.showName(), player_damage_taken))
            if gamer.is_dead():
                continue
        continue

    if action_s[0] == "equip": #to equip armor or weapon
        if len(action_s) == 1:
            print("In Backpack: ")
            print(gamer.inventory.showBackpack())
            equipc = input("What would you like to equip?: ").lower()
        else:
            equipc = " ".join(action_s[1:])
        checker = 0
        for item in gamer.inventory.backpack.binventory:
            if equipc == str(item.name).lower():
                if item.itemtype == 'Armor' or item.itemtype == 'Weapons':
                    checker += 1
                    gamer.inventory.equip(item.name)
                    continue
                    
                else:
                    print("Could not equip that item")
                    checker += 1
                    continue
                
        if checker == 0:
            print('Could not find that item')


    
    if action == "consume": #to eat food and heal
        print("Consumables in Backpack: ")
        consumable_list = []
        for item in gamer.inventory.backpack.binventory:
            if item.itemtype == 'Consumable':
                consumable_list.append(item.name)
                print(item)
        if len(consumable_list) == 0:
            print('You do not have any consumables.')
            continue
        eat = input("What would you like the consume? ").title()
        if eat in consumable_list:
            gamer.consume_item(eat)
            print(f'{eat} consumed!')
            continue
        else:
            print("Could not find that item")
            continue

    if action_s[0] == "inspect":
        if len(action_s) > 1:
            inspected = " ".join(action_s[1:])
        else:
            inspected = input("Inventory, Enemy, Floor or Self? ").lower()
        if inspected == "inventory":
            print(gamer.showLoot())
            continue
        elif inspected == "enemy":
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
        elif inspected == "floor":
            print(current_tile.showLoot())
            continue
        
        elif inspected == 'self':
            print(str(gamer))
            continue









        

           





            
        




        
        
        





        


    


    

    
    

    
