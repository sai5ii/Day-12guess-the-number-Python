#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
from replit import clear

def set_level():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  print(level)
  if level == 'hard':
    return 10
  if level == 'easy':
    return 5
  else:
    print("Not a valid choice, restart the game")
    return 0
    
  
def check_guess(guess , answer , lives):
  if guess > answer:
    print("Your Guess is too high..")
    return lives - 1
  elif guess < answer:
    print("Your Guess is too low..")
    print("Guess Again!!")
    return lives - 1
  else:
    print(f"Great guess you won. {answer} it was !!")
    return 0

def input_guess(message):
  while True:
    try:
       user_guess = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return user_guess 
       break 
      
def play_game():
  print(logo)
  print("Welcome to Guess the Number Game!")
  print("I'm thinking of a number between 1 and 100.")
  rand_number = random.choice(range(1,101))
  lives = set_level()
  while lives > 0:
    print(f"You have {lives} more turns..")
      
    user_guess = input_guess("Guess a number: ")
    lives = check_guess(user_guess,rand_number,lives)
    if lives == 0:
      print("You ran out of turns..")
    
  
while input("Do you want to play a number guessing game, yes or no: ").lower() == 'yes':
  clear()
  play_game()