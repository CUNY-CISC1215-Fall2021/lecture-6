# This file implements a guessing game
# The game will ask you repeatedly to guess a number between 0 and 10,
# and will give you clues if you get it wrong

import random

def rand_game():
    rand_num = random.randrange(10)

    guessed = False
    counter = 0         # Keep track of the number of guesses

    while not guessed:
        guess = int(input("Guess a number: "))
        if guess == rand_num:
            print("Right!")
            guessed = True
        elif guess < rand_num:
            print("Too small")
        else:
            print("Too big")
        counter = counter + 1

    print("It took you " + str(counter) + " guesses")

rand_game()

