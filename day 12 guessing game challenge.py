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

def set_difficultyu_level (user_input):
  if user_input == 'easy' : 
    no_of_lives = 10
    print (f" You have {no_of_lives} attempts remaining to guess the number!")
    return no_of_lives
  else : 
    no_of_lives = 5
    print (f" You have {no_of_lives} attempts remaining to guess the number!")
    return no_of_lives


def game ():

  difficulty_level = input ("Choose a dificulty. Type 'easy' or 'hard'!")

  winning_guess = random.randint(1,101)
  no_of_lives = set_difficultyu_level(difficulty_level)
  

  should_continue = True
  while should_continue : 
    user_guess = int (input("Make Your Guess"))
    if user_guess == winning_guess:
      print ("You won!")
      should_continue = False
    elif user_guess > winning_guess:
      print ("Too High!")
      print ("Make a guess again!")
      no_of_lives -= 1
      print(f"You have {no_of_lives} attempts left")
    elif user_guess < winning_guess:
      print ("Too low!")
      print ("Make a guess again!")
      no_of_lives -= 1
      print(f"You have {no_of_lives} attempts left")
    if no_of_lives  == 0: 
      print ("You've ran out of guesses, you lose!")
      should_continue = False


def play ():

  print (logo)

  print ('Welcome to the number guessing game!!')

  print ("I am thinking a number between 1 and 100")

  first_choice = random.randint(1,101)
  print (f" Fssst, the correct answer is {first_choice}")

  game ()


play ()


     