from player import *
from enemies import *

"""
Combat is turn-based and simple. You can do one action per turn. Be it consume some food or attack
We could potentially add an attempt to flee later on


"""


def Combat(gamer, enemy):
    print("You're in combat.\n {}: DMG: {} | MHEALTH: {} | CHEALTH: {} | RES: {}\n {} {}: DMG: {} | HEALTH: {} | RES: {}".format(gamer.showName(), gamer.showDamage(), gamer.showMHealth(), gamer.showCHealth, gamer.showResistance(), enemy.showName(), enemy.showDamage(), enemy.showHealth(), enemy.showResistance()))
    command = input('What would you like to do?')

