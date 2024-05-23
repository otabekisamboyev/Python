# patorjk.com
from replit import clear
from art import logo
import random


def guess(guess_number):
    global attempts
    if guess_number > number:
        attempts -= 1
        print(f"Too high, try again!\nYou have {attempts} attempts remaining to guess the number\n")
    elif guess_number < number:
        attempts -= 1
        print(f"Too low, try again!\nYou have {attempts} attempts remaining to guess the number\n")
    else:
        print("You found the number, congrats!\n")
        return False


def play():
    global number
    global attempts
    print(logo)
    print("Welcome to guess number game!")
    difficulty = input("Choose game difficulty. Hard or Easy: ").lower()
    if difficulty == 'hard':
        attempts = 5
        print(f"Alright you have {attempts} attempts to find the number")
    elif difficulty == 'easy':
        attempts = 10
        print(f"Alright you have {attempts} attempts to find the number")
    else:
        print("Wrong insert, try again!")
    number = random.randint(1, 100)
    is_this_number = True
    while is_this_number:
        guessing_number = int(input("Guess the number: "))
        guess(guessing_number)
        if guessing_number == number:
            is_this_number = False
        if attempts == 0:
            is_this_number = False
            print(f"You lose. Number was: {number}")
    another_game = input("Wanna play another game? Type 'y' or 'n': ").lower()
    while another_game == 'y':
        clear()
        play()
    else:
        print("Alright, Good bye!")


play()


'''Teacher's solution
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
'''