import time
import random

#use if specific_item in inventory to check if player has correct item
#use list.count() to recieve 0 or 1 or 2 for item checker



#items setup
middle_items=["food", "pistol", "0.25$",  ]
north_items=["papers", "string",]
east_items=["cane", "food", "food", "food"]
west_items=["knife", "pan", "fork"]
south_items=["map"]
safe_items = ["note"]
grill_items = ["fish"]
all_items = [middle_items, north_items, east_items, west_items, south_items]
hidden_items = [safe_items, grill_items]

#commands
all_commands=["check", "take", "drop", "look", "go", "pick",]

#words lists
check_list = ["check", "look"]
move_list=["goto", "moveto",]
preposition_list=["the", "at", "to"]

#locations setup
middle = [0, "middle", "m", "ground"]
north = [1, "north", "n", "desk", ]
east = [2, "east", "e", "cabinets",]
west = [3, "west", "w", "kitchen",]
south = [4, "south", "s", "exit",]
all_bunker_locations = [middle, north, east, west, south]


#game setup
player_location = middle
local_items = all_items[player_location[0]]
game_run=True
first_time=True
inventory = ["banana", "orange", "purple", ]

#item locations
bunker_item_locations = []
for wario in all_bunker_locations:
    bunker_item_locations.append(wario[3])


#booleans (progress for hints and stuff)
safe_unlocked=False
fishing_rod_made=False
fish_caught=False
exit_unlocked=False



#messages
wake_up_msg="""You wake up in the middle of a windowless room. 
Laying around you are various items. There's a grill underneath you, and you can hear running water.
There's food in the broken cabinets to the east, seemingly in an eternal state of tumbling
There's kitchen wares in the kitchen to the west
There's a desk, reasearch-like, in front of you. There's various materials hanging out of the desk drawers.
Behind you, to the south, lies an exit door at the top of some stairs."""

location_msg="""You're in some sort of bunker. 
In the middle, there's a grill with some sort of underground river running under it.
In the north, there's a desk with various materials
In the east, there's some cabinets with food.
In the west, there's a kitchen with kitchen wares
In the south, there's a door."""

desk_msg="""It looks like there's a safe underneath the desk"""
exit_msg="""Locked with a keypad. The combination can only be letters"""
cabinet_msg="""Just some old cabinets. There might be some useful stuff here, though"""
kitchen_msg="""It looks like this kitchen's been ransacked."""


#
#START OF BASIC FUNCTIONS 
#**functions that don't use other functions
#

#miscellaneous functions

def delay(delay_seconds):
    time.sleep(delay_seconds)
    pass

def stripper(input_string):
    output_string = str(input_string).strip().lower()
    return output_string

def list_list_combine(list_to_combine): #WARNIGN !COMBINES LIST OF LISTS INTO SINGLE LIST. NOT USEFUL FOR COMBINGNG LISTS COMTAININg SINGLE VARTIBALES TOGERTYHER. WARNING!
    new_list=[]
    for value in list_to_combine:
        new_list.extend(value)
    return new_list

def list_combine(list_1_to_combine, list_2_to_combine):
    new_list=[]
    new_list.extend(list_1_to_combine)
    new_list.extend(list_2_to_combine)
    return new_list

def show_list(item_list):
    for value in item_list:
        print(value)
    pass

def error(): #done
    print("I don't understand.")
    pass

#item-related functions

def item_refresh():
    global local_items
    local_items = all_items[player_location[0]] #need to put this whenever location changes. in location change function! waaaaw
    return local_items

def add_item(added_item, chosen_list):
    chosen_list.append(added_item)
    return chosen_list
    #can call by add_item(item, list). NICE

def remove_item(removed_item, chosen_list): #used to be inventory_remove
    chosen_list.remove(removed_item)
    return chosen_list

#text-related functions

def first_time_function():
    global first_time
    print(wake_up_msg)
    print("type 'help' to see a list of commands")
    first_time=False
    return first_time

def location_print():
    print(f"you are in the {player_location[1]} part of the bunker, near the {player_location[3]}")
    pass


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

#END OF BASIC FUNCTIONS




#START OF ADVANCED FUCNTIONS 
#**functions that use basic functions


def command_list_function(command): #creates a list of commands the user inputted
    command_list=stripper(command).split()
    return command_list


#item-related functions
def take_and_check(taken_item, placeholder_item_list): #takes and checks the validity of an item
    if len(inventory)<=7:
        add_item(taken_item, inventory) #adds to inventory
        print(f"you add the {taken_item} to your inventory")
        remove_item(taken_item, placeholder_item_list) #removes from local_items (probably)
    elif len(inventory)>7:
        print(f"you do not have enough space for the {taken_item}")
    return inventory

