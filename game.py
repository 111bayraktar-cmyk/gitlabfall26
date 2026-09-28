#A student led RPG game

#contributors
#gpoppe


#imported libraries

import math
import time

#function definitions

def room1():
    #room1
    print("This door is locked.")

def room2():
    #room2
    print("This door is locked.")

def room3():
    #room3
    print("This door is locked.")

def room4():
    #room4
    #Alejandra Ibarra
    print("Pokemon Master")

def room5():
    #room5
    #Carmen Aguilar-Reyes
    print("Legendary Adventurer")
 
    name = input ("Welcome adventurer!What is your name?: ")

    print ("Hello", name, "you have discovered a mysterious island filled with ancient secrets.")
    print ("Your goal is to find the legendary Crystal to help you escape the island.")

    print ("You arrived at a fork in the path")

    print("1. Enter the jungle")
    print("2. Climb the mountain trail")
    print("3. Follow the beach")
    choice1 = input("Which path do you choose? ")


    if choice1 == "1":
        print(name, "enters the jungle.")
    elif choice1 == "2":
        print(name, "climbs the mountain trail.")
    elif choice1 == "3":
        print(name, "follows the beach.")
    else:
        print("You got lost and the adventure ends.")
        return
# Decision 2

    print("You discover an abandoned camp with three useful items.")
    print("1. Compass")
    print("2. Flashlight")
    print("3. Rope")
    choice2 = input("Which item do you take? ")


    if choice2 == "1":
        print("You take the compass.")
    elif choice2 == "2":
        print("You take the flashlight.")
    elif choice2 == "3":
        print("You take the rope.")
    else:
        print("You waste too much time and the adventure ends.")
        return 

# Decision 3

    print("Later, you reach a rushing river.")
    print("1. Swim across")
    print("2. Build a raft")
    print("3. Search for a bridge")
    choice3 = input("What do you do? ")

    if choice3 == "1":
        print("You carefully swim across.")
    elif choice3 == "2":
        print("You build a sturdy raft.")
    elif choice3 == "3":
        print("You find an old bridge and cross safely.")
    else:
        print("You fall into the river and lose the adventure.")
        return

# Decision 4

    print("You discover the entrance to an ancient temple.")
    print("1. Enter through the main gate")
    print("2. Use a hidden side entrance")
    print("3. Climb through a rooftop opening")
    choice4 = input("How will you enter? ")

    if choice4 == "1":
        print("You walk through the massive gate.")
    elif choice4 == "2":
        print("You sneak through the side entrance.")
    elif choice4 == "3":
        print("You climb into the temple from above.")
    else:
        print("You trigger a trap and lose.")
        return

# Decision 5

    print("Inside the temple are three crystal pedestals.")
    print("1. Red Crystal")
    print("2. Blue Crystal")
    print("3. Green Crystal")
    choice5 = input("Which crystal will you take? ")

    if choice5 == "1":
        print("The temple begins to glow!")

    elif choice5 == "2":
        print("The temple begins to glow!")
    elif choice5 == "3":
        print("The temple begins to glow!")
    else:
        print("The temple collapses before you make a choice.")
        return
#Decision Treasure
    
    print ("While exploring the temple, you find a treasure chest!")
    print ("1. Open it")
    print ("2. Ignore it")
    print ("3. Inspect it carefully")

    treasurechoice = input("What do you do?")

    if treasurechoice == "1": 
        print ("You found the Golden Idol!")
    elif treasurechoice == "2": 
        print ("You leave the chest alone.")
    elif treasurechoice == "3": 
        print ("You discovered an Ancient map.")
    else: 
        print ("You walk away from the chest")
        return 

# Decision 6

    print("You must escape the island.")
    print("1. Sail away on a boat")
    print("2. Fly away in an ancient airship")
    print("3. Use a hidden portal")
    choice6 = input("How will you escape? ")

    if choice6 == "1":
        print("Congratulations", name,  "! You sail away with the Crystal of Destiny and win!")
    elif choice6 == "2":
        print("Congratulations", name, "! You fly away with the Crystal of Destiny and win!")
    elif choice6 == "3":
        print("Congratulations", name, "! You step through the portal with the Crystal of Destiny and win!")
    else:
        print("You hesitate too long and remain trapped on the island.")

# Main game loop

    play_again = input("Would you like to play again? ")

    if play_again == "yes": 
        room5()
    else: 
        print("Thanks for playing!")

    
def room6():
    #room6
    print("This door is locked.")

def room7():
    #room7
    print("This door is locked.")

def room8():
    #room8
    print("This door is locked.")

def room9():
    #room9
    print("This door is locked.")

def room10():
    #room10
    print("This door is locked.")

def room11():
    #room11
    print("This door is locked.")

def room12():
    #room12
    print("This door is locked.")

def room13():
    #room13
    print("This door is locked.")

def room14():
    #room14
    print("This door is locked.")

def room15():
    #room15
    print("This door is locked.")

def room16():
    #room16
    print("This door is locked.")

