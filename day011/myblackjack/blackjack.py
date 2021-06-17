from time import sleep

import game_functions
from art import logo

# Configs
number_of_decks_used = 3
wait_timer = 2
dealer_stands_on = 17

# Welcoming player
print(logo)
print("Welcome to our Blackjack table!")
print("Setting up table...")
sleep(wait_timer)

# Starting draws
deck = game_functions.set_decks(number_of_decks_used)
playing = True

while playing:
    game = game_functions.game_start(deck)
    on_hand = True

    # Get player movement
    while on_hand:
        dealer_score = game_functions.check_score(game, 'dealer')
        player_score = game_functions.check_score(game, 'player')

        if player_score == 21 and len(game['player_hand']) == 2:
            print("You Won!")
            break
        
        player_move = input("Would you like to Hit or Stand? ").lower()

        if player_move not in ['hit', 'stand']:
            print("Please choose a valid play!")
            continue

        # Progress the game for stand
        if player_move == 'stand':
            while dealer_score < dealer_stands_on:
                game = game_functions.draw(game, 'dealer')
                print(f"Dealer has: {game['dealer_hand']}")
                sleep(wait_timer)

                dealer_score = game_functions.check_score(game, 'dealer')
                
            
            if dealer_score < player_score:
                print("You Won!")
                on_hand = False
            
            elif dealer_score > 21:
                print("You Won!")
                on_hand = False

            elif dealer_score == player_score:
                print("Draw!")
                on_hand = False
                
            else:
                print("You Lose!")
                on_hand = False

        # Progress the game for hit
        if player_move == 'hit':
            game = game_functions.draw(game, 'player')
            print(f"Player has: {game['player_hand']}")

            player_score = game_functions.check_score(game, 'player')
            
        if player_score > 21:
            print('You Lose.')
            on_hand = False
        
        elif player_score == 21:
            print('You Won!')
            on_hand = False

    sleep(wait_timer)

    # Asks if player wants another hand in the same deck
    play_again = ''
    while play_again not in['yes', 'y', 'no', 'n']:
        play_again = input('Would you like to play another hand? ').lower()

    if play_again in ['yes', 'y']:
        game_functions.clear_console()
        if len(deck) < number_of_decks_used * 12:
            print("We need to change decks, just a second...")
            spleep(wait_timer)
            deck = game_functions.set_decks(number_of_decks_used)
    else:
        print("See you!")
        playing = False