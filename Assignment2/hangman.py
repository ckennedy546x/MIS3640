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
    underscore = ['_ '] * len(secretWord) #sets a variable that will create the same amount of underscores as the length of the secretWord. This will create a list of underscores with the amount of underscores equalling the length of the secretWord word

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

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #creates a variable that is a list containing every letter in the alphabet
    alphabet2 = alphabet[:] #creates a variable that is a copy of alphabet

    def removeDupsBetter(L1, L2): #Creates a function within the getAvailableLetters with arguments of L1 and L2 which will be will be equated to our lettersGuessed and our copied alphabet list
        L1Start = L1[:] #creates a variable which creates a copy of L1
        for m in L1: #starts a for loop that will run through each element within the L1 list which will be set as lettersGuessed
            if m in L1Start: #if the element in the specific loop is in the copy of L1 (L1Start)
                L2.remove(m) #then the element or letter will be removed from L2, which will later be set as the copied alphabet list 
        return ''.join(str(m) for m in L2) #after the loop is completed, the updated list (L2) will be returned 

    return removeDupsBetter(lettersGuessed, alphabet2) #Once the getAvailableLetters function is run, this will run the function within it (removeDupsBetter).  It sets L1 as lettersGuesses and L2 as the alphabet2 (the copied alphabet list)


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

    intro = str(len(secretWord)) #Sets variable equal to length of secretWord
    lettersGuessed = [] #creates a variable that is an empty list
    guess = str #makes an inputted guess a string
    mistakesMade = 8 #Sets the amount of allowed mistakes to 8.  After each wrong guess, 1 will be subtracted from this number.
    wordGuessed = False #sets variable that is equal to false to start
    
    print('Welcome to the game, Hangman!') #prints phrase when game begins
    print(('I am thinking of a word that is ') + intro + (' letters long.')) #prints phrase "I am thinking of a word that is (length of the secret word) letters long"
    print(('------------')) #prints a line to seperate opening phrase

    while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False: #the while statement will continue to run if the amount of wrong guesses is higher than 0, less than or equal to 8, and if the word hasn't been fully guessed yet
        if secretWord == getGuessedWord(secretWord, lettersGuessed): #if the secretWord word is equal to the word that was generated from the getGuessedWord funtion, then wordGuessed variable is changed to true now and the while statement is stopped and "Congratulations, you won" is printed
            wordGuessed = True
            break
        print(('You have ') + str(mistakesMade) + (' guesses left.')) # if the full word hasn't been guessed, the game will tell you how many guesses you have left 
        print(('Available letters: ') + getAvailableLetters(lettersGuessed))#the game will also tell you how many letters are left which will draw upon the getAvailableLetters function
        guess = input(('Please guess a letter: ').lower())#the game will then ask you for another letter to be guessed and will convert it to lowercase
        if guess in secretWord:#if the inputted guess is in fact in secretWord...
            if guess in lettersGuessed: #AND if the letter has already been guessed, found from the created list, the game will tell you that you have already guessed letter and will tell you the current updated word at the current point
                print(("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed))
                print('------------')
            else: #AND if it hasn't been guessed the current state of your guessed word will add the letter to your GuessedWord and the lettersGuessed will take out the letter you just guessed
                lettersGuessed.append(guess)
                print(('Good guess: ') + getGuessedWord(secretWord, lettersGuessed))
                print(('------------'))
        else: #if the letter is not in SecretWord...
            if guess in lettersGuessed:#AND your letter was already guessed, found from the created list, the game will tell you that you have already guessed letter and will tell you the current updated word at the current point
                print(("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed))
                print('------------')
            else:#AND if the letter hasn't been guessed yet your amount of tries left (mistakesMade) will decrease by 1 and the game will tell you that it is not in the secretWord and will remind you of your updated word from the getGuessedWord function
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print(('Oops! That letter is not in my word: ') + getGuessedWord(secretWord, lettersGuessed))
                print('------------')

    if wordGuessed == True: #If your word that you've created equals the secretWord word, the game will tell you that you won
        return 'Congratulations, you won!'
    elif mistakesMade == 0: #if you guess incorrectly 8 times before finding out the whole word, you lose and the game will tell you that you ran out of guesses and will then tell you what the secretWord was
        print(('Sorry, you ran out of guesses. The word was ') + secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower() #this will randomly choose a word from the word.txt file and make sure it is lowercase
print(hangman(secretWord)) #Once this function is called upon it will run the hangman function and begin the game using the secretWord as the argument or word to be guessed

