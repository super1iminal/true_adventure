"""
Panagiotis Torabi , Asher Arya, Hien Minh Le
Friday , May 13
R. Vincent , instructor
Final Project
"""

def _adjective_gen(n_adjectives = 2):
    """Generates 0 or more adjectives"""
    from random import randint
    adjectives = ''
    adj = open ('words/adjectives.txt')
    adjective1 = adj.readline().strip().split()
    if randint(0,1) == 1:
        adjectives += adjective1[randint(0, len(adjective1)-1)] + " "
    if n_adjectives == 2:
        adjective2 = adj.readline().strip().split()
        if randint(0,1) == 1:
            adjectives += adjective2[randint(0, len(adjective2)-1)] + " "
    adj.close()
    return adjectives

def weapon_gen():
    """Generates a weapon name"""
    from random import randint
    weapon_name = ''
    fp = open('words/weapons.txt')
    weap = fp.readline().strip().split('-')
    adjectives = _adjective_gen()
    weapon_name += adjectives
    weapon_name += weap[randint(0, len(weap)-1)]
    fp.close()
    return weapon_name

def armor_gen(location):
    """Generates an armor name based on armor location"""
    """Head, Torso, Arms, Legs"""
    from random import randint
    location_to_ind = {'Head':0, 'Torso':1, 'Arms':2, 'Legs':3}
    ind = location_to_ind[location]
    fp = open('words/armor.txt')
    armor_all = fp.readline().strip().split('|')
    armor_specific = armor_all[ind].strip().split('-')
    armor_name = ""
    armor_name += _adjective_gen()
    armor_name += armor_specific[randint(0, len(armor_specific)-1)]
    fp.close()
    return armor_name


def consumable_gen():
    """Generates a consumable name"""
    from random import randint
    fp = open('words/consumables.txt')
    consumable = fp.readline().strip('\n').split('-')
    consumable = consumable[randint(0, len(consumable)-1)]
    fp.close()
    return consumable

def enemy_gen(en_type = 'Enemy'):
    """Generates an enemy name by enemy type. Default enemy type is enemy, can also be Boss"""
    from random import randint
    enemy_name = ''
    enemy_name += _adjective_gen(2)
    if en_type == 'Enemy':
        fp = open('words/enemies.txt')
        enemies = fp.readline().strip().split('-')
        enemy_name += enemies[randint(0, len(enemies)-1)]
        fp.close()
    else:
        fp = open('words/bosses.txt')
        bosses = fp.readline().strip().split('-')
        enemy_name += bosses[randint(0, len(bosses)-1)]
    return enemy_name



#def armor_gen():
    

