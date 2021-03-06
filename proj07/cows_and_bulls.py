# Create a program that will play the 'cows and bulls' game with the user. The game works
# like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every
# digit that the user guessed correctly in the correct place, they have a 'cow'. For
# every digit the user guessed correctly in the wrong place is a 'bull.' Every time the
# user makes a guess, tell them how many 'cows' and 'bulls' they have. Once the user
# guesses the correct number, the game is over. Keep track of the number of guesses the
# user makes throughout the game and tell the user at the end.
#
# Say the number generated by the computer is 1038. An example interaction could look like
# this:
#
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull

# Until the user guesses the number.


import random
number = str(random.randint(1000,9999)) #random 4 digit number
snake = 1

L = []
L2 = []
cows = 0
bulls = 0


for letter in number:
    L.append(letter)

print "Welcome to Cows and Bulls! Type 0 to exit"

while snake == 1:
    user_guess = raw_input("Enter a 4-digit number or exit.")
    if cows == 4:
        snake = snake - 1
        break
    elif user_guess == "0":
        snake = snake - 1
        break
    cows = 0
    bulls = 0
    counter = 0

    for letter in user_guess:
        L2.append(letter)
    for  x in range(0, 4):
        if L2[x] == L:
            cows = cows + 1
            print "You have " + str(cows) + " cows and " + str(bulls) + " bulls."
            L2[counter] = "&"
            L[counter] = "$"
        counter = counter + 1
    counter = 0
    for letter in L2:
        c2 = 0
        for item in L:
            if letter == item:
                bulls = bulls + 1
                L[c2] = "@"
                break
            c2 = c2 + 1
        counter = counter + 1
    print "You have " + str(cows) + " cows and " + str(bulls) + " bulls."
