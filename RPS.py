#RPS.py
#Name: Jenna Kramer
#Date: 02/08/26
#Assignment:Lab 3
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  again = "Y"
  while again == "Y": 
    #User can play as many games as they wish.
    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice(["R", "P", "S"])

    #Prompt the user for their RPS selection
    player = input("Pick your weapon (R, P, S):")

    #Determine winner and state what happened to the user
    if computer == "R":
      print("Computer chose Rock")
    elif computer == "P":
      print("Computer chose Paper")
    else:
      print("Computer chose Scissors")
    
    if player == "R":
      print("Player chose Rock")
    elif player == "P":
      print("Player chose Paper")
    else:
      print("Player chose Scissors")

    if player == "R" and computer == "R":
      print("Tie")
      ties = ties + 1
    if player == "R" and computer == "P":
      print("Computer wins.")
      losses = losses + 1
    if player == "R" and computer == "S":
      print("You win!")
      wins = wins + 1 

    if player == "S" and computer == "S":
      print("Tie")
      ties = ties + 1
    if player == "S" and computer == "R":
      print("Computer wins.")
      losses = losses + 1
    if player == "S" and computer == "P":
      print("You win!")
      wins = wins + 1 

    if player == "P" and computer == "P":
      print("Tie")
      ties = ties + 1
    if player == "P" and computer == "S":
      print("Computer wins.")
      losses = losses + 1
    if player == "P" and computer == "R":
      print("You win!")
      wins = wins + 1 

    #Ask the user if they would like to play again.
    again = input("Do you want to play again? (Y or N)")
    #if again == "Y"
    #elif again == "N":

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
