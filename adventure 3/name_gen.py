def _adjective_gen():
    from random import randint
    adjectives = ''
    adj = open ('words/adjectives.txt')
    adjective1 = adj.readline().strip().split()
    if randint(0,1) == 1:
        adjectives += adjective1[randint(0, len(adjective1)-1)] + " "
    adjective2 = adj.readline().strip().split()
    if randint(0,1) == 1:
        adjectives += adjective2[randint(0, len(adjective2)-1)] + " "
    adj.close()
    return adjectives

def weapon_gen():
    from random import randint
    weapon_name = ''
    fp = open('words/weapons.txt')
    weap = fp.readline().strip().split('-')
    adjectives = _adjective_gen()
    weapon_name += adjectives
    weapon_name += weap[randint(0, len(weap)-1)]
    return weapon_name

def armor_gen(location):
    """Helmet, Torso, Arms, Legs"""
    from random import randint
    location_to_ind = {'Helmet':0, 'Torso':1, 'Arms':2, 'Legs':3}
    ind = location_to_ind[location]
    fp = open('words/armor.txt')
    armor_all = fp.readline().strip().split('|')
    armor_specific = armor_all[ind].strip().split('-')
    armor_name = ""
    armor_name += _adjective_gen()
    armor_name += armor_specific[randint(0, len(armor_specific)-1)]
    return armor_name


def consumable_gen():
    from random import randint
    fp = open('words/consumables.txt')
    consumable = fp.readline().strip('\n').split('-')
    consumable = consumable[randint(0, len(consumable)-1)]
    return consumable

#def armor_gen():
    

