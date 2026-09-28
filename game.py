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
    print("This door is locked.")

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
    #Ceiry Molina
    #room12
    print("Ceiry's Game!")

    opt1 = ["Choose you Jedi:","1.Luke Skywalker","2.Obi Wan","3.Ahsoka"]

    opt2 = ["How do you want to eqip your compasnion:","1.Jedi Robes","2.Clome Armor","3.Mandalorian Cape"]

    opt3 = ["What mission do you want  to begin:","1.Explore a New Planet", "2.Battle the Empire","3.Attend a Galactic Celebration"]

    opt4 = ["Do you wish to upgrade your companion's Force abilities?:","1.No", "2.Increase Training","3.Master the Force"]

    opt5 = ["The Empire is attacking! How do you wish to proceed?:","1.Fight alongside your companion","2.Face the enemy alone","3.Stay back and watch"]

    opt6 = ["While on a mission you find a box! How do you wish to proceed?:","1.Open it", "2.Ignore it","3.Inspect it"]

    redo_game = ["Do you want to play again?","1.Yes","2.No"]
    again = 1 
    while(again ==1):
        print("Welcome, young Padawan! Your Star Wars adventure begins now. May the Force be with you!")

    #Level1
        for item in opt1:
            print(item)

        starter_choice = int(input("Pick a number 1-3:"))

        if starter_choice ==1:
            print("Luke Skywalker joins your journey! His courage and determination will guide you through the galaxy.")

        if starter_choice ==2:
            print("A wise choice. Obi Wan is ready to share the wisdom of the Jedi Order")

        if starter_choice ==3:
            print("Excellent choice! Ahsoka is prepared to face% any challenge and protect the galaxy")
        
        print("Before beginning your mission, let's prepare you companion!")

    #Level2
        for item in opt2:
            print(item)
    
        dress_choice = int(input("Pick a number 1-3:"))

        if dress_choice ==1:
            print("Classic Jedi style! Your companion is prepared for an honorable mission across the stars.")

        if dress_choice ==2:
            print("Battle ready! Your companion looks prepared to take on Imperial forces.")
        if dress_choice ==3:
            print("An impressive look! Your companion stands out as a true galactic hero.")

    #Level3 
        for item in opt3:
            print(item)

        journey = int(input("Pick a number 1-3:"))

        if journey ==1:
            print("Adventure awaits! Discover hidden worlds, ancient secrets, and new allies throughout7 the galaxy.")

        if journey ==2:
            print("The battle begins! Use strategy, teamwork, and the Force to defeat the Empire")

        if journey ==3: 
            print("A celebration across the galaxy! Show off your companion and enjoy the festivities")

    #Level4
        for item in opt4:
            print(item)

        evolution = int(input("Pick a number 1-3:"))

        if evolution ==1:
            print("Your companion remains as they are. Remember true strength comes from within")

        if evolution ==2:
            print("Training complete!Your companion has grown stronger and gained new Force abilities")

        if evolution ==3:
            print("Force mastery achieved! Your companion has reached their highest potential and become a legendary hero")

    #Level5

        for item in opt5:
            print(item)

        attack = int(input("Pick a number 1-3:"))

        if attack ==1:
            print("Together you fight! The force is strongest when allies stand side by side;")

        if attack ==2:
            print("Bravery is admirable, but teamwork is the Jedi way. Facing the enemy alone is risky.")

        if attack ==3:
            print("Standing aside while others fight is not the Jedi path. Heroes help those in need!")

    #Level6 

        for item in opt6:
            print(item)

        box_choice = int(input("Pick a number 1-3:"))

        if box_choice ==1:
            print("Congrats you found a purple light saber!!")

        if box_choice ==2:
            print("You leave the box alone very safe choice!")

        if box_choice ==3:
            print("You find a green light saber, very good choice!")

    #End Game 
        for item in redo_game:
            print(item)

        again = int(input("Please enter 1 or 2:"))

def room13():
    #room13
    #Muhammad Mahmood
    print("Fallout 389")

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
    #Vicky Kong
    print("Journey to K-Pop Concert")

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


