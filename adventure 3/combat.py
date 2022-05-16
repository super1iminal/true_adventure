"""
Panagiotis Torabi , Asher Arya, Hien Minh Le
Friday , May 13
R. Vincent , instructor
Final Project
"""

from player import *
from enemies import *

"""
Combat is turn-based and simple. You can do one action per turn. Be it consume some food or attack
We could potentially add an attempt to flee later on


"""


ccommands = ('attack', 'consume', 'help')


helpmsg_c = '''
list of combat commands: {}

type a main command to get all possible actions'''



def Combat(gamer, enemy):
    """Returns True if combat is won and False if combat is lost"""
    print("You're in combat. Enter help for a list of commands.\n {}: DMG: {} | MHEALTH: {} | CHEALTH: {} | RES: {}\n {} {}: DMG: {} | HEALTH: {} | RES: {}".format(gamer.showName(), gamer.showDamage(), gamer.showMHealth(), gamer.showCHealth, gamer.showResistance(), enemy.showName(), enemy.showDamage(), enemy.showHealth(), enemy.showResistance()))
    while True:
        command_s = input('What would you like to do? ').strip().lower().split()

        if command_s[0] == "help": #prints instructions for player
            print(helpmsg_c)
            continue


        if command_s[0] == 'attack':
            player_damage = gamer.damage_dealt()
            enemy_dead = enemy.damage_taken(player_damage)
            if enemy_dead:
                print('You deal {} damage. You kill the {}!'.format(player_damage, enemy.showName()))
                return True
            else:
                print("You deal {} damage. The {} is currently at {} health".format(player_damage, enemy.showName(), enemy.showHealth()))

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

        enemy_damage = enemy.damage_dealt()
        player_dead = gamer.damage_taken(enemy_damage)
        if player_dead:
            print('The {} dealt {} damage to you. You are dead!'.format(enemy.showName(), enemy_damage))
            return False
        else:
            print('The {} deals {} damage to you.'.format(enemy.showName(), enemy_damage))

        