def room17():
    #room17
    print("This door is locked.")

def room18():
    #room18
    print("This door is locked.")

def room19():
    #room19
    print("This door is locked.")

def room20():
    #room20
    print("This door is locked.")

def room21():
    #room21
    print("This door is locked.")

def room22():
    #room22
    print("This door is locked.")

def room23():
    #room23
    print("This door is locked.")

def room24():
    #room24
    print("This door is locked.")

def room25():
    #room25
    print("This door is locked.")

def room26():
    #room26
    print("This door is locked.")

def room27():
    #room27
    print("This door is locked.")

def room28():
    #room28
    print("This door is locked.")

def room29():
    #room29
    print("This door is locked.")

def room30():
    #room30
    print("This door is locked.")

def room31():
    #room31
    print("This door is locked.")

def room32():
    #room32
    print("This door is locked.")

def room33():
    #room33
    print("This door is locked.")

def room34():
    #room34
    print("This door is locked.")

def room35():
    #room35
    print("This door is locked.")

def room36():
    #room36
    print("This door is locked.")

def room37():
    #room37
    print("This door is locked.")

def room38():
    #room38
    print("This door is locked.")

def room39():
    #room39
    print("This door is locked.")

def room40():
    #room40
    print("This door is locked.")

def room41():
    #room41
    print("This door is locked.")

def room42():
    #room42
    print("This door is locked.")

def room43():
    #room43
    print("This door is locked.")

def room44():
    #room44
    print("This door is locked.")

def room45():
    #room45
    print("This door is locked.")

def room46():
    #room46
    print("This door is locked.")

def room47():
    #room47
    print("This door is locked.")

def room48():
    #room48
    print("This door is locked.")

def room49():
    #room49
    print("This door is locked.")

def room50():
    #room50
    #garrett poppe
    print("Game Title: Best Game Ever!")


#main program

mainChoice = 0

print("____________________________________")
print("")
print("Welcome to the role playing game!")
time.sleep(1)
print(".....")
time.sleep(1)
print("....")
time.sleep(1)
print("...")
time.sleep(1)
print("..")
time.sleep(1)
print(".")
time.sleep(1)
print("You wake up and find yourself in the center of a massive room.")
print("You do not know how you arrived here, but you look around and realize you are at the center of the room.")
print("The walls of this circular room are made of many doors.")
print("Each door has a finely crafted number plate. It appears there are 50 doors.")
print("All of a sudden, the room starts to fill with water. You must act quickly before the room floods and you drown.")
mainChoice = int(input("You decide you're going to exit through one of the doors. Which door number do you choose? "))

if mainChoice == 1:
    room1()
elif mainChoice == 2:
    room2()
elif mainChoice == 3:
    room3()
elif mainChoice == 4:
    room4()
elif mainChoice == 5:
    room5()
elif mainChoice == 6:
    room6()
elif mainChoice == 7:
    room7()
elif mainChoice == 8:
    room8()
elif mainChoice == 9:
    room9()
elif mainChoice == 10:
    room10()
elif mainChoice == 11:
    room11()
elif mainChoice == 12:
    room12()
elif mainChoice == 13:
    room13()
elif mainChoice == 14:
    room14()
elif mainChoice == 15:
    room15()
elif mainChoice == 16:
    room16()
elif mainChoice == 17:
    room17()
elif mainChoice == 18:
    room18()
elif mainChoice == 19:
    room19()
elif mainChoice == 20:
    room20()
elif mainChoice == 21:
    room21()
elif mainChoice == 22:
    room22()
elif mainChoice == 23:
    room23()
elif mainChoice == 24:
    room24()
elif mainChoice == 25:
    room25()
elif mainChoice == 26:
    room26()
elif mainChoice == 27:
    room27()
elif mainChoice == 28:
    room28()
elif mainChoice == 29:
    room29()
elif mainChoice == 30:
    room30()
elif mainChoice == 31:
    room31()
elif mainChoice == 32:
    room32()
elif mainChoice == 33:
    room33()
elif mainChoice == 34:
    room34()
elif mainChoice == 35:
    room35()
elif mainChoice == 36:
    room36()
elif mainChoice == 37:
    room37()
elif mainChoice == 38:
    room38()
elif mainChoice == 39:
    room39()
elif mainChoice == 40:
    room40()
elif mainChoice == 41:
    room41()
elif mainChoice == 42:
    room42()
elif mainChoice == 43:
    room43()
elif mainChoice == 44:
    room44()
elif mainChoice == 45:
    room45()
elif mainChoice == 46:
    room46()
elif mainChoice == 47:
    room47()
elif mainChoice == 48:
    room48()
elif mainChoice == 49:
    room49()
elif mainChoice == 50:
    room50()
else:
    print("That was the wrong choice....")
    time.sleep(1)
    print("You have perished.")


print("____________________________________")
print("")
time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(1)
print("....")
time.sleep(1)
print(".....")
time.sleep(1)
print("You wake up and realize this was all a dream.")


