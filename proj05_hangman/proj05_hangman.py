# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

word = choose_word(wordlist)

L = []
L2 = []
var = string.lowercase
counter = 6
game = 1
Answer = False
index =

for letter in word:
    L.append(letter)
    L2.append("_")

print "Welcome to Hangman!"
print "I am thinking of a word " +str(len(word)) + " letters long."
print L2

L2[index] = "user_guess"

while game:
    print "------------------"
    print "Guesses: " + str(counter)
    print "Available letters: " + var
    user_guess = raw_input("Please enter a letter: ")
    counter = counter - 1
    for letter in word:
        if user_guess == letter:
            var = var.replace(user_guess, "")
            #print L2
            Answer = True
        elif user_guess != letter:
            var = var.replace(user_guess, "")
            #print "YOU'RE WRONG!"
            #print L2

        else:
            game = game - 1

    if Answer == False:
        print "YOU'RE WRONG!"
    else:
        print "Nice, you got a letter!"





