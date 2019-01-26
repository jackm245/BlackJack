#imports
from cards import SuitList, ListOfValaues, AlreadyPickedCards
from colorama import Fore as F
import sys#allows you to stop the program
from random import choice
from replit import clear
import time

#declares variables
CpuScore = []#a list where the score for the cpu is kept
CpuBust = False# a  variable declaring wether the Cpu is bust



def cpu_face_value_changer(Number):#changes face value of card to numerical value
  global CpuScore
  #changes face value
  if Number == "Jack" or Number == "Queen" or Number == "King":
    Number = 10
  #checks if ace is 1 or 11
  if Number == "Ace":
    #if the score is more than 10, then ace is low
    if sum(CpuScore) > 10:
      Number = 1
    else:
    #if the score is less than 10, then ace is high
      Number = 11
  cpu_check_if_bust(int(Number))#checks if the Cpu is bust


def cpu_check_card_valid(Card, Number, Suit):#check if card already picked
  if Card not in AlreadyPickedCards:#keeps going if card hasnot been chosen before
      return(F.BLUE + "Cpu's card is the {} Of {}!".format(F.GREEN+Number,F.GREEN+Suit))
      #adds to the list of cards so that it can not be picked again
      AlreadyPickedCards.append(Card)
  else: #if card is picked, pick again
    cpu_new_card(choice(list(ListOfValaues)), choice(SuitList).title())


def cpu_check_if_bust(Number):#checks if cpu is bust
  from time import sleep
  global CpuScore
  global CpuBust
  #adds cpu's socre
  CpuScore.append(Number)
  TotalCpuScore = sum(CpuScore)
  #prints their score
  print(F.WHITE + "Cpu's score: "+str(TotalCpuScore))
  #cheks if they are bust
  #if the cpu is bust, the player wins
  if TotalCpuScore >21:
    sleep(3)#waits for 3 seconds, allowing you to see the scores
    clear()
    sys.exit(F.RED + "Cpu is bust!"+"\n"+F.GREEN+"You win")#prints that the player wins and stops the program

    
def cpu_check_if_blackjack(CpuScore):#checks if the Cpu has blackjack
  if CpuScore[0] == 10 and CpuScore[1] == 11:
    time.sleep(1)
    clear()
    sys.exit(F.RED + "BlackJack, CPU wins")
  elif CpuScore[1] == 10 and CpuScore[0] == 11:
    time.sleep(1)
    clear()
    sys.exit(F.RED + "BlackJack, CPU wins")


def cpu_new_card(Number, Suit):
  #The card is made of the number and the suit
  Card = Number + Suit
  print(cpu_check_card_valid(Card, Number, Suit))#checks if the card has been picked before
  cpu_face_value_changer(Number)#changes face values and numericla values
