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
counter = 10
exit = 1

A2 = False

for letter in word:
    L.append(letter)
    L2.append("_")

print "Welcome to Hangman! Type 0 to exit."
print "I am thinking of a word " +str(len(word)) + " letters long."
print L2
print word


while counter > 0 and exit == 1:
    Answer = False
    print "------------------"
    print "Guesses: " + str(counter)
    print "Available letters: " + var
    user_guess = raw_input("Please enter a letter: ")

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
            counter = counter + 1




    if user_guess == "0":
        exit = exit - 1
    elif Answer == False:
        print "YOU'RE WRONG!"
        counter = counter - 1
    else:
        print "Nice, you got a letter!"
        c2 = 0
        for letter in L:
            on = "_"
            nn = user_guess
            if letter == nn:
                L2[c2] = nn
            c2 = c2 + 1
    print L2





