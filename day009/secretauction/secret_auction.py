import os

from art import logo


def clear_console():
    '''Clears console independent of OS'''

    command = 'clear'
    if os.name in ['nt', 'dos']:
        command = 'cls'
    os.system(command)

def get_bidders(dict):
    '''Adds new bidders to auction'''

    while True:
        bidder = input("What's your name? ")
        bid = int(input("What's your bid? $"))

        dict[bidder] = bid

        add_bidder = ''
        while add_bidder not in ["yes", "no"]:
            add_bidder = input("Add another bidder? Yes or No: ").lower()

        clear_console()
        if add_bidder == "no":
            break

def print_winners(dict):
    '''Print winners names and bid'''

    winner_bid = 0
    winner_name = ''
    for bidder, bid in dict.items():
        if bid > winner_bid:
            winner_bid = bid
            winner_name = bidder
        elif bid == winner_bid:
            winner_name += f" and {bidder}"
    
    print(f"{winner_name} won with a bid of ${winner_bid}.")


if __name__ == '__main__':
        
    print(logo)
    print("Welcome to Secret Auction Program.")

    bidders = {}
    get_bidders(bidders)
    print_winners(bidders)

