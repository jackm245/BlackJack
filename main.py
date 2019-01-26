  #===================================================================================================#
#
#   File:   BlackJack
#   Author: Jack Morgan
#   Date:   December 2018
#   Notes:  A game of Blackjack against a CPU
#           Variable Names are in CapWords
#           Functions are seperated_with_underscore
#           (Im trying to start laying out code using a basic form of PEP8)
#           My basic PEP 8 doc:
# https://docs.google.com/document/d/1MFuuD-BcZkngGSRAMMD88nO16lqqvXJ5pE1QsUjsLdA/edit?usp=sharing
#
#===================================================================================================#

#imports
from cards import SuitList, ListOfValaues#from a file that I created. 
from random import choice#allows you to get a random chpoice from a list or other variable
from PlayerFunctions import player_new_card, ask_if_twist, PlayerScore, player_check_if_blackjack, player_check_if_five_card_trick#imports functions from the PlayerFunctions File
from CpuFunctions import cpu_new_card, CpuScore, cpu_check_if_blackjack#imports functions from the CpuFunctions File
from SharedFunctions import scoring#imports the scoring function
from replit import clear#allows you to clear the screen
from time import sleep#allows you to wait
from colorama import Fore as F#allows for pretty colours :)

#main acess point for application
def main():
  clear()
  #gets players 2 original cards
  for i in range(2):
    player_new_card(choice(list(ListOfValaues)), choice(SuitList).title())
  #checks if you have Blackjack
  player_check_if_blackjack(PlayerScore)
  player_check_if_five_card_trick(PlayerScore)
  ask_if_twist() # asks if the player wants to twist
  print(F.RED+"Cpu's Turn")#states that it is no longer your turn
  #deals cpu 2 cards
  for i in range(2):
    cpu_new_card(choice(list(ListOfValaues)), choice(SuitList).title())
  #checks if the cpu has blackjack
  cpu_check_if_blackjack(CpuScore)
  #cpu tries to beat player by getting a higher scor than them
  while sum(CpuScore) < sum(PlayerScore):
    cpu_new_card(choice(list(ListOfValaues)), choice(SuitList).title())
  #prints winner
  sleep(2)#waits for two seconds first
  clear()#clears the screen
  print(scoring(sum(PlayerScore), sum(CpuScore)))#prints if the player wins or loses


if __name__ == '__main__': # runs main if not imported from elsewhere
  main()
