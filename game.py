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
    again = "yes"

    def choice1(input1):
        print("")
        print("You discover a dusty old map showing escape route. What do you want to do with map?")
        print("")
        print("1. Follow the marked trail")
        print("2. Ignore the map and explore freely")
        print("3. Tear the map open (something is inside)")
        option1 = int(input("Choose one of the following options."))
        if option1==1:
            print( name, " , as you are following the marked trail, you found the old bunker.")
            option10=choice2(option1)
            return option10
        elif option1==2:
            print( name, " , since you ignored the map;")
            option11=choice4(option1)
            return option11
        elif option1==3:
            print(name, ", you tear the map open and find a metal key which you used to call tribal warrior.")
            option12 = choice2(option1)
            return option12
    
        
    
    def choice2(input2):
        print("")
        print("A tribal warrior appears and calls out to you.")
        print("")
        print("1. Ask the warrior for help")  
        print("2. Hide behind rocks")
        print("3. Offer the metal key you found")
        option3 = int(input("What do you choose? "))
        if option3==2:
            print(name,", as you were hiding behind the underground door.")
            option13= choice4(option3)
            return option13  
        if option3==1:
            print (name, ", a warrior appear in front of you and showed you the cave")
            option14= choice3(option3)
            return option14
        if option3==3:
            print(name, ", in exchange of the metal key you warrior showed you a way to the island.")
            option15= choice5(option3)
            return option15
    
    def choice3(input3):
        print("")
        print("You reach the base of the volcano. Smoke fills the air.")
        print("")
        print("1. Enter the lava tube tunnel")  
        print("2. Climb the outer ridge")
        print("3. Search for the old bunker")
        option4 = int(input("What do you choose? "))
        if option4==1:
            print(name, ", you have reached to the end of the tunnel.")
            option16= choice5(option4)
            return option16
        if option4==2:
            print(name, ", you have found a key on the way the island.")
            option17= choice2(option4)
            return option17
        if option4==3:
            print(name, ", you found the old map in the old bunker.")
            option18=choice1(option4)
            return option18
    
    def choice4(input4):
        print("")
        print("A loud alarm blares—the final evacuation is happening now!")
        print("")
        print("1. Board the rescue helicopter")  
        print("2. Sail away on a wooden raft")
        print("3. Ride a zipline across the canyon")
        option5 = int(input("What do you choose? "))
        if option5 == 1:
            print("The helicopter lifts off just as the volcano erupts." ,name , " , you have successfully escaped Volcano Island!")
        elif option5 == 2:
            print("The raft carries you away, but the waves grow violent.", name, ", you barely escape with your life!")
        elif option5 == 3:
            print("The zipline snaps halfway across the canyon.", name, ", you fall into the jungle and perish.")
        else:
            print(name, "your hesitation costs you precious time. The volcano erupts and you do not survive.")
        
        return option5
    
    def choice5(input5):
        print("")
        print("You walk deeper into the island and reach a dangerous crossroads.")
        print("The volcano shakes violently, and you must choose quickly.")
        print("")
        print("1. Cross the shaky wooden bridge")
        print("2. Crawl through a narrow lava tunnel")
        print("3. Climb the steep rocky cliff")
        print("4. Follow the hidden path behind the waterfall")
        option6 = int(input("What do you choose? "))
    
        while option6 < 1 or option6 > 4:
            option6 = int(input("Choose option from above. What do you choose? "))
    
        if option6 == 1:
            print(name, ", you carefully cross the shaky bridge and reach a safe zone.")
            return choice4(option6)
    
        elif option6 == 2:
            print(name, ", you crawl through the lava tunnel and barely escape the heat.")
            return choice4(option6)
    
        elif option6 == 3:
            print(name, ", you climb the cliff and see the evacuation area from above.")
            return choice4(option6)
    
        elif option6 == 4:
            print(name, ", you follow the hidden path and discover a secret rescue station!")
            return choice4(option6)
    
     #Main body
    name = str(input("Welcome traveler!  What is your name? "))
    while again =="yes" or again == "Yes" or again== "YES":
    
        
        print("Hello ", name , " you wake up on a mysterious island.  The ground shakes beneath you. A volcano at the center of the island is about to erupt.  You must escape")
        print(" ")
        print(" You see three possible paths in front of you. ")
        print ("************************************************************")
        print ("1. Climb the watch tower")
        print ("2. Go to the jungle")
        print ("3. Go to the beach")
        print ("************************************************************")
        option= int(input("what do you choose, before lava gets to you? "))
        
        if option==1:
            print( name, " , you just climbed the watch tower and reached the top.")
            option1=choice1(option)
          
        
        if option==2:
            print(name, " , you are in the jungle now. ")
            option2 = choice2(option)
        if option == 3:
            print (name, ", you are the beach where you can hear the sound of waves. Danger is still dangling.")
            option3 = choice3(option)
            
    
        while option <1 or option>3 :
            option = int(input("Choose option from above. What do you choose? "))  
    
        print (" ")
        again = input("Would you like to play again? (yes/no)")
    print("Thank you for playing! Have a mathemagical day!")
    

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
    #Mario Magallanes
    print("")
    print("Video Game Labyrinth")

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


