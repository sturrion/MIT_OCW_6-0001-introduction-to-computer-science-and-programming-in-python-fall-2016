# Problem Set 2, hangman.py
# Name: Silvia Turrion
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word = guessed_word + letter
        else:
            guessed_word = guessed_word + '_ '
    
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters = available_letters + letter
    
    return available_letters
    

def get_unique_letters(secret_word):
    '''
    secret_word: string, the word the user is guessing
    returns: number of unique letters in secret_word.
    '''
    letters = []
    for letter in secret_word:
        if letter not in letters:
            letters.append(letter)
            
    return len(letters)
    


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    
    message = ""
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings_remaining, "warnings left.")

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("-" * 13)
        print("You have", guesses_remaining, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
    
        guess = input("Please guess a letter: ")
        
        if not str.isalpha(guess):
            message = "Oops! That is not a valid letter."
            if warnings_remaining > 0:
                warnings_remaining -= 1
                message = message + " " + "You have " + str(warnings_remaining) + " warnings left:"
            else:
                guesses_remaining -= 1
                message = message + " " + "You have no warnings left so you lose one guess:"
        else:
            guess = str.lower(guess)
            
            if guess in letters_guessed:
                message = "Oops! You've already guessed that letter."
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    message = message + " " + "You have " + str(warnings_remaining) + " warnings left:"
                else:
                    guesses_remaining -= 1
                    message = message + " " + "You have no warnings left so you lose one guess:"
            else:
                letters_guessed.append(guess)
                if guess in secret_word:
                    message = "Good guess:"
                else:
                    if guess in ('a','e','i','o','u'):
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
                    message = "Oops! That letter is not in my word:" 
                     
        print(message, get_guessed_word(secret_word, letters_guessed))
    
    print("-" * 13)
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        total_score = guesses_remaining * get_unique_letters(secret_word)
        print("Your total score for this game is:", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was else.")
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ','')
    other_word = other_word.replace(' ','')
    
    if len(my_word) != len(other_word):
        return False
    
    my_word_list = list(my_word)
    other_word_list = list(other_word)
    
    i = 0
    for letter in my_word_list:
        if letter != '_':
            if my_word_list.count(letter) != other_word_list.count(letter):
                return False
            if letter != other_word_list[i]:
                return False
        i += 1
    
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = False
    match_list = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            match_list.append(word)
            matches = True
    
    if matches:
        print("Possible word matches are:")
        print(' '.join(match_list))
    else:
        print("No matches found")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    
    message = ""
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings_remaining, "warnings left.")

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("-" * 13)
        print("You have", guesses_remaining, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
    
        guess = input("Please guess a letter: ")
        
        if guess == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
            if not str.isalpha(guess):
                message = "Oops! That is not a valid letter."
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    message = message + " " + "You have " + str(warnings_remaining) + " warnings left:"
                else:
                    guesses_remaining -= 1
                    message = message + " " + "You have no warnings left so you lose one guess:"
            else:
                guess = str.lower(guess)
                
                if guess in letters_guessed:
                    message = "Oops! You've already guessed that letter."
                    if warnings_remaining > 0:
                        warnings_remaining -= 1
                        message = message + " " + "You have " + str(warnings_remaining) + " warnings left:"
                    else:
                        guesses_remaining -= 1
                        message = message + " " + "You have no warnings left so you lose one guess:"
                else:
                    letters_guessed.append(guess)
                    if guess in secret_word:
                        message = "Good guess:"
                    else:
                        if guess in ('a','e','i','o','u'):
                            guesses_remaining -= 2
                        else:
                            guesses_remaining -= 1
                        message = "Oops! That letter is not in my word:" 
                         
            print(message, get_guessed_word(secret_word, letters_guessed))
    
    print("-" * 13)
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        total_score = guesses_remaining * get_unique_letters(secret_word)
        print("Your total score for this game is:", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was else.")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
