''' Generates a random name based on user inputs and given lists'''

from random import choice

print('Welcome to D&D Name Generator\n')
print('Choose your race:\n 1- Half-Orc\n 2- Dwarf\n 3- Elf\n')

race = 0
while race < 1 or race > 3:
    race = int(input('Enter the number of your race: '))

if race == 1:
    race = 'halforc'
if race == 2:
    race = 'dwarf'
if race == 3:
    race = 'elf'

gender = 'none'
while True:
    gender = input('Are you "male" or "female": ')
    if gender == 'male' or gender == 'female':
        break

file = open(f'day001/dednamegenerator/{race}{gender}.txt', 'r')

names= []
for line in file:
    n = line.strip()
    names.append(n)
    
file.close()

name = choice(names)
print(f'{name} is a good name for you!')