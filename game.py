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
    print("You are going to a K-Pop concert soon. Let's see how prepared you are to go the concert!")

    name=input("What is your name super fan?")

    x="yes"

    while(x=="yes"):
        play=True

        #part 1
        print("Hello",name,"! before we start heading out, you need to choose an outfit!")
        print("1. Comfy outfit")
        print("2. Silly Costume")
        print("3. Nice outfit")
        y=int(input("Enter the number to choose your outfit!"))

        if(y==1):
            print("Nice choice! Being confortable is important to having fun at a concert!")
        if(y==2):
            print("All the fans around you will love your fit and take pictures with you! Everyone is having a good laugh.")
        if(y==3):
            print("You look really nice! Slayyyy!")

        #part 2
        print("Now that you have an outfit, let's pack your concert bag!")
        concertitems=["phone","portable battery","tickets","wallet","bottle of water","keys","portable fan","lightstick","polaroid","freebies"]
        print("In your concert bag, you have included:")
        for i in concertitems:
            print(i)
        print("Oh no! Your concert bag is full! You will need to take an item out.")
        print("1. Lightstick")
        print("2. Polaroid")
        print("3. Freebies")
        z=int(input("Enter the number to take out that item:"))

        if(z==1):
            print("You can't go to a K-Pop concert without a lightstick! You are not able to go to the concert anymore.")
            x=input("Would you like to play again?")
            play=False

        if(z==2):
            print("Good choice! You are not able to take a polaroid into the venue anyways. It is best to not bring it.")

        if(z==3):
            print("You must bring your freebies! It is K-pop culture to give out freebies to other fans.")
            x=input("Would you like to play again?")
            play=False

        #part 3
        if(x=="yes" and play): 
            print("Now that you are ready, let's plan out on when you should arrive to the venue!")
            print("1. 12pm")
            print("2. 5pm")
            print("3. 8pm")
            a=int(input("Enter the number for the time you plan to arrive at the venue:"))

            if(a==1):
                print("That is a bit early, but you got to exchange a lot of freebies with other fans!")

            if(a==2):
                print("5pm is a good time! You have enough time to find parking and line up to get inside the venue!")

            if(a==3):
                print("You are late! The concert has already started! You did not make it to the concert.")
                x=input("Would you like to play again?")
                play=False

        #part 4
        if(x=="yes" and play):
            print("Let's decide how you would get to the venue.")
            print("1. Driving")
            print("2. Public Transportation")
            print("3. Walking")
            b=int(input("Enter the number for your means of transportation:"))

            if(b==1):
                print("Not the best option in my opinion. Hope you are okay with paying for parking!")

            if(b==2):
                print("Public transportation is the best!")

            if(b==3):
                print("Walking is not a good option especially if you live far from the venue. You did not make it to the concert.")
                x=input("Would you like to pay again?")
                play=False

        #part 5
        if(x=="yes" and play):
            print("You have made it to the venue! Let's decide what you should do before going inside!")
            print("1. Use the restroom")
            print("2. Get food! Yum!")
            print("3. Buy merch!")
            c=int(input("Enter the number for the activity you want to do:"))

            if(c==1):
                print("Use the restroom inside the venue! The portable restrooms are so dirty!")
                x=input("Would you like to play again?")

            if(c==2):
                print("Yes! Eat before going in! The food inside the venue is overpriced.")
                print("Have fun at the concert!")
                x=input("Would you like to play again?")

            if(c==3):
                print("Yes! Buy some merch to commemorate tonight!")
                print("Have fun at the concert!")
                x=input("Would you like to play again?")

    print("Thank you for playing!")

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


