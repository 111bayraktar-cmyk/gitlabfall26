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
    #Alejandra Ibarra

    newlist = ["Pick a starter pokemon:","1.Piplup","2.Chimchar","3.Turtwig"]
        
    option1 = ["Pick a starter pokemon:","1.Squirtle","2.Charmander","3.Bulbasaur"]

    option2 = ["How do you want to dress your Pokemon:","1.Goggles","2.Top Hat","3.Party Hat"]

    option3 = ["What do you want to do with your starter:","1.Free Play","2.Battle Ground","3.Show off your pokemon!"] 

    option4 = ["Do you wish to evolve your Pokemon?:","1.No.","2.Evolve Once","3.Fully Evolve"]

    option5 = ["Your Pokemon is being attacked, how do you wish to proceed?:","1.Join your Pokemon in battle.","2.Catch the Pokemon yourself.","3.Watch your Pokemon battle."]

    redo_game = ["Do you want to play again?", "1.Yes", "2.No"]
    again = 1
    while(again==1):
        print("Welcome Trainer, your Pokemon adventure begins now! Lets see if you have what it takes to become a Pokemon Master!")

#Level1
    
        choice = int(input("Do you want starters from generation 1 or 4? "))
        if choice == 1:

            for item in option1:
                print(item)

            starter_choice = int(input("Pick a number 1-3: "))

            if starter_choice == 1:
                print("A smart choice! Squirtle is ready to make a splash and take on whatever challenges come your way.")

            if starter_choice == 2:
                print("Your adventure is heating up. Charmander is ready to bring the energy and power through every challenge.")

            if starter_choice == 3:
                print("The best choice! Bulbasaur is ready to grow, learn, and tackle every challenge that comes your way.")
        else:

            for item in newlist:
                print(item)
        
            starter_choice = int(input("Pick a number 1-3: "))

            if starter_choice == 1:
                print("Leave the familiar behind and experience the Sinnoh region!")
                print("Piplup is excited to start your journey together!")

            if starter_choice == 2:
                print("Leave the familar behind and experience the Sinnoh region!")
                print("Chimchar is bursting with energy and ready to start your journey together!")

            if starter_choice == 3: 
                print("Leave the familiar behind and experience the Sinnoh region!")
                print("Turtwig is ready to step forward and follow you on your adventure!")

    
        print("Before begining your journey lets dress your Pokemon!")

#Minigame/Loop
        mini=True
        print("Lets play a minigame.")
        pokemans = ["1.Luigia", "2.Diglett", "3.Mudkip", "4.Drilbur", "5.Garchomp", "6.Applin"]
        while(mini):
            for poke in pokemans:
                print(poke)
            guess = int(input("Guess what my favorite Pokemon is: "))
            if guess == 6:
                mini = False 
        print("Congrats you guessed correctly, I love Applin and his green shiny!<3")

#Level2
        for item in option2:
            print(item)

        dress_choice = int(input("Pick a number 1-3: "))

        if dress_choice == 1:
            print("Adventure mode on! Your Pokemon is geared up and ready to explore, discover, and take on the next challenge!")

        if dress_choice == 2:
            print("Fancy choice, trainer! Your Pokemon is looking ready for a VIP battle.")

        if dress_choice == 3:
            print("Party time! Your Pokemon is ready to party AND play.")
#Level3
        for item in option3:
            print(item)
    
        journey = int(input("Pick a number 1-3: "))

        if journey == 1:
            print("No rules, no pressure... just explore, experiment and have fun! Take your Pokemon on an adventure and see what you discover!")

        if journey == 2:
            print("Its time to put your skill to the test. Choose your moves wisely, earn XP, and see if you have waht it take to battle!")

        if journey == 3:
            print("Your Pokemon is ready for the spotlight! Show off your style and let everyone see your AWESOME Pokemon. Remember: Strike a pose, trainer!")

        for item in option4:
            print(item)

        evolution = int(input("Pick a number 1-3: "))

        if evolution == 1:
            print("Staying just the way you are! Your Pokemon doesnt need to evolve to be awesome. Keep training, keep learning, and show everyone what you can do!")

        if evolution == 2:
            print("Evolution unlocked! Your Pokemon has leveled up and grown stronger. Look at you go, trainer.")

        if evolution == 3:
            print("You've powered up your Pokemon ALL the way. Your dedication has paid off, and your Pokemon has reached its final form. You are on step close to become a Pokemon Master.")

#Level5
    
        for item in option5:
            print(item)

        attack = int(input("Pick a number 1-3: "))

        if attack == 1:
            print("Teamwork makes the dream work, trainer! Your Pokemon is stonger wit you by its side. You really are a Pokemon Master.")

        if attack == 2:
            print("You fool! You should know working together is ALWAYS the right choice. You are not ready to be a Pokemon Master.")

        if attack == 3:
            print("You stand back and watch your Pokemon battle?? Uh-Oh. NEVER leave your Pokemon to battle alone! Your Pokemon needs you by their side.")


#End Game
    
        for item in redo_game:
            print(item)
    
        again = int(input("Please enter 1 or 2: "))

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


