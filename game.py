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
    first_decision_results = []
    first_decision_results.append("You woke up late again! This was the last straw. You got fired from work. Restart the game.")
    first_decision_results.append("You brush your teeth, shower, and get dressed. Time to go to work!")
    first_decision_results.append("Oops, it turns out that you don't have sick days left. Restart the game.")
    second_decision_results = []
    second_decision_results.append("It took too long to ride to work and you were late again! You got fired. Restart the game.")
    second_decision_results.append("There is an ongoing strike and the bus got delayed. You got fired from work for being late. Restart the game.")
    second_decision_results.append("You got to work just on time!")
    third_decision_results = []
    third_decision_results.append("You got to your classroom right before the bell rang!")
    third_decision_results.append("The copy machine jammed, and caused you go be late. You got fired. Restart the game.")
    third_decision_results.append("Your coworker spent too much time talking and now you're late and got fired. Restart the game.")
    fourth_decision_results = []
    fourth_decision_results.append("Later, one of your students' parents filed a complaint. You got fired. Restart the game.")
    fourth_decision_results.append("Unfortunately, an administrator decided to evaluate your lesson today. You got fired. Restart.")
    fourth_decision_results.append("The lesson went fine though could have been better.")
    fifth_decision_results = []
    fifth_decision_results.append("It's a little awkward buying lunch with the students but you're not hungry anymore.")
    fifth_decision_results.append("You didn't make it back on time. You got fired. Restart the game.")
    fifth_decision_results.append("You got too hungry to teach effectively during an important evaluation. You got fired. Restart.")

    time.sleep(1)
    print()
    print("Survive a Day of Work!")
    time.sleep(1)
    def main_menu():
        print()
        name = input("Please enter your name: ")
        time.sleep(0.5)
        print()
        print("Hello", name, "it's morning and you have just woken up. What do you do?")
        time.sleep(1)
        print("1. Press the snooze button on your alarm")
        time.sleep(0.3)
        print("2. Get ready to go to work")
        time.sleep(0.3)
        print("3. Call in sick")
        time.sleep(0.5)
        return name

    def hint():
        choice = ""
        while choice != "yes" and choice != "no":
            choice = input("Would you like a hint? yes/no: ")
            time.sleep(0.3)
            if choice == "yes":
                time.sleep(0.5)
                print("Choose the answer that would most likely get you through the work day.")
                time.sleep(1)
            elif choice != "no":
                time.sleep(0.5)
                print("You must answer with yes or no")
                time.sleep(0.5)

    def first_decision():
        choice = int(input("What do you choose? "))
        time.sleep(0.5)
        if choice == 1:
            print(first_decision_results[0])
            time.sleep(0.5)
            return "restart"
        elif choice == 2:
            print(first_decision_results[1])
            time.sleep(0.5)
            return "continue"
        elif choice == 3:
            print(first_decision_results[2])
            time.sleep(0.5)
            return "restart"

    def second_decision(name):
        print()
        print("How will you go to work today,", name)
        time.sleep(0.5)
        print("1. Ride your bike to work")
        time.sleep(0.3)
        print("2. Take the bus to work")
        time.sleep(0.3)
        print("3. Drive to work")
        time.sleep(0.5)
        choice = int(input("What do you choose? "))
        time.sleep(0.5)
        if choice == 1:
            print(second_decision_results[0])
            time.sleep(0.5)
            return "restart"
        elif choice == 2:
            print(second_decision_results[1])
            time.sleep(0.5)
            return "restart"
        elif choice == 3:
            print(second_decision_results[2])
            time.sleep(0.5)
            return "continue"

    def third_decision(name):
        print()
        print("You are now at work. What do you do next,", name)
        time.sleep(0.5)
        print("1. Go to your classroom")
        time.sleep(0.3)
        print("2. Go make copies")
        time.sleep(0.3)
        print("3. Chat with a coworker")
        time.sleep(0.5)
        choice = int(input("What do you choose? "))
        time.sleep(0.5)
        if choice == 1:
            print(third_decision_results[0])
            time.sleep(0.5)
            return "continue"
        elif choice == 2:
            print(third_decision_results[1])
            time.sleep(0.5)
            return "restart"
        elif choice == 3:
            print(third_decision_results[2])
            time.sleep(0.5)
            return "restart"

    def fourth_decision():
        print()
        print("You are now in your classroom, and you realize you forgot to plan for today's lessons. What do you do?")
        time.sleep(0.5)
        print("1. Play a movie and give the students a free day")
        time.sleep(0.3)
        print("2. Make up a lesson on the spot")
        time.sleep(0.3)
        print("3. Use last year's lesson")
        time.sleep(0.5)
        choice = int(input("What do you choose? "))
        time.sleep(0.5)
        if choice == 1:
            print(fourth_decision_results[0])
            time.sleep(0.5)
            return "restart"
        elif choice == 2:
            print(fourth_decision_results[1])
            time.sleep(0.5)
            return "restart"
        elif choice == 3:
            print(fourth_decision_results[2])
            time.sleep(0.5)
            return "continue"

    def fifth_decision(name):
        print()
        print("It is now lunchtime, and you realized you forgot to bring your lunch. What do you do next,", name)
        time.sleep(0.5)
        print("1. Buy lunch from the cafeteria")
        time.sleep(0.3)
        print("2. Drive to Chipotle to buy some food")
        time.sleep(0.3)
        print("3. Decide to not eat anything and try to make it to the end of the day")
        time.sleep(0.5)
        choice = int(input("What do you choose? "))
        time.sleep(0.5)
        if choice == 1:
            print(fifth_decision_results[0])
            time.sleep(0.5)
            return "continue"
        elif choice == 2:
            print(fifth_decision_results[1])
            time.sleep(0.5)
            return "restart"
        elif choice == 3:
            print(fifth_decision_results[2])
            time.sleep(0.5)
            return "restart"

    def ending(name):
        time.sleep(1)
        for i in range(10):
            if i%2 == 0:
                print("               CONGRATULATIONS")
            else:
                print()
            time.sleep(0.2)
        time.sleep(0.5)
        print(name, "you made it through the day without getting fired! You won the game!")
        for i in range(10):
            if i%2 == 0:
                print()
            else:
                print("               CONGRATULATIONS")
            time.sleep(0.2)

    play_again = "yes"
    while play_again == "yes":
        name = main_menu()
        hint()
        first_result = first_decision()
        if first_result != "restart":
            second_result = second_decision(name)
            if second_result != "restart":
                third_result = third_decision(name)
                if third_result != "restart":
                    fourth_result = fourth_decision()
                    if fourth_result != "restart":
                        fifth_result = fifth_decision(name)
                        if fifth_result != "restart":
                            ending(name)

        play_again = input("Would you like to play again? ")    

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


