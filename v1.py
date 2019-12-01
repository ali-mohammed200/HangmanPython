#####################
#####################
## Version 1 Below ##
#####################
#####################


print("Welcome to Hangman!")
word = "anonymous"
original = word # This is a copy of the word
count = len(word) #This is the length of characters in the word
tries = 6 # We only have 6 tries to guess the word

print("The word is " + str(count) + " letters long.")


while count != 0 and tries > 0:
  print("\n")
  guess = input("Guess a letter: ")[0] #taking the first character inputted
  occurence = word.count(guess)
  if occurence != 0:
    print("Yes, you guessed correctly!")
    word = word.replace(guess, "0")
    count -= occurence
    print("Letters remaining to guess: " + str(count))
    print(word)
  else:
    tries -= 1
    print("Bad guess, " + str(tries) + " tries left")
  
if count < 1:
  print("You Win! The word is " + original)
elif tries == 0:
  print("You lose!, The word was " + original)
