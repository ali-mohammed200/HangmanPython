
#####################
#####################
## Version 4 Below ##
#####################
#####################

# Now to add cool ASCHII art

# Include random words with https://pypi.org/project/Random-Word/ package
# and only inputting one character error
# Fixed typing the same letter for every guess error

#Importing the regex library to switch out all letters for blank spaces that look like this [_]
import re
from random_word import RandomWords
r = RandomWords()

# Return a single random word
rw = r.get_random_word()
print(rw)


print("Welcome to Hangman!")
word = rw.lower()
original = word # This is a copy of the word
count = len(word) #This is the length of characters in the word
tries = 6 # We only have 6 tries to guess the word

# This is where we replace each letter for empty spaces that look like this [_]
# re is the regex library
# .sub is the substition method that works with regex
# \S is a regex command that chooses everything other than a white space character
# Check this for more info: https://docs.python.org/3/library/re.html
# the next argument is what I want to replace with
# the last argument is the string that I am doing all this on.
ourGuess = re.sub("\S", "[_]", word) #anonymous -> [_][_][_][_][_][_][_][_][_]
print(ourGuess)

print("The word is " + str(count) + " letters long.")

letterBank = "" # A bank of every correctly guessed letter
incorrectLetters = ""

while count != 0 and tries > 0:
  print("\n")  
  guess = input("Guess a letter: ")[0] #taking the first character inputted
  occurence = word.count(guess) # counting how many times the letter we guessed occurs in the word

  if occurence != 0 and letterBank.count(guess) == 0:
    print("Yes, you guessed correctly!")
    letterBank += guess

    print("Letter bank: [" + letterBank + "] Incorrect letters: [" + incorrectLetters + "]")
    ourGuess = word.replace(guess, "0") # Takes the guessed letter and replaces it with 0 in the actual word

    #print("OurGuess :" + ourGuess) # the actual word with 0s
    regeSub = "[^0" + letterBank + "]" # the regex sub string we want to match including our letterbank
    ourGuess = re.sub(regeSub, "[_]", ourGuess) # We replace anything other than 0's and correctly guessed letters with [_]
    #print("OurGuess :" + ourGuess)
    ourGuess = re.sub("0", guess, ourGuess) # The previously replaced 0s are going back to the original letters 
    #ex. anonymous -> anon0mous -> [_][_][_][_]0[_][_][_][_] -> [_][_][_][_]y[_][_][_][_]
    #print("OurGuess :" + ourGuess)
    count -= occurence
    print("Letters remaining to guess: " + str(count))
    # print("word " + word) #Prints the word
    print("OurGuess :" + ourGuess)
  elif incorrectLetters.find(guess) == -1 and letterBank.count(guess) == 0:
    incorrectLetters += guess
    tries -= 1
    print("Letter bank: [" + letterBank + "] Incorrect letters: [" + incorrectLetters + "]")
    print("OurGuess :" + ourGuess)
    print("Bad guess, " + str(tries) + " tries left")
  else:
    print("You already guessed that!!")


if count < 1:
  print("You Win! The word is " + original)
elif tries == 0:
  print("You lose!, The word was " + original)