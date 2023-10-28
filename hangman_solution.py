# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import re

WORDLIST_FILENAME = '.\words.txt'


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

# print(type(load_words())) 


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
secret_word = choose_word(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    lista = [x.lower() for x in letters_guessed ]
    for i in secret_word.lower():
        if i not in lista:
            return False
    return True
# print(is_word_guessed('apple',['l','f','p','e','a']))   

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    lista = [x.lower() for x in letters_guessed ]
    word_lista = ['_ ' for x in secret_word]
    for letter in secret_word.lower():
          if letter in lista:
              #per avere gli indici di ogni lettera
              #index of every letter in secret_word
              letter_index= [m.start() for m in re.finditer(letter, secret_word.lower())]
              for ind in letter_index:
                word_lista[ind] = letter                     
    return ''.join(word_lista)        
#print(get_guessed_word('aPPle',['l','f','p','e']))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = string.ascii_lowercase
    for i in letters_guessed:
        available_letters = available_letters.replace(i,'')
    return available_letters            
#print(get_available_letters(['a', 't','z']))


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
    print(f'''The secret word length is {len(secret_word)}. You have 6 guesses.\n 
          You lose respectively 1 and 2 guess(es) for every inputed consonant/vowel not in secret word.
          If you enter for three times a character different from a letter or a letter that has been guessed
          you lose a guess.''')  
    # Everytime you insert a consonant that is not contained in the secret word you lose 
    # a guess, instead you lose 2 guessed in case of a vowel.   
    guess = ''
    guessedLetters = []
    nr_guess = 6
    warning = 3
    vowels = ('a','e','i','o','u') 
    consonants = [x for x in string.ascii_lowercase if x not in vowels]

    while nr_guess > 0  :
        print('---------------------------------------------------------------') 
        print(get_guessed_word(secret_word, guessedLetters))
        print('The available letters are:')
        print(get_available_letters(guessedLetters))
        print('You have ', nr_guess, 'guess(es) left!')

        guess = input('Input a letter!\n').lower()
            
        if guess not in secret_word:
            print(f'The letter \'{guess}\'is not in the secret word.')
        
        if guess not in string.ascii_lowercase or guess in guessedLetters:
            nr_guess 
            warning -=1
            print('The guess is not a letter or it has been already guessed: You have', warning, 'warning(s)')
            if warning == 0:
                nr_guess -=1
                print('''You have inputed for three times a character different from a letter or 
                         that has been guessed, you lose a guess.You have 0 warnings, you lost 1 guess.\n 
                         You have ', nr_guess,'guess(es)!''')
   
        if guess in guessedLetters or guess in secret_word:
            nr_guess
        elif guess in vowels and guess not in secret_word:
            nr_guess-= 2
        elif guess in consonants and guess not in secret_word:
              nr_guess -= 1 
        else:
            nr_guess 
        
        if guess.lower() in string.ascii_lowercase:
          guessedLetters += [guess]    
        print('The guessed characters are:',guessedLetters)
        word = get_guessed_word(secret_word, guessedLetters)

        if word == secret_word :
            print(f'You guessed the secret word!: "{secret_word}". Congratulations!')
            break
        elif nr_guess == 0 :
          print(f'You didn\'t guess the secret word: {secret_word}. GAME OVER!' )
  
        
   
    return secret_word 

# to test the code
# hangman('hellow')
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
    my_word = my_word.split() # to obtain the length of the my_word (spaces excluded)
    my_word = ''.join(my_word)  
    print(len(my_word))
    if len(my_word) == len(other_word):
        if len(my_word) == len(other_word):
          lista = []
          for i in range(len(my_word)): 
            #to catch this case -- print(match_with_gaps('ap_ le', 'apple'))
            if other_word[i].lower() == other_word[i-1].lower()  and \
                my_word[i-1].lower() == other_word[i-1].lower() and \
                my_word[i] == '_':
                lista += [False]
            #to catch this case --  print(match_with_gaps('a_ ple', 'apple'))  
            elif i < (len(my_word)-1) and my_word[i] == '_' and  my_word[i+1].lower() == other_word[i+1].lower() \
             and other_word[i].lower() == other_word[i+1].lower():
                lista += [False]  
            elif (my_word[i].lower() == other_word[i].lower() or my_word[i] == '_'):
              lista += [True] 
            else:
                lista += [False]
    if len(lista)!=0 and all(lista):
            return True
    else:
        return False  
# print(match_with_gaps('app_ e ', 'apple')) # --> True
# print(match_with_gaps('ap_ le ', 'apple')) # --> False


def guessed_letters(guess):
  ##it returns the guessed letters
  guessed_letters = []
  guessed_letters += [guess]
  return guessed_letters
#print(guessed_letters('a'))


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word = my_word.split() 
    my_word = ''.join(my_word) 
    index_guessed_letters = []
    guessed_characters = [] 
    missing_letters_index = []
    for i in range(len(my_word)):
        if my_word[i] != '_':
          index_guessed_letters.append(i) 
          if my_word[i] not in guessed_characters:
            guessed_characters.append(my_word[i])
        else:
            missing_letters_index.append(i)
  
    #To obtain the list of words that can be a match with my_word
    #It returns the words that has the same length of my_word and the first letter guessed is the same
    potential_list = [potenzial_word for potenzial_word in wordlist if len(my_word) == len(potenzial_word) and my_word[index_guessed_letters[0]] == potenzial_word[index_guessed_letters[0]]]
    matching_words = []

    #To obtain the matching words (in words.txt) with my_word
    for word in potential_list:
        matching_index = []
        for index_ in index_guessed_letters:
            if word[index_] == my_word[index_]:
                matching_index += [True]
            else:  
                break                   
        if len(matching_index)==len(index_guessed_letters):
            unguessed_lett_ind = [] #unguessed letters index
            for k in missing_letters_index:
                if word[k] in guessed_characters:
                    break
                elif word[k] not in guessed_characters:
                    unguessed_lett_ind += [True]
            if all(unguessed_lett_ind) and len(unguessed_lett_ind)==len(missing_letters_index):        
              matching_words += [word]                
    print('The matching words are: ', matching_words)  
#print(show_possible_matches('_ or_ '))   


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
    print(f'''The secret word length is {len(secret_word)}. You have 6 guesses.\n 
          You lose respectively 1 and 2 guess(es) for every inputed consonant/vowel not in secret word.
          If you enter for three times a character different from a letter or a letter that has been guessed
          you lose a guess.''')   

    # Everytime you insert a consonant that is not contained in the secret word you lose 
    # a guess, instead you lose 2 guessed in case of a vowel.    
    guess = ''
    guessedLetters = []
    nr_guess = 6
    warning = 3
    vowels = ('a','e','i','o','u')
    consonants = [x for x in string.ascii_lowercase if x not in vowels]

    while nr_guess > 0  : 
      
      print(get_guessed_word(secret_word, guessedLetters))
      print('The available letters are:')
      print(get_available_letters(guessedLetters))
      print('You have ', nr_guess, 'guess(es) left!')

      guess = input('Input a letter. If you input \'*\' you get some hints about the secret words!\n').lower()
      print('---------------------------------------------------------------') 
      if guess == '*':
          show_possible_matches(word)

      if guess not in secret_word:
          print(f'The letter \'{guess}\' is not in the secret word.') 

      if guess == '*':
          nr_guess
          warning 
      elif (guess not in string.ascii_lowercase) or (guess in guessedLetters) :
          nr_guess
          warning -=1
          print('The guess is not a letter or it has been already guessed: You have', warning, 'warning(s).')
          if warning == 0:
              nr_guess -=1
              print('''You have inputed for three times a character different from a letter or 
                       that has been guessed, you lose a guess.You have 0 warnings, you lost 1 guess.\n 
                       You have ', nr_guess,'guess(es)!''')
   
      if guess in guessedLetters or guess in secret_word:
          nr_guess
      elif guess in vowels and guess not in secret_word:
          nr_guess-= 2
      elif guess in consonants and guess not in secret_word:
            nr_guess -= 1 
      else:
          nr_guess 

      if guess.lower() in string.ascii_lowercase:
        guessedLetters += [guess]    
       
      print('The guessed characters are:',guessedLetters)
      word = get_guessed_word(secret_word, guessedLetters)

      if word == secret_word :
          print(f'You guessed the secret word!: "{secret_word}". Congratulations!')
          break
      elif nr_guess == 0 :
        print(f'You didn\'t guess the secret word: "{secret_word}". GAME OVER!')
      print('---------------------------------------------------------------') 
    return secret_word 

# print(hangman_with_hints('hello'))
# exit()

if __name__ == "__main__":
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
   
