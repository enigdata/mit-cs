# Problem Set 2, hangman.py
# Name: Sili Wang

# Hangman Game
# -----------------------------------
# Helper code

import random
import string

WORDLIST_FILENAME = "words_problem2.txt"


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

    for char in secret_word:
      if char not in letters_guessed:
        return False 

    return True 


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    res = ''
    for char in secret_word:
      if char in letters_guessed:
        res = res + char 
      else:
        res = res + "_"

    return res 


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    all_available_letter = string.ascii_lowercase
    res = ''
    for char in all_available_letter:
      if char not in letters_guessed:
        res = res + char 
    return res 
    
def get_user_input(guesses_remaining):
    """
    print informational statements and query for user input
    """
    global letters_guessed

    print("-----------------------------------")
    print(f"You have {guesses_remaining} guesses left.")
    print(f"Available letters: {get_available_letters(letters_guessed)}")
    print("Please guess a letter: ")
    guess = input()

    return guess 

def is_input_valid(input_):
    """
    determine whether the user's input is valid
    """
    if len(input_) == 1 and input_.isalpha() or input_ == '*':
      return True 
    else:
      return False 

def is_vowel(letter):
    """
    determine whether a letter is vowel
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter in vowels:
      return True 
    else:
      return False

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

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    global letters_guessed

    guesses_remaining = 6 
    warnings_remaining = 3 
    letters_guessed = list()

    while guesses_remaining > 0:

      if is_word_guessed(secret_word, letters_guessed):
        print("------------------------------------")
        print("Congratulations! You won!")
        total_score = guesses_remaining * len(set(list(secret_word)))
        print(f"Your total score for this game is : {total_score}")
        break 
        return 

      guess = get_user_input(guesses_remaining)
      
      if not is_input_valid(guess) and warnings_remaining > 0:
        print(f"Oops! That is not a valid letter. Please enter a single alphabet.")
        print(f"You have {warnings_remaining} warnings left.")
        warnings_remaining -= 1 
        continue

      if not is_input_valid(guess) and warnings_remaining == 0:
        print(f"Please enter a single alphabet.")
        print("You have 0 warnings left.")

        guesses_remaining -= 1
        continue

      if is_input_valid(guess) and guess.lower() in letters_guessed:
        print(f"Oops! You have guessed this before.")
        if warnings_remaining > 0:
          warnings_remaining -= 1
          print(f"You have {warnings_remaining} warnings left.")
        else:
          guesses_remaining -= 1 
        continue

      elif is_input_valid(guess) and guess.lower() not in secret_word:
        letters_guessed.append(guess.lower())
        if is_vowel(guess):
          guesses_remaining -= 2
        else:
          guesses_remaining -= 1

        print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')

      elif is_input_valid(guess) and guess.lower() in secret_word:
        letters_guessed.append(guess.lower())
        print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')

    if not is_word_guessed(secret_word, letters_guessed):
        print("------------------------------------")
        print("Sorry you lost.")
        print(f"The word is : {secret_word}")
        return 


# ----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    if len(my_word.strip()) != len(other_word.strip()):
      return False
    else:
      hidden = list()
      for i in range(len(my_word)):
        if my_word[i].isalpha() and my_word[i] != other_word[i]:
          return False 
        if not my_word[i].isalpha():
          hidden.append(other_word[i])
      for char in hidden:
        if char in my_word:
          return False    

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
    matches = list()
    for word in wordlist:
      if match_with_gaps(my_word, word):
        matches.append(word)

    if len(matches) == 0:
      print("No Matches found")
      return

    else:
      for match in matches:
        print("Possible matches are: ")
        print(match + ' ')
      return 



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
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    global letters_guessed

    guesses_remaining = 6 
    warnings_remaining = 3 
    letters_guessed = list()

    while guesses_remaining > 0:

      if is_word_guessed(secret_word, letters_guessed):
        print("------------------------------------")
        print("Congratulations! You won!")
        total_score = guesses_remaining * len(set(list(secret_word)))
        print(f"Your total score for this game is : {total_score}")
        break 
        return 

      guess = get_user_input(guesses_remaining)

      if guess == '*':
        my_word = get_guessed_word(secret_word, letters_guessed)
        show_possible_matches(my_word)
  
      if not is_input_valid(guess) and warnings_remaining > 0:
        print(f"Oops! That is not a valid letter. Please enter a single alphabet.")
        print(f"You have {warnings_remaining} warnings left.")
        warnings_remaining -= 1 
        continue

      if not is_input_valid(guess) and warnings_remaining == 0:
        print(f"Please enter a single alphabet.")
        print("You have 0 warnings left.")

        guesses_remaining -= 1
        continue

      if is_input_valid(guess) and guess.lower() in letters_guessed:
        print(f"Oops! You have guessed this before.")
        if warnings_remaining > 0:
          warnings_remaining -= 1
          print(f"You have {warnings_remaining} warnings left.")
        else:
          guesses_remaining -= 1 
        continue

      elif is_input_valid(guess) and guess.lower() != '*' and guess.lower() not in secret_word:
        letters_guessed.append(guess.lower())
        if is_vowel(guess):
          guesses_remaining -= 2
        else:
          guesses_remaining -= 1

        print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')

      elif is_input_valid(guess) and guess.lower() in secret_word:
        letters_guessed.append(guess.lower())
        print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')

    if not is_word_guessed(secret_word, letters_guessed):
        print("------------------------------------")
        print("Sorry you lost.")
        print(f"The word is : {secret_word}")
        return 
    

if __name__ == "__main__":

    #secret_word = choose_word(wordlist)
    #secret_word = 'else'
    #hangman(secret_word)

    # print(match_with_gaps('te_t', 'tact'))
    # print(match_with_gaps('a__le', 'banana'))
    # print(match_with_gaps('a__le', 'apple'))
    # print(match_with_gaps('a_ple', 'apple'))

    # show_possible_matches('t__t')
    # show_possible_matches('abbbb_')
    # show_possible_matches('a_pl_')

###############
    
    # To test part 3 
    
    #secret_word = choose_word(wordlist)
    secret_word = 'apple'
    hangman_with_hints(secret_word)
