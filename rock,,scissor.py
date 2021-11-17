#Created By Archit Deshpande
#imports random
import random

#Initializing all the vaiables in our programs:
user_wins = 0
cpu_wins = 0

#options for the CPU to choose from randomly
options = ("rock", "paper", "scissors")

#The whole loop in which the main program is executed:
while True:
    #the Input in which all the program coomands are inputted By the user
    user_input = input("Type Rock/paper/scissors or q to quit the game and reveal the score: ").lower()
    if user_input == "q":
        print(f"you scored {user_wins} point(s) and computer scored {cpu_wins} point(s)")
        break
    #Generates the random number for the CPU to choose from:
    random_number = random.randint(0, 2)
    #Prints the option that the computer chooses randomly and prints it so that the user understands.
    computer_picked = options[random_number]
    print("Computer picked", computer_picked + ".")
    #All the conditions that the user can input and the program searches for it and then displays the random output
    #Note that If the user inputs something incorrect, the CPU returns a random value but dosen't print the statement and no points are given to anyone
    if user_input == "rock" and computer_picked == "scissors":
        print("YEAHHH!! You got it right and won a point!")
        user_wins =+ 1
        continue
    if user_input == "rock" and computer_picked == "paper":
        print("Oh! You lost and computer got a point!")
        cpu_wins += 1
        continue
    if user_input == "rock" and computer_picked == "rock":
        print("Oh! Both of you got the same answer so no points to anyone!")
        continue
    if user_input == "rock" and computer_picked == "scissors":
        print("YEAHHH!! You got it right and won a point!")
        user_wins =+ 1
        continue
    if user_input == "paper" and computer_picked == "rock":
        print("Yeahhhhh! you got a point!")
        user_wins += 1
        continue
    if user_input == "paper" and computer_picked == "scissors":
        print("Oh! You got it wrong so computer got a point!")
        cpu_wins += 1
        continue
    if user_input == "paper" and computer_picked == "paper":
        print("Oh! No one got a point")
        continue
    if user_input == "scissors" and computer_picked == "paper":
        print("Yeahhh!! YOU got a point!")
        user_wins += 1
        continue
    if user_input == "scissors" and computer_picked == "rock":
        print("Oh! computer got a point!")
        cpu_wins += 1
        continue
    if user_input == "scissors" and computer_picked == "scissors":
        print("Oh! No One got a point!")
        continue