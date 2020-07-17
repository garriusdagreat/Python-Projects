# Guess the Number Game!
# A very barebones guessing game. 

import random

print('Hey there! What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1-10.') 
secretNum = random.randint(1, 10)

#print('DEBUG: The secret number is ' + str(secretNum))

try:
  for guessesTaken in range(1, 5):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNum:
      print('That is too low.')

    elif guess > secretNum:
      print('That is too high.')
  
    else:
      break
      
except ValueError:
  print('You did not enter a number')
  
print('You guessed my secret number!')