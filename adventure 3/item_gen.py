from items import *
from random import randint

adj = open ('adjectives.txt')

def item_gen(self):
    if randint(0,1) == 1:
        self.name = randint(adjectives)
