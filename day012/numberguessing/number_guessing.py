'''A simple number guessing game'''

import os
from random import randint

LEVELS = {'easy': 10, 'hard': 5}

def clear_console():
    '''Clears console independent of OS'''

    command = 'clear'
    if os.name in ['nt', 'dos']:
        command = 'cls'
    os.system(command)

def get_game_level(dict):
    '''Ask player for Difficulty Level'''

    while True:
        game_level = input('Would you like to play on easy or hard mode? ').lower()
        if game_level not in ['easy', 'hard']:
            print("You can choose between EASY or HARD.")
            continue
        else:
            break

    return dict[game_level]

def get_guess():
    '''Get a valid guess from user'''

    while True:
        try:
            guess = int(input('Guess the number: '))
        except ValueError:
            print("Please enter an integer number")
        else:
            break
    
    return guess

def check_guess(number, guess):
    '''return from player input'''

    if guess > number:
        print("Too High!")      
    elif guess < number:
        print("Too Low!")
    else:
        print("YOU WON!")  
        return True

def game():
    '''Runs the game'''

    print("Welcome to the number guessing game!")
    guesses = get_game_level(LEVELS)
    
    print(f"You'll have {guesses} guesses to figure out the number!")
    number = randint(1, 100)

    while guesses > 0:
        guess = get_guess()

        if check_guess(number, guess):
            break

        guesses -= 1
        print(f"You have {guesses} guesses remaining")

    if guesses == 0:
        print("You lost...")

def play_again():
    '''Prompts the user to play again'''

    play_again = ''
    while play_again not in ['yes', 'y', 'no', 'n']:
        play_again = input('Would you like to play again? ').lower()

    if play_again in ['yes', 'y']:
        clear_console()
        return True
    else:
        print("See you!")
        return False

# Run game
if __name__ == '__main__':
    running = True

    while running:
        game()
        running = play_again()

