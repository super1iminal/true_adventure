#here is where you'll get all the inputs and interpret them
#MAKE IT SO PLAYER CAN'T MOVE IF THERI BACKPACK IS OVER CAPACITY (use backpack.is_over() backpack method)

print("\nWelcome to our ADVENTURE GAME")
print("PROCEED WITH CAUTION ( ͡° ͜ʖ ͡°)")
print("\ntype HELP if ever you need help!")
while True:
    action = input("\nWhat would you like to do?") 

    if action == "help": 
        helper = '''
        move: DIRECTION (n,e,s,w)
        e.g. move n

        equip: ITEM
        e.g. equip axe
        --> on: LOCATION
            e.g. on left hand
            


        '''
        print(helper)
    
