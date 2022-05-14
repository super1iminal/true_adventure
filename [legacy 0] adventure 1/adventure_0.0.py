"""
Asher Arya
Started Wednesday, September 5th, 2021
A text-based adventure game
"""

#what I learnt
"""
argument: the shit inside () or can be outside, like variable.find(), where variable is the argument
object: everything in python is an object.
    int, float, string, list, tuple, dictionary or set objects,
    user-defined objects, classes, functions, and *modules and packages* beyond the scope of what i'm doing
    list and tuple are similar, but tuple is unchangeable
return: necessary at the end of a function to return a value to the main code.
    you can have return without a specified value or omit it entirely, but in both cases no data will be sent back
    return can only be used in a function or method definition
    explicit return: immediately terminates a function's execution and sends the return value back to main code
        if you have a function that returns an explicit return value (e.g. 42), you can use that function as a variable (e.g. return_42() * 2)
    implicit return: either no return or no value attributed to return will return None (nothing), so no matter how complex your function is, it will return nothing if no value is assigned to return
    *return can return any object
    *you can have an expression in the return value slot
    ***any 
"""

import random
import time #for *suspense*
    #time.sleep(seconds)

def errorMessage(): #this is a procedure, as it performs actions without computing a final result. does not need return statement. basically, it only outputs, and returns nothing
    print("I didn't understand, please try again.")
    print()

def displayIntro(): #this is also a procedure, as it performs actions without computing a final result. does not need return statement
    print("It's the end of a long year of fighting space criminals")
    print("you come to  a crossroads on your trip home, one path leads home")
    print("where you will be handsomely rewarded for a job well done")
    print("and the other leads through a gamma ray burst that will disentigrate you")
    print()

    pass #null operation, just there to be syntaxically correct

def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation, prevents user from inputting garbage that will break function
        path =input("Which path will you choose? (1 or 2): ")

    return path

def checkPath(chosenPath): #the chosen path is a placeholder to use in the code. it's basically replacing the variable or value you'd put there in your actual code.
    print("You head down the path")
    time.sleep(2)
    print("there's an asteroidnearby that looks familiar, that must be a good sign...")
    time.sleep(2)
    print("But your skin begins to tingle..")
    print()

    correctPath = str(random.randint(1, 2))

    if chosenPath ==correctPath:
        print("That tingling was just the feeling of admiration whatever (good end)")
    else:
        print("Bad end")

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (yes/no)")

displayIntro()
choosePath()
