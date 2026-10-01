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
   # def room15():
    #room15
    #Jitender Rajpoot
    print("Good choice. You've avoided drowning in the previous room.")
    userName = input("Enter your name: ")

    def play_game():

      print("Hi ", userName, ", welcome to 'Final Destination'--an interactive experience in which you navigate death, I mean, navigate your way to the moon and back to Earth. Safe journey!")
      points = 0        #new feature keep score for correct decisions
      #decision 1
      print("Choose your spacecraft:")

      spacecraft = ["Space Shuttle", "Solar Shuttle", "Prototype Shuttle"]    #list feature
      index = 0
      for item in spacecraft:               #loop to print list items with their index+1
        index = index+1
        print(index, item)

      choice1 = input("Enter 1, 2, or 3: ")

      if choice1 == "1":
        print("Sorry, rocket fuel prices are unaffordable. This shuttle can't fly to the moon. Flooding from the main room blocks your exit, so you can't escape and drown to deaty, Sorry, Game over!")
      elif choice1 == "2":
        points = points + 10            #add points for correct decision
        print("Great choice! Sun's fusion will power you to the moon. Points: ", points)
        #Decision 2
        print("Choose your flight path:")

        flightPath = ["Lunar Orbit", "Fly to Moon and back", "Land on Moon"]
        index = 0
        for item in flightPath:
          index = index + 1
          print(index, item)

        choice2 = input("Enter 1, 2, or 3: ")

        if choice2 == "1":
          print("The shuttle remains in an infinite loop rotating around the moon. Sorry, you die due to dehydration after 88 days. Game over!")
        elif choice2 == "2":
          print("You returned back to Earth but never stepped on the Moon.")
          print("Although you technically saw the Moon from close range, you return to Room 15, which is flooded. You valiantly struggle but succumb to a drowning death after 33 minutes. Sorry, Game over!")
        elif choice2 == "3":
          points = points + 20
          print("Well done! You made it to the Moon. Now let's explore, but first let's nourish your body. Points: ", points)
          #Decision 3
          print("What do you want to eat?")

          nourishment = ["High energy food", "Freeze dried meal", "Canned tuna and peppers with aioli"]
          index = 0
          for item in nourishment:
            index = index + 1
            print(index, item)

          choice3 = input("Enter 1, 2, or 3: ")

          if choice3 == "1":
            print("This food has too many calories. Unfortunately your heart can't handle your low blood pressure but high blood glucose levels.")
            print("Your heart decides to give up rather than continue the torture. Sorry, you die. Game over!")
          elif choice3 =="2":
            points = points + 30
            print("These items have an unsavory flavor and undesirable texture but exactly what your body needs. Points: ", points)
            #Decision 4
            print("Now let's find an activity to do. What would you like?")

            activity = ["Collect Moon Rocks", "Conduct Chemical Experiments", "Take Photographs"]
            index = 0
            for item in activity:
              index = index + 1
              print(index, item)

            choice4 = input("Enter 1, 2, or 3: ")

            if choice4 == "1":
              points = points + 40
              print("This was your best move! You've found rare Moon Diamonds, which will pay for the next 3 generations of your family. Points:", points)
              print("You should head back to Earth and enjoy your wealth. Where do you want to land?")

              landing = ["Ocean landing", "Desert Landing", "Landing Pad"]
              index = 0
              for item in landing:
                index = index + 1
                print(index, item)

              choice5 = input("Enter 1, 2, or 3: ")
              if choice5 == "1":
                points = points + 50
                print("You win! Ocean was the safest and least dangerous space to re-enter Earth. Enjoy your Moon Diamonds! Points: ", points)
              elif choice5 == "2":
                print("The ambient temprature above the desert combined with heat from your re-entry velocity disintegrated the shuttle.")
                print("Everything including you and the Moon Diamonds dissolved into the thin air. Sorry, game over!")
              elif choice5 == "3":
                print("The booster engines to decelerate the shuttle in order to land malfunctioned and accelerated instead.")
                print("At the sound of speed, you died alongside a Sonic boom. Sorry, game over!")

            elif choice4 == "2":
              print("Sorry, the gases released from the chemical reactions are poisonous.")
              print("From an allergic reaction, our sweat pores extract every drop of blood from you leaving you dead. Sorry, game over!")
            elif choice4 == "3":
              print("The batteries aren't meant to operate in Moon's extreme temperatures. The camera explodes severing your cranial nerves.")
              print("So you feel no pain, but take 72 hours to take your last breath. Sorry, game over!")

          elif choice3 == "3":
            print("This was the worst choice. All items were infected with botulinum toxin.")
            print("You died a slow suffocating death from paralysis of your lungs. Sorry, game over!")
      elif choice1 == "3":
        print("Sorry, the Prototype wasn't tested properly. It exploded midflight. Sorry, you die. Game over!")


    play_game()

    play_again = input("Do you want to try navigating to the moon and back again? Type 'yes' or 'no': ")

    while play_again == "yes":
      play_game()
      play_again = input("Would you like to try again? ")
    else:
      print("Thanks for trying 'Final Destination.' Safe travels!", userName)

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


