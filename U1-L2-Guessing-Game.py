#Uses while loop, decision making, two built in functions and a module
#Guess the number programme, using a random number generator

import random

mynumber=(random.randint(1,100)) #Assign the secret number, randomly generated between 1 and 100

print("Let's play a guessing game, I'm thinking of a number between 1 and 100...")

for turn in range (1, 6):
  usernumber = int(input("\nTurn number: " + str(turn) + "\nGuess a number:"))
  
  if usernumber < mynumber:
    print("A little higher... guess again!")
  elif usernumber > mynumber:
    print("A little lower... guess again!")
  else:
    print("You read my mind! It was " + str(mynumber) + ", well done!")
    break #End while loop once number has been guessed
  
else:
  print("Game over! You've used all 5 turns. The number was " + str(mynumber) + ".")