from random import randint

def adjective_gen():
    adjectives = ''
    adj = open ('words/adjectives.txt')
    adjective1 = adj.readline().strip().split()
    if randint(0,1) == 1:
        adjectives += adjective1[randint(0, len(adjective1)-1)]
    else:
        adjectives += adjective2[randint(0, len(adjective2)-1)]
    adj.close()
    return adjectives

def weapon_gen():
    weapon_name = ''
    weapon = open('words/weapons.txt')
    weap = weapon.readline().strip('\n').split('-')
    adjectives = adjective_gen()
    if randint(0,1) == 1:
        weapon_name += adjectives
        weapon_name += weap[randint(0, len(weap)-1)]

adjective_gen()

#def armor_gen():
    

