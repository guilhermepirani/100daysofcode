'''Calculates the value of a tip given percentage and total'''

print('Welcome to tip calculator!')

pct = 0
total = 0
people = 0
available_tips = [10, 12, 15]

while total <= 0:
    total = float(input('What was the total bill? $'))

while not pct in available_tips:
    pct = int(input('What percentage tip would you like to give? 10, 12 or 15? '))

while people <= 0:
    people = int(input('How many people to share the bill? '))

final_value = round((total + total * (pct / 100)) / people, 2)

print(f'Each person should pay ${final_value} for a ${total} bill with {pct}% tip')