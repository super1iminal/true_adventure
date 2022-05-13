#here is where you'll get all the inputs and interpret them


print("\nWelcome to our ADVENTURE GAME")
print("PROCEED WITH CAUTION ( ͡° ͜ʖ ͡°)")
print("\nyell HELP quick instructions!")
 
mcommands = ["move", "equip", "attack", "loot"] #main commands
while True:
    action = input("\nWhat would you like to do? ") 

    action_s = action.split()
    if not action_s[0] in mcommands:
        print("Invalid command")
        continue

    if action == "HELP": #prints instructions for player
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



    if action_s[0] == "move":
        #CHECK IF BACKPACK FULL, THEN CANT MOVE  backpack.is_over() backpack method)?


        if action == "move": 
            dir = input("In which direction do you move? ")
            if dir in ["n","e","s","w"]:
                pass#EXECUTE MOMEMENT IN GIVEN DIRECTION NEED CODE
                
            else: 
                print("Invalid direction")
                continue
        
        if action_s[1] in ["n","e","s","w"]:
            pass#EXECUTE MOVEMENT IN GIVEN DIRECTION NEED CODE
               
        else:
            print("Invalid direction")
            continue




    if action_s[0] == "loot":
        if action == "loot":
            print("x") #CODE TO LIST ALL POSSIBLE LOOTABLE THINGS
            lootc = input("What would you like to loot? ")
            #CHECK IF INPUT IS VALID THEN EXCUTE LOOT ACTION
            continue

        lootable = " ".join(action_s[1:])
        #CHECK IF LOOTABLE THING IS VALID THEN EXECUTE LOOT
        continue




    if action_s[0] == "attack":
        if action == "attack":
            print('x') #CODE TO LIST ALL POSSIBLE ATTACKIBLES
            attackc = input("What would you like to attack? ")
            #CHECK IF INPUT IS VALID THEN EXCUTE ATTACK ACTION
            continue

        attackable = " ".join(action_s[1:])
        #CHECK IF LOOTABLE THING IS VALID THEN EXECUTE ATTACK
        continue

    if action_s[0] == "equip":
        if action == "equip":
            print("x") #CODE TO LIST ALL POSSIBLE EQUIPABLE THINGS
            equipc = input("What would you like to equip? ")
            #CHECK IF INPUT IS VALID
            print("y") #LIST ALL EQUIPABLE LOCATIONS
            equipl = input("Where do you equip", equipc, "? ")
            #CHECK IF INPUT IS VALID THEN EXCUTE EQUIP ACTION




            
        




        
        
        





        


    


    

    
    

    
