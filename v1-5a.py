#####################
#####################
## Version 1-5a Below ##
#####################
#####################

### Fixed some loop holes in guessing 
# and added the letter banks

## Adding loop functionality to show letters guessed
## without using regex


print("Welcome to Hangman!")
word = "anonymous"
original = word # This is a copy of the word
count = len(word) #This is the length of characters in the word
tries = 6 # We only have 6 tries to guess the word

print("The word is " + str(count) + " letters long.")

letterBank = "" # A bank of every correctly guessed letter
incorrectLetters = ""

def wordmaker():
    # Checks each letter of the word to see if we have guessed
    # it and if it is included in the word bank 
    # and then if it is, keep the letter, 
    # otherwise make it an empty slot.
    # example: an[_]n[_][_][_][_][_]
    i = 0
    ourGuess = ""
    while i < len(word):
        if letterBank.find(word[i]) != -1:
            ourGuess += word[i]
        else:
            ourGuess += "[_]"
        i += 1
    return ourGuess

while count != 0 and tries > 0:
    print("\n") #Makes white space in the command line
    guess = input("Guess a letter: ")[0] #taking the first character inputted
    occurence = word.count(guess)

    if occurence != 0 and letterBank.count(guess) == 0:
        print("Yes, you guessed correctly!")
        letterBank += guess

        print("Letter bank: [" + letterBank + "] Incorrect letters: [" + incorrectLetters + "]")
        currentGuess = wordmaker()
        print("currentGuess: " + currentGuess)
        
        count -= occurence
        print("Letters remaining to guess: " + str(count))
        print(word)
    elif incorrectLetters.find(guess) == -1 and letterBank.count(guess) == 0:
        incorrectLetters += guess
        tries -= 1
        print("Letter bank: [" + letterBank + "] Incorrect letters: [" + incorrectLetters + "]")
        #print(word)
        print("Bad guess, " + str(tries) + " tries left")
    else:
        print("You already guessed that!!")
  
if count < 1:
    print("You Win! The word is " + original)
elif tries == 0:
    print("You lose!, The word was " + original)
