#A student led RPG game

#contributors
#gpoppe


#imported libraries

import math
import time

#function definitions

def room1():
    #room1
    #Ted :)
    print("Walt Disney World Vacation")

def room2():
    #room2
    print("This door is locked.")

def room3():
    #room3
    #Arpita Shah
    print("Let's Mathify this game.")

def room4():
    #room4
    #Alejandra Ibarra
    print("Pokemon Master")

def room5():
    #room5
    #Carmen Aguilar-Reyes
    print("Legendary Adventurer")

def room6():
    #room6
    #Angela Vasquez
    print("Welcome to The Halloween Adventure Park!")

def room7():
    #room7
    print("This door is locked.")

def room8():
    #room8
    print("Welcome to the best game!")

def room9():
    #room9
    print("This door is locked.")

def room10():
    #room10
    #lauren bowman
    print("The Music Career Game!")

def room11():
    #room11
    #Timothy Duong
    print("Survive a Day of Work!")

def room12():
    #Ceiry Moline
    #room12
    print("Ceiry's Game!")

def room13():
    #room13
    #Muhammad Mahmood
    print("Fallout 389")

def room14():
    #room14
    # Jeff Yock
    print("Best Student Ever")

def room15():
    #room15
    #Jitender Rajpoot
    print("Final Destination.")

def room16():
    #room16
    # Moshe Molcho
    print("Escape the Possessed Math Classroom")

def room17():
    #room17
    #Josue Zamora
    print("Two Minute Drill")

def room18():
    #room18
    #Cesar Cano
    print("Dark Gengar.")

def room19():
    #Patricia Flores
    print("Star Wars")

def room20():
    #room20
    print("This door is locked.")

def room21():
    #room21
    #Dawei Sun
    print("The Lost Jade Pendant")


def room22():
    #room22
    #Rogelio Jeronimo
    print("Playing in the Fun House.")

def room23():
    #room23    
    # Mario Magallanes

    game = 1
    option = 0
    name = input("Greetings, What is your name?: ")
    print ("")
    print (name, "You are about to enter the video game labyrinth. You will go through 6 chambers.")
    print ("Each chamber will have items or fighters for you to select.")
    print ("Chose carefully. The outcome can be to advance, to reset, or to die for.")

#chamber 1 
    while game != 0:
        if game == 1:
            print("")
            print("****************")
            print ("Welcome to the Game of Zelda Chamber.")
            print (" 1 The Ocarina of Time ")
            print (" 2 Master Sword ")
            print (" 3 Hyland Shield ")
            print ("****************")
            print (name)
            option = int(input("Please make your selection: "))

            if option == 1:
                print ("The Ocarina of Time will let you move forward")
                game = 2
        
            elif option == 2:
                print ("The Master Sword will let you try again")
                game = 1
        
            elif  option == 3:
                print ("The Hyland Shield will kill you")
                game = 0 

#chamber 2 
        if game == 2:
            print("")
            print("****************")
            print ("Welcome to the Mario World Chamber.")
            print (" 1 Koopa ")
            print (" 2 Goomba ")
            print (" 3 Shy Guy ")
            print ("****************")
            print (name)
            option = int(input("Please make your selection: "))

            if option == 1:
                print ("You defeated Koopa. Move Forward")
                game = 3
        
            elif option == 2:
                print ("It is a tie! Try again")
                game = 2
        
            elif  option == 3:
                print ("The Shy Guy was too much for you!")
                game = 1 

#chamber 3 
        if game == 3:
            print("")
            print("****************")
            print ("Welcome to the Contra Chamber.")
            print (" 1 Spear Gun ")
            print (" 2 Laser Gun ")
            print (" 3 Rapid Fire ")
            print ("****************")
            print (name)
            option = int(input("Please make your selection: "))

            if option == 1:
                print ("The Spear Gun is a keeper. Move Forward")
                game = 4
        
            elif option == 2:
                print ("The Laser Gun is defective, Try again")
                game = 3
        
            elif  option == 3:
                print ("Rapid Fire Gun exploded in your hand. Try Again!!")
                game = 1 

#chamber 4 
        if game == 4:
            print("")
            print("****************")
            print ("Welcome to the Pac-Man Chamber.")
            print (" 1 Blinky ")
            print (" 2 Pinky ")
            print (" 3 Inky ")
            print (" 4 Clyde ")
            print ("****************")
            print (name)
            option = int(input("Please make your selection: "))

            if option == 1 or option == 2:
                print ("You defeated Blinky or Pinky. Move Forward")
                game = 5
        
            elif option == 3:
                print ("It is a tie! Try again")
                game = 4
        
            elif  option == 4:
                print ("The Shy Guy was too much for you!")
                game = 0 

#chamber 5 
        if game == 5:
            print("")
            print("****************")
            print ("Welcome to the Street Fighter Chamber.")
            print (" 1 Hadouken ")
            print (" 2 Shoryuken ")
            print (" 3 Sonic Boom ")
            print ("****************")
            print (name)
            option = int(input("Please make your selection: "))

            if option == 1:
                print ("The Hadouken served you well! Move to the next level")
                game = 6
        
            elif option == 2:
                print ("It is a tie! Try again")
                game = 2
        
            elif  option == 3:
                print ("The Sonic Boom took you off!")
                game = 0 

#chamber 6 
        if game == 6:
            print("")
            print("****************")
            print ("Welcome to the Castlevania's Chamber. Select your opennet Trevor Belmont!")
            print (" 1 Count Dracula")
            print (" 2 Medusa ")
            print (" 3 Death ")
            print ("****************")
            print (name)
            option = int(input("Please make your selection: "))

            if option == 1:
                print ("You defeated the game!!!")
                print (name)
                game = int(input("Enter 1 if you wan to play again and 0 to end the game: "))
        
            elif option == 2:
                print ("It is a tie! Try again")
                game = 6
        
            elif  option == 3:
                print (name)
                print ("Since you had an honorable defeat. Death will grant you a second cahnce!")
                game = 1 

        if game == 0: 
            print("")
            print ("You lost your life! Thank you for playing")
            print (name)
            game = int(input(" Enter 1 if you wish to play again. 0 if you don't:  "))

def room24():
    #room24
    print("This door is locked.")

def room25():
    #room25
    print("This door is locked.")

def room26():
    #room26
    #Janelle Piva
    print("The Haunted School.")

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
    #Tonya McIntyre
    print("Wise One")
    

def room31():
    #room31
    #Karl Kottman
    print("Musical Odyssey")

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


