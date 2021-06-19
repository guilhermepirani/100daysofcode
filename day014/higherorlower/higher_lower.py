''' A guessing game of who has most followers on instagram'''

import random
import time
import os

import art
import game_data

def clear_console():
    '''Clears console independent of OS'''

    command = 'clear'
    if os.name in ['nt', 'dos']:
        command = 'cls'
    os.system(command)

def get_data(person = None):
    '''get info from game data'''

    if person is None:
        random_person = random.choice(game_data.data)
        game_data.data.remove(random_person)
    else:
        random_person = person

    return random_person

def get_guess():
    '''Get user's guess'''

    user_guess = ''
    while user_guess not in ['a', 'b']:
        user_guess = input("Who has more followers: A or B? ").lower()

    return user_guess

def game():
    '''Runs the game'''

    print("Welcome to Higher or lower! Can you guess who has the most followers on instagram? ")
    score = 0
    person = None

    while True:
        print(art.logo)

        # Checks if there's still data to use
        if len(game_data.data) == 0:
            print("You're pretty good! You reached MAX SCORE!")
            break

        # Sets matches
        a = get_data(person)
        print(f"Option A: {a['name']}, {a['description']}, from {a['country']}.")

        print(art.vs)

        b = get_data()
        print(f"Option B: {b['name']}, {b['description']}, from {b['country']}.")

        # Prompts user for an answer
        guess = get_guess()

        # Continue game according to user's guess
        if guess == 'a' and a['follower_count'] > b['follower_count']:
            score += 1
            person = a
            print(f"You're right! Current score: {score}")
            time.sleep(2)
            clear_console()
            continue
        elif guess == 'b' and a['follower_count'] < b['follower_count']:
            score += 1
            person = b
            print(f"You're right! Current score: {score}")
            time.sleep(2)
            clear_console()
            continue
        else:
            print(f"You Lost! Score: {score}")
            break
    

game()
