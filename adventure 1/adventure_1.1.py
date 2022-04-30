import time
import random

#use if specific_item in inventory to check if player has correct item


#items setup
middle_items=["food", "pistol", "0.25$",  ]
north_items=["north_item_1"]
east_items=["east_item_1"]
west_items=["west_item_1"]
south_items=["south_item_1"]
#items
inventory = ["banana", "orange", "purple", ]
all_items = [middle_items, north_items, east_items, west_items, south_items]
local_items = all_items[player_location[0]]


#commands
all_commands=["check", "take", "drop", "look", "go", "pick",]

#words lists
check_list = ["check", "look"]
move_list=["go", "move", ]
preposition_list=["the", "at", "to"]

#locations setup
middle = [0, "middle", "m", "ground"]
north = [1, "north", "n", "desk", ]
east = [2, "east", "e", "cabinets",]
west = [3, "west", "w", "kitchen",]
south = [4, "south", "s", "exit",]

#locations
bunker_locations_list = [middle, north, east, west, south]
player_location = middle

#game
game_run=True
first_time=True

#booleans (progress for hints and stuff)
safe_unlocked=False
fishing_rod_made=False
fish_caught=False
exit_unlocked=False



#messages
wake_up="""
You wake up in the middle of a windowless room. 
Laying around you are various items.
There's food in the broken cabinets to the east, seemingly in an eternal state of tumbling
There's kitchen wares in the kitchen to the west
There a desk, reasearch-like, in front of you. There's various materials 
Behind you, to the south, lies an exit door at the end of some stairs. 


"""



def item_refresh():
    global local_items
    local_items = all_items[player_location[0]] #need to put this whenever location changes. in location change function! waaaaw
    return local_items

#basic functions
def delay(delay_seconds):
    time.sleep(delay_seconds)
    pass

def stripper(input_string):
    output_string = str(input_string).strip().lower()
    return output_string

def list_combine(list_to_combine): #WARNIGN !COMBINES LIST OF LISTS INTO SINGLE LIST. NOT USEFUL FOR COMBINGNG LISTS COMTAININg SINGLE VARTIBALES TOGERTYHER. WARNING!
    new_list=[]
    for value in list_to_combine:
        new_list.extend(value)
    return new_list

def show_list(item_list):
    for value in item_list:
        print(value)
    pass

def add_item(added_item, chosen_list):
    chosen_list.append(added_item)
    return chosen_list
    #can call by add_item(item, list). NICE

def remove_item(removed_item, chosen_list): #used to be inventory_remove
    chosen_list.remove(removed_item)
    return chosen_list

def error(): #done
    print("I don't understand.")
    pass

def first_time_function():
    global first_time
    print(wake_up)
    print("write \"check commands\" to see a list of commands")
    first_time=False
    return first_time


def command_list_function(command): #creates a list of commands the user inputted
    command_list=command.split()
    return command_list


def describe(item):
    if item in local_items:
        if item=="pistol":
            print("A semi-automatic pistol. 9x19 caliber. I have extra magazines, so no need to worry about that.")
        if item=="food":
            print("Some extra food scraps I managed to find. Might be useful, although I haven't been feeling hungry lately")
        if item=="$0.25":
            print("I literally have no use for money... although this quarter might be unconventionally useful.")
    else:
        print("I have no description for this.")
    pass



#advanced functions (uses prev. functions)
def take_and_check(taken_item, placeholder_item_list): #takes and checks the validity of an item
    if len(inventory)<=7:
        add_item(taken_item, inventory) #adds to inventory
        print(f"you add the {taken_item} to your inventory")
        remove_item(taken_item, placeholder_item_list) #removes from local_items (probably)
    elif len(inventory)>7:
        print(f"you do not have enough space for the {taken_item}")
    return inventory

def remove_and_check(removed_item, placeholder_item_list):
    if removed_item not in placeholder_item_list and removed_item in inventory:
        remove_item(removed_item, inventory) #removes from inventory
        print(f"you drop the {removed_item} from your inventory")
        add_item(removed_item, placeholder_item_list) #adds to local_items (probably)
    return inventory


#command functions. not execution!!

def location_change(location_command): #changes your location based on location_commmand input. 
    global player_location
    if location_command in player_location:
        print("You are already here!")
    elif location_command not in player_location:
        i=0
        while i<len(bunker_locations_list):
            if location_command in bunker_locations_list[i]:
                player_location=bunker_locations_list[i]
            i+=1
        print(f"your location is now {player_location[1]}")
        item_refresh()
    return player_location

def description(description_command): #gives a description of a specific item
    if description_command in inventory:
        describe(description_command)
    if description_command in local_items: #all_items[0, 1 , 2 , 3 or 4]]
        print("I need to have this item to describe it.")
    pass

def location_print():
    print(f"{player_location[3]}")
    pass

def help():
    print("write one of these words:")
    show_list(all_commands)
    print("combined with a second, specific word")
    print(f"hint: write \"check {player_location[3]}\"")
    pass

#1 word commands execution

def one_word_commands(command_list):
    first_command=command_list[0]
    if first_command in list_combine(bunker_locations_list):
        location_change(first_command)
    if first_command in local_items or inventory:
        description(first_command)
    if first_command == "help":
        help()
    return

#2 word commands execution

def two_word_commands(command_list):
    first_command=command_list[0]
    second_command=command_list[1]
    if first_command in check_list: # if check _____ or look _____
        if second_command == "location":
            location_print()
        if second_command == "inventory":
            show_list(inventory)
        if second_command in local_items or inventory:
            description(second_command) #already has if statement in it
        if second_command == "commands":
            help()
        if second_command in player_location:
            if len(local_items)>0:
                show_list(local_items)
            if len(local_items)==0:
                print("There are no items here.") #should turn this into function.
    if first_command in move_list: #if go ______ or move _____
        if second_command in middle or north or east or west or south:
            location_change(second_command)
    if first_command == "take":
        if second_command in local_items:
            take_and_check(second_command, local_items)
    if first_command == "drop":
        if second_command in inventory:
            remove_and_check(second_command, local_items)
    if first_command == "describe":
        if first_command in local_items or inventory:
            description(second_command)
    return

#3 word commands execution

def three_word_commands(command_list):
    first_command=command_list[0]
    second_command=command_list[1]
    third_command=command_list[2]
    if first_command == "pick" and second_command == "up":
        if third_command in local_items:
            take_and_check(third_command, local_items)
    if first_command in check_list and second_command in preposition_list:
        if third_command == "location":
            location_print()
        if third_command == "inventory":
            show_list(inventory)
        if third_command in local_items or inventory:
            description(third_command) #already has if statement in it
        if third_command == "commands":
            help()
        if third_command in player_location:
            if len(local_items)>0:
                show_list(local_items)
            if len(local_items)==0:
                print("There are no items here.") # should turn this into function
    if first_command in move_list and second_command in preposition_list:
        if third_command in middle or north or east or west or south:
            location_change(third_command)
    return



#GAME SCRIPT


while game_run==True:
    if first_time==True:
        first_time_function()
    command_list = command_list_function(stripper(str(input())))
    # print(command_list) # for bug testing
    if len(command_list)==0:
        error()
    if len(command_list)==1:
        one_word_commands(command_list)
    if len(command_list)==2:
        two_word_commands(command_list)
    if len(command_list)==3:
        three_word_commands(command_list)

    


