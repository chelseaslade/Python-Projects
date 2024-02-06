#Rock Paper Scissors including scoreboard and replay option

from random import randint
import random

#Game options list
t = ["Rock", "Paper", "Scissors"]

#Makes computer select random choice from list
computer = t[randint(0,2)]

#Score keeping
player = 1
computerWin = 0
playerWin = 0

while player == 1:
   #If move results in a tie:
    player = input("Rock, Paper, or Scissors? ").title()
    computer = t[randint(0,2)]
    if player == computer:
        print("Tie!")
        print("Score")
        print("Computer win: ", computerWin)
        print("Player win: ", playerWin)
   
   #If player plays Rock
    elif player == "Rock":
        if computer == "Paper":
            print("Sorry, you lost!" , computer, "covers", player)
            computerWin+=1
            print("Score")
            print("Computer win: ", computerWin)
            print("Player win: ", playerWin)
        else:
            print("You win!", player, "smashes", computer)
            playerWin+=1
            print("Score")
            print("Computer win: ", computerWin)
            print("Player win: ", playerWin)
    
    #If player plays Paper
    elif player == "Paper":
        if computer == "Scissors":
            print("Sorry, you lost!", computer, "cut", player)
            computerWin+=1
            print("Score")
            print("Computer win: ", computerWin)
            print("Player win: ", playerWin)
        else:
            print("You win!", player, "covers", computer)
            playerWin+=1
            print("Score")
            print("Computer win: ", computerWin)
            print("Player win: ", playerWin)
   
   #If player plays Scissors
    elif player == "Scissors":
        if computer == "Rock":
            print("Sorry, you lost!", computer, "smashes", player)
            computerWin+=1
            print("Score")
            print("Computer win: ", computerWin)
            print("Player win: ", playerWin)
        else:
            print("You win!", player, "cut", computer)
            playerWin+=1
            print("Score")
            print("Computer win: ", computerWin)
            print("Player win: ", playerWin)
   
   #If incorrect input
    else:
        print("Invalid, please check your spelling/capitalization!")
    
    #Play again or quit
    print("")
    ch=input("Do you wish to continute? (Y/N)").upper()
    if ch=="Y":
        player = 1
        computer = t[randint(0,2)]

    else:
        break
