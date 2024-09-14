import random
from random import randint

guess_machine=randint(1,50)
while True:
    guess=int(input("Please guess a number between 1 and 50 "))
    if guess<guess_machine:
        print("Too law!")
    elif guess>guess_machine:
        print("Too high!")
    else:
        print("You find correct number!")

