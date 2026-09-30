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

    def door1():
        print("Door 1: Private Piano Teacher")
        print ("You are teaching a student, but notice the piano bench is wobbly. What do you do next?")
        print ("1. Fix the bench before playing with a wrench.")
        print ("2. Swap out the bench for a chair.")
        print ("3. Ignore that the bench is broken, hop on the bench and play violently.")
   
        choice = input ("Choose 1,2, or 3: ")
        if choice == "1":
            print("You fix the bench and have a great lesson!")
        elif choice == "2":
            print ("The student learns discipline and becomes a great pianist. The parents help you by donating a new piano bench to you a week later.")
        elif choice == "3":
            print("The bench breaks, you fall, hit the back of your head on your floor and die.")
        else:
            print("Invalid choice. You wasted time and the lesson ended.")

    def door2():
        print("Door 2: Street performer")
        print(" You are playing at 3rd Street Promenade when a rival musician tries to take your spot. What do you do next? ")
        print ("1. Perform a duet together.")
        print ("2. Play louder to drown them out and attract more of a crowd.")
        print ("3. Physically attack the rival.")
   
        choice = input ("Choose 1, 2, or 3:")
        if choice == "1":
            print ("The crowd loves it! You both make a lot of money and become friends.")
        elif choice == "2":
            print ("You win the crowd over with your amazing skills.")
        elif choice == "3": 
            print ("The rival pulls out a knife and you die after being attacked.")
        else:
            print("Invalid choice. The rival steals your spot.")

    def door3():
        print("Door 3: Music Producer" )
        print (" Your high-teach studio console sparks during a big recording session. What do you do next?")
        print ("1. Call an electrician to fix it.")
        print ("2. Grab the live wires with bare hands.")
        print ("3. Switch to working on your laptop.")
   
        choice = input("Choose 1,2, or 3: ")
        if choice == "1":
            print ("The console gets fixed safely and you finish the album.")
        elif choice == "2":
            print ("You get electrocuted by high voltage and die.")
        elif choice == "3":
            print ("You finish the song on your computer thanks to your knowledge of music tech and production software and win a Grammy!")
        else: 
            print ("Invalid choice. You lose the project file.")

    def door4():
        print("Door 4: High School Band Director")
        print ("Right before a big championship, the band is out of tune. What do you do next?")
        print ("1. Tune every instrument carefully.")
        print ("2. Give an inspiring pep talk.")
        print ("3. Scold the band for being irresponsible.")

        choice = input("Choose 1,2, or 3: ")
        if choice == "1":
            print ("The band plays perfectly and wins 1st place because you took the time to tune them!")
        elif choice == "2":
            print ("The pep talk motivates them to play their best, but they didn't win the competition.")
        elif choice == "3":
            print ("The stress kills you and you have a heart attack on the football field right after they play.")
        else:
            print ("Invalid choice. The band misses their turn.")

    def door5():
        print("Door 5: Touring Musician")
        print("You are on stage at a huge rock concert with pyrotechnics going off. What do you do next?")
        print("1. Stay in your area onstage and play your solo.")
        print("2. Jump directly into the live flame cannons.")
        print("3. Jump off the stage into the crowd.")

        choice = input("Choose 1,2, or 3: ")
        if choice == "1":
            print("Your solo goes viral and you become famous!")
        elif choice == "2":
            print("You catch on fire and die instantly.")
        elif choice == "3":
            print("The crowd catches you and carries you around, then back onto the stage!")
        else:
            print ("Invalid choice. You miss your turn to play your solo.")

    def door6():
        print("Door 6: Wedding Singer")
        print("You are singing and playing guitar at a wedding reception and your break a string. What do you do? You are supposed to play for 2 hours.")
        print("1. You play all the songs on the guitar with the broken string, revoicing everything.")
        print("2. You see a covered piano sitting in the recpeiton hall, uncover it and show off your piano and singing skills!")
        print("3. You decide to restring your guitar because you forgot your string winder.")
    
        choice = input("Choose 1,2, or 3: ")
        if choice == "1":
            print("You amaze the bride, groom and other wedding guests. A few months later, the groom hires you to teach him how to play guitar!")
        elif choice == "2":
            print("A wedding guest who is also a musician, is impressed with your multi-instrumental music skills and hires you to play gigs with an 80's cover band.")
        elif choice == "3":
            print ("Trying to rush, and under a lot of pressure, you pop a steel string and it slices your neck open. You're bleeding heavily and have to leave the wedding to go to the emergency room to get stiches. You lose out on money from the gig and you can't play until your neck is healed.")
        else:
            print("Invalid choice, you end up not getting the wedding gig and need to look for more opportunities to perform.")

    def game():
        playing = True
        while playing:
            print("------------------------------------------------------")
            print("Welcome to the game of Music Careers! Choose wisely!")
            print("1. Private Piano Teacher~")
            print("2. Street Performer~")
            print("3. Music Producer~")
            print("4. High School Band Director~")
            print("5. Touring Musician~")
            print("6. Wedding Singer~")

            door = input ("Hello! Pick a door (#1-6): ")

            if door == "1":
                door1()
            elif door == "2":
                door2()
            elif door == "3":
                door3()
            elif door == "4":
                door4()
            elif door == "5":
                door5()
            elif door == "6":
                door6()
            else:
                print ("Door choice invalid.")

            playagain = input("Do you want to play again? (yes or no)?")
            if playagain == "no":
                playing = False
                print("Thank you for playing, this is the end of the game!")
                print("======================================================")

    game()



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


