'''A guess the state names game for US states'''

import pandas as pd
from turtle import Screen

from map_writer import Writer

window = Screen()
window.setup(width=750, height=500)
window.title('US States Guess Game')
window.bgpic('C:/100daysofcode/day025/statesgame/blank_states_img.gif')
window.tracer()

df = pd.read_csv('C:/100daysofcode/day025/statesgame/50_states.csv')

label = Writer()

score = 0
guessed = []

game_on = True
while game_on and len(guessed) < 50:
    window.update()

    user_guess = window.textinput(title=f'{score}/50 States', prompt='Write a State name and press Enter')

    if user_guess == 'exit':
        game_on = False

    if user_guess not in guessed:
        if user_guess in [state for state in df['state']]:
            x = [x for x in df[df['state'] == user_guess]['x']]
            y = [y for y in df[df['state'] == user_guess]['y']]
            label.move(x[0], y[0])
            label.fill(user_guess)
            guessed.append(user_guess)
            score += 1

window.exitonclick()