def pre_take_and_check(chosen_item, placeholder_item_list):
    if chosen_item in local_items:
        take_and_check(chosen_item, placeholder_item_list)
    if chosen_item in inventory:
        print("you already have this item")
    if chosen_item not in local_items:
        print("you can't get to this item")
    if chosen_item not in list_list_combine(all_items):
        error()
    pass

def remove_and_check(removed_item, placeholder_item_list):
    if removed_item not in placeholder_item_list and removed_item in inventory:
        remove_item(removed_item, inventory) #removes from inventory
        print(f"you drop the {removed_item} from your inventory")
        add_item(removed_item, placeholder_item_list) #adds to local_items (probably)
    return inventory


#location change function and its correspoing check statement
def location_change(location_command): #changes your location based on location_commmand input. 
    global player_location
    if location_command in player_location: #the end is for the function that tells you what items are close to u
        print("You are already here!")
    elif location_command not in player_location:
        i=0
        while i<len(all_bunker_locations):
            if location_command in all_bunker_locations[i]:
                player_location=all_bunker_locations[i]
            i+=1
        print(f"your location is now {player_location[1]}")
        item_refresh()
    return player_location

def pre_location_change(location_command):
    if location_command in list_list_combine(all_bunker_locations):
        location_change(location_command)
    elif location_command not in list_list_combine(all_bunker_locations):
        error()
    pass

#text functions

def description(description_command): #gives a description of a specific item
    if description_command in inventory:
        describe(description_command)
    if description_command in local_items: #all_items[0, 1 , 2 , 3 or 4]]
        print("I need to have this item to describe it.")
    pass

def help():
    print(location_msg)
    print("write \"check commands\" to see a list of commands")
    pass


def check_for_items(command, area_item_locations):
    if command in area_item_locations and command in player_location:
            if len(local_items)>0:
                show_list(local_items)
            if len(local_items)==0:
                print("There are no items here.")
    if command in area_item_locations and command not in player_location:
        print(f"you have to be at the {command} to check it for items!")
    pass

def use_function(item):
    if item=="fishing_rod":
        



#def pre_use_function(item, inventory, correct_location):
 #   if item in inventory and player_location[0] in correct_location:
  #      use_function(item)
   # pass

#1

def one_word_commands_standalone(first_command):
    if first_command in list_list_combine(all_bunker_locations): #maybe change
        pre_location_change(first_command)
    if first_command in local_items:
        print(f"what would you like to do with the {first_command}?")
    if first_command == "help":
        help()
    pass

def one_word_commands(command):
    if command in inventory:
        description(command)
    
    if command == "location":
        location_print()

    if command == "locations":
        print(location_msg)

    if command == "inventory":
        show_list(inventory)

    if command == "commands":
        show_list(all_commands)

    pass

#2

def two_word_commands(first_command, second_command):
    if first_command == "check": 
        one_word_commands(second_command)
        
        check_for_items(second_command, bunker_item_locations)

    if first_command in ["go", "move"]: #if go ______ or move _____
        pre_location_change(second_command)

    if first_command == "take":
        pre_take_and_check(second_command, local_items)

    if first_command == "drop":
        if second_command in inventory:
            remove_and_check(second_command, local_items)

    if first_command == "describe":
        if second_command in local_items or inventory:
            description(second_command)
    return

#3

def three_word_commands(first_command, second_command, third_command):
    first_second_command=first_command+second_command

    if first_second_command in ["takethe", "pickup",]:
        pre_take_and_check(third_command, local_items)
    
    if first_second_command in ["goto", "moveto"]:
        pre_location_change(third_command)

    if third_command == "check" and second_command in preposition_list:

        check_for_items(third_command, bunker_item_locations)

        if third_command == "inventory":
            show_list(inventory)

        if third_command in local_items or inventory:
            description(first_command) #already has if statement in it

        if third_command == "commands":
            show_list(all_commands)
        


            
    return


#events. have their own check and shit
def fishing_rod_event():
    pass
def exit_unlock_event():
    pass



#END OF ADVANCED FUNCTIONS

#GAME SCRIPT
while game_run==True:
    if first_time==True:
        first_time_function()
    command_list = command_list_function(str(input()))
    # print(command_list) # for bug testing
    if len(command_list)==0:
        error()
    if len(command_list)==1:
        first_command=command_list[0]
        one_word_commands(first_command)
    if len(command_list)==2:
        first_command=command_list[0]
        second_command=command_list[1]
        two_word_commands(first_command, second_command)
    if len(command_list)==3:
        first_command=command_list[0]
        second_command=command_list[1]
        third_command=command_list[2]
        three_word_commands(first_command, second_command, third_command)

    


