# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "Assignment2\words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    count = 0  #sets the counter to start from zero
    for i, c in enumerate(secretWord):  #the for loop uses enumerate which allows i to be the index and c to be the value
    	if c in lettersGuessed: #if the the value of the element in lettersGuessed is the same as the value in the element in secretWord, the loop will move to the next element in secret word and start another loop and 1 will be added to the counter 
    		count += 1
    if count == len(secretWord): #if the counter ended up equaling the length of the secretWord word the function will return true 
    	return True
    else:
    	return False #if the counter does not equal the length of the length of the secret word, it means the all the letters in secretWord are not in lettersGuessed, and the function will return false

# When you've completed your function isWordGuessed, uncomment these three lines
# and run this file to test!

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(secretWord, lettersGuessed))

# Expected output:
# False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    count = 0 #sets the counter to start from zero
    underscore = ['_ '] * len(secretWord) #sets a variable that will create the same amount of underscores as the length of the secretWord 

    for i, c in enumerate(secretWord): #the for loop uses enumerate which allows i to be the index and c to be the value
        if c in lettersGuessed: #if the the value of the element (c) in lettersGuessed is the same as the value (c) in the element in secretWord, 1 will be added to the counter 
            count += 1
            underscore.insert(count-1,c) #then (c) will be inserted into the index that is one less than our current counter
            underscore.pop(count) #this will remove the element in the list that is at the index that is equal to our current counter
            if count == len(secretWord): #once our current counter is equal to the length of our secretWord we will return the list that we have created with letters and underscores. If it doesn't equal, then the next loop will be started
                return ''.join(str(s) for s in underscore)
        else: #if the the value of the element (c) in lettersGuessed is not the same as the value (c) in the element in secretWord, 1 will be added to the counter 
            count += 1 
            underscore.insert(count-1,'_') #then '_' will be inserted into the index that is one less than our current counter
            underscore.pop(count) #this will remove the element in the list that is at the index that is equal to our current counter
            if count == len(secretWord): #once our current counter is equal to the length of our secretWord we will return the list that we have created with letters and underscores. If it doesn't equal, then the next loop will be started
                return ''.join(str(s) for s in underscore)


# When you've completed your function getGuessedWord, uncomment these three lines
# and run this file to test!

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))

# Expected output:
# '_ pp_ e'


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Hint: You might consider using string.ascii_lowercase, which
    # is a string comprised of all lowercase letters.

    # FILL IN YOUR CODE HERE...


# When you've completed your function getAvailableLetters, uncomment these two lines
# and run this file to test!

# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))

# Expected output:
# abcdfghjlmnoqtuvwxyz


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

