import time
import random

#use if specific_item in inventory to check if player has correct item

items_ground_bunker_main = ["food", "pistol", "0.25$",  ] #useless for now, will be used to compare item in all_items and in correct location
all_commands=["check", "take", "drop", "look", "go", "pick"]
all_items = ["food", "pistol", "$0.25",  ]
inventory = ["banana", "orange", "purple", ]
game_run=True
first_word=str(0)
first_time=True
third_word=0

middle = ["middle", "m", 0]
north = ["north", "n", "desk", 1]
east = ["east", "e", "cabinets", 2]
west = ["west", "w", "kitchen", 3]
south = ["south", "s", "exit", 4]

player_location = random.randint(0, 4)


#basic functions
def delay(delay_seconds):
    time.sleep(delay_seconds)
    pass

def stripper(input_string):
    output_string = str(input_string).strip().lower()
    return output_string

def show_list(item_list):
    n=0
    while n!=(len(item_list)):
        print(item_list[n])
        n=n+1

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
    if first_time==True:
        print("write \"check commands\" to see a list of commands")
        first_time=False
    return first_time


def command_list_function(command): #creates a list of commands the user inputted
    command_list=[]
    if " " not in command:
        command_list.append(command)
        pass
    elif " " in command:
        first_space=command.find(" ")
        if command.find(" ")==command.rfind(" "):
            first_word=command[:first_space]
            second_word=command[(first_space+1):]
            command_list.append(first_word)
            command_list.append(second_word)
            pass
        elif command.find(" ")!=command.rfind(" "):
            second_space=command.rfind(" ")
            first_word=command[:first_space]
            second_word=command[(first_space+1):second_space]
            third_word=command[(second_space+1):]
            command_list.append(first_word)
            command_list.append(second_word)
            command_list.append(third_word)
            pass
        pass
    return command_list

def describe(item):
    if item=="pistol":
        print("A semi-automatic pistol. 9x19 caliber. I have extra magazines, so no need to worry about that.")
        pass
    if item=="food":
        print("Some extra food scraps I managed to find. Might be useful, although I haven't been feeling hungry lately")
        pass
    if item=="$0.25":
        print("I literally have no use for money... although this quarter might be unconventionally useful.")
        pass
    else:
        print("I have no description for this.")
        pass
    pass



#advanced functions (uses prev. functions)
def take_and_check(taken_item, placeholder_item_list): #takes and checks the validity of an item
    if taken_item in placeholder_item_list and taken_item not in inventory: #REMEMBER, ITEM LIST IS A PLACEHOLDER VARUIABLE
        if len(inventory)<=7:
            add_item(taken_item, inventory) #adds to inventory
            print(f"you add the {taken_item} to your inventory")
            remove_item(taken_item, placeholder_item_list) #removes from all_items
        elif len(inventory)>7:
            print(f"you do not have enough space for the {taken_item}")
    elif taken_item in inventory:
        print("item is already in inventory") #may not need in future
    elif taken_item not in placeholder_item_list:
        error()
    return inventory

def remove_and_check(removed_item, placeholder_item_list):
    if removed_item not in placeholder_item_list and removed_item in inventory:
        remove_item(removed_item, inventory)
        print(f"you drop the {removed_item} from your inventory")
        add_item(removed_item, placeholder_item_list)
    elif removed_item in placeholder_item_list:
        print("you do not have this item")
        pass
    pass

def one_word_command_location(one_word_command):
    global player_location
    if one_word_command in middle:
        player_location="middle"
    if one_word_command in north:
        player_location="north"
    if one_word_command in east:
        player_location="east"
    if one_word_command in west:
        player_location="west"
    if one_word_command in south:
        player_location="south"
    print(f"your location is now {player_location}")
    return player_location

def one_word_command_description(one_word_command):
    if one_word_command in inventory:
        describe(one_word_command)
        pass
    if one_word_command not in inventory:
        print("I need to have this item to describe it.")
    return



def one_word_commands(first_command):
    one_word_command_location(first_command)
    one_word_command_description(first_command)
    pass
def two_word_commands():
    pass
def three_word_commands(): 
    pass


while game_run==True:
    first_time_function()
    command_list = command_list_function(stripper(str(input())))
    print(command_list) # for bug testing
    if len(command_list)==0:
        error()
    if len(command_list)>=1:
        first_command=command_list[0]
        if len(command_list)==1:
            one_word_commands(first_command)
        pass
    if len(command_list)>=2:
        second_command=command_list[1]
        if len(command_list)==2:
            two_word_commands(first_command, second_command)
        pass
    if len(command_list)>=3:
        third_command=command_list[2]
        if len(command_list)==3:
            three_word_commands(first_command, second_command, third_command)
        pass
    #while player_location in middle:
    if first_command == "go":
        pass
    if first_command == "look":
        pass
    if first_command == "take":
        take_and_check(second_command, all_items)
        pass
    if first_command == "drop":
        remove_and_check(second_command, all_items)
        pass
    if first_command == "check":
        if second_command == "location":
            print("player_location")
            pass
        if second_command == "inventory":
            show_list(inventory)
            pass
        if second_command == "commands":
            print("write one of these words:")
            show_list(all_commands)
            print("combined with a second, specific word")
            print("hint: write \"check ground\"")
            pass
        if second_command == "ground":
            show_list(all_items)
        pass
    if first_command == "pick":
        if second_command == "up":
            take_and_check(third_command, all_items)
        pass
    elif first_command not in all_commands:
        error()
        pass

