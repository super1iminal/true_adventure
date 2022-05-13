#here is where you'll get all the inputs and interpret them
#MAKE IT SO PLAYER CAN'T MOVE IF THERI BACKPACK IS OVER CAPACITY (use backpack.is_over() backpack method)

print("\nWelcome to our ADVENTURE GAME")
print("PROCEED WITH CAUTION ( ͡° ͜ʖ ͡°)")
print("\nyell HELP quick instructions!")

commands = ["move", "equip", "attack", "loot", "on", "HELP"]
while True:
    action = input("\nWhat would you like to do? ") 

    if not action_s[0] in commands:
        print("Invalid command")

    if action == "HELP": 
        helper = '''

        list of commands: [move, equip, attack, loot]
        
        just type a command to get all possible actions
        
        or excute command right away
        |
        |
        V

        move: DIRECTION (n,e,s,w)
        e.g. move n

        equip: ITEM
        e.g. equip axe
        --> on: LOCATION
            e.g. on left hand
        
        attack: ENEMY
        e.g. attack blue goblin

        loot: LOCATION
        e.g. loot floor
        '''
        print(helper)
        continue


    action_s = action.split()

    
    

    
