'''A virtual coffee machine'''

import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(drink):
    '''Checks if machine can produce drink'''
    for item in drink:
        if drink[item] > resources[item]:
            print(f"Sorry, the machine is out of {item}")
            return False
    return True

def process_coins():
    '''Charges the user'''
    print("Please insert coins: ")
    total = 0
    for key, value in {'quarters': 0.25, 'dimes': 0.1, 'nickles': 0.05, 'pennies': 0.01}.items():
        total += int(input(f"Insert {key}: ")) * value
    return total

def check_payment(charged, received):
    '''Checks if drink was properly paid for'''
    if charged <= received:
        change = round(received - charged, 2)
        if not change == 0:
            print(f"Here is ${change} in change.") 
        global money
        money += charged
        return True
    else:
        print("Sorry, that's less than the expected amount. Refunding now.")
        return False

def make_drink(drink, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!")

is_on = True
while is_on:
    try:
        prompt = input("What would you like? (espresso/latte/cappuccino): ")
        if prompt == 'off':
            print("Turning off...")
            for _ in range(3):
                time.sleep(1)
                print('.')
            is_on = False
        elif prompt == 'report':
            [print(f'{key}: {value}') for key, value in resources.items()]
            print(f'money: {money}')
        else:
            if check_resources(MENU[prompt]['ingredients']):
                if check_payment(MENU[prompt]['cost'], process_coins()):
                    make_drink(prompt, MENU[prompt]['ingredients'])
    except KeyError:
        continue
            
