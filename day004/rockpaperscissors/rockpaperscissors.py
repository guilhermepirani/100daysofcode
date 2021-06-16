'''A game of rock-paper-scissors against the machine'''

from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

player_choice = 3
while  player_choice < 0 or player_choice > 2:
    player_choice = int(input("Enter 0 for rock, 1 for paper or 2 for scissors.\n"))
print(choices[player_choice])

pc_choice = randint(0, 2)
print("Computer chose:\n", choices[pc_choice])

if player_choice == 0 and pc_choice == 1:
    print('You lose"')
elif player_choice == 1 and pc_choice == 2:
    print('You lose"')
elif player_choice == 2 and pc_choice == 0:
    print('You lose"')
elif player_choice == pc_choice:
    print('Draw!')
elif player_choice == 2 and pc_choice == 1:
    print("You Won!")
elif player_choice == 1 and pc_choice == 0:
    print("You Won!")
elif player_choice == 0 and pc_choice == 2:
    print("You Won!")
