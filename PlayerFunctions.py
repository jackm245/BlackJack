#imports
from cards import SuitList, ListOfValaues, AlreadyPickedCards
from colorama import Fore as F
from random import choice
import sys
from replit import clear
import time


#declares player score
PlayerScore = []
PlayerBust = False#decalres if player is bust


def player_face_value_changer(Number):#changes face  value to number
  if Number == "Jack" or Number == "Queen" or Number == "King":#if picture card, change numerical value to 10
    Number = 10
  if Number == "Ace":#ask if ace is high or low
    while 1:
      #makes usre that they enter either 1 or 11
      Option = input("Do you want this to be 1 or 11?: ")
      if not Option.isdigit():
        print("You must enter a number")
      elif int(Option) != 1 and int(Option) !=11:
        print("You must enter 1 or 11")
        #sets ace to high or low, depending on input
      elif int(Option) == 1:
        Number = 1
        break
      else:
        Number =  11
        break
  #checks if the player has gone bust
  player_check_if_bust(int(Number))


def player_check_if_bust(Number):
  from time import sleep
  global PlayerScore
  global PlayerBust
  PlayerScore.append(Number)
  TotalPlayerScore = sum(PlayerScore)
  #prints their score
  print(F.WHITE + "score: "+str(TotalPlayerScore))
  #cheks if they are bust
  if TotalPlayerScore >21:
    sleep(3)
    clear()
    sys.exit(F.RED + "You got {}".format(TotalPlayerScore)+"\n"+F.RED+"You are bust!")


def ask_if_twist():
  #runs while player is not bust
  while not PlayerBust:
    option = input(F.WHITE + "Do you want to twist? (Y/N): ").lower()
    #checks if what they entered is correct
    if not option.isalpha():
      print(F.RED + "You must enter y / n")
    elif option != "y" and option != "n":
      print(F.RED + "You must enter y / n")
    elif option == "y":
      #gets them another card if they choose to twist
      player_new_card(choice(list(ListOfValaues)), choice(SuitList).title())
    else:
      #if they stick, then their turn is over
      print(F.RED + "Your turn is over")
      break


def player_check_card_valid(Card, Number, Suit):
  if Card not in AlreadyPickedCards:#if the card has not already been picked, then carry on with the program
      return(F.BLUE + "Your card is the {} Of {}!".format(F.GREEN+Number,F.GREEN+Suit))
      AlreadyPickedCards.append(Card)
  else:
    #if the card has already been picked, then get a new card instead
    player_new_card(choice(list(ListOfValaues)), choice(SuitList).title())


def player_check_if_blackjack(PlayerScore):#checks if the player has blackjack
  if PlayerScore[0] == 10 and PlayerScore[1] == 11:
    time.sleep(1)
    clear()
    sys.exit(F.GREEN + "BlackJack, You win")
  elif PlayerScore[1] == 10 and PlayerScore[0] == 11:
    time.sleep(1)
    clear()
    sys.exit(F.GREEN + "BlackJack, You win")

def player_check_if_five_card_trick(PlayerScore):#checks if player has a five card trick
  if len(PlayerScore) == 5:
    time.sleep(1)
    clear()
    sys.exit(F.GREEN + "Five card Trick! \n You win!")

def player_new_card(Number, Suit):
  #uses the randomly created number and suit to create a card
  Card = Number + Suit
  #checks if the card us already used
  print(player_check_card_valid(Card, Number, Suit))
  #changes face value to number
  player_face_value_changer(Number)
