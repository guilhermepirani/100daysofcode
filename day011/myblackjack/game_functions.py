'''Functions for the blackjack game'''

import os
import random

def clear_console():
    '''Clears console independent of OS'''

    command = 'clear'
    if os.name in ['nt', 'dos']:
        command = 'cls'
    os.system(command)

def set_decks(number_of_decks):
    '''Sets deck for a new game'''

    # Setting up deck
    values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    decks_used = number_of_decks
    return [value for value in values for suit in suites * decks_used]

def game_start(deck):
    '''Sets the table for a new game'''

    dealer_hand = [random.choice(deck)]
    [deck.remove(value) for value in dealer_hand]
    player_hand = [random.choice(deck), random.choice(deck)]
    [deck.remove(value) for value in player_hand]
    
    print(f"Dealer has: {dealer_hand}")
    print(f"Player has: {player_hand}")
    
    return {'player_hand': player_hand, 'dealer_hand': dealer_hand, 'deck': deck}

def draw(game, person):
    '''Hits a card'''

    new_card = [random.choice(game['deck'])]
    game[person + '_hand'].append(new_card[0])
    game['deck'].remove(new_card[0])
    
    return game

def check_score(game, person):
    '''Checks a persons score'''

    blackjack_values = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11,
    }

    temp_hand = game[person + '_hand'].copy()

    for index, card in enumerate(temp_hand):
        if type(card) is str:
            temp_hand[index] = blackjack_values.get(card)
    
    # Solving Ace bi-value
    if 11 in temp_hand and sum(temp_hand) > 21:
        temp_hand.remove(11)
        temp_hand.append(1)

    return sum(temp_hand)

