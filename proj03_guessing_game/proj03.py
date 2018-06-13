# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""


game = 1
counter = 0

import random
num = int(random.randint(1, 9))
while game == 1 and counter < 10:
    ug = int(raw_input("Enter a number, or type 0 to end. "))
    counter = counter + 1
    if ug == 0:
        game = game - 1
    elif ug > num:
        print "You guessed too high!"
    elif ug < num:
        print "You guessed too low!"
    elif ug == num:
        ui = raw_input(("Congrats, you won in ") + str(counter) + (" guess(es)! Would you like to play again? "))
        if ui == "Yes" or ui == "yes" or ui == "yup" or ui == "Yup":
            game = 1
            num = int(random.randint(1, 9))
            counter = 0
        else:
            game = game - 1
    else:
        counter = counter + 0
        print "A number, not a word or letters."
