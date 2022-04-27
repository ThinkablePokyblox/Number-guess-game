#Config
from multiprocessing.connection import wait
import string
import random
HighestNumber = 100
LowestNumber = 0
#Functions
def Startgame():
    print("Please wait while we set your game up!")
    UserLives = 5
    RandomNumber = random.randrange(LowestNumber, HighestNumber)
    while True:
        if UserLives > 0:
            Guess = input("Guess a number!")
            if str.isnumeric(Guess):
                if int(Guess) == RandomNumber:
                    print("Congratulations! You won")
                    break
                elif int(Guess) > RandomNumber:
                    UserLives = UserLives - 1
                    print("The number is lower than " + str(Guess) + ". You have " + str(UserLives) + " lives left!")
                elif int(Guess) < RandomNumber:
                    UserLives = UserLives - 1
                    print("The number is bigger than " + str(Guess) + ". You have " + str(UserLives) + " lived left!")
        else:
            print("You lost all of your lives.. Good luck next time!")
            break
#Main
PlayInput = input("Would you like to play random number guesser? (Yes,No)")
if str.lower(PlayInput) == "yes":
    while True:
        IncorrectArgsProvied = False
        SettingsInputA = ""
        if IncorrectArgsProvied == True:
            SettingsInputA = input("Oops! You failed to provide a number, please try again!")
        else:
            SettingsInputA = input("What should the highest guessable number be? (Number)")
        if str.isnumeric(SettingsInputA):
            HighestNumber = int(SettingsInputA)
            IncorrectArgsProvied = False
            break
        else:
            IncorrectArgsProvied = True
    while True:
        IncorrectArgsProvied = False
        SettingsInputB = ""
        if IncorrectArgsProvied == True:
            SettingsInputB = input("Oops! You failed to provide a number, please try again!")
        else:
            SettingsInputB = input("What should the lowest guessable number be? (Number)")
        if str.isnumeric(SettingsInputB):
            LowestNumber = int(SettingsInputB)
            IncorrectArgsProvied = False
            break
        else:
            IncorrectArgsProvied = True
    Startgame()
else:
    print("Oh well, have a good day!")
    exit()
