'''A Flash Card App to learn languages'''

import pandas as pd
import random
import tkinter as tk
from tkinter import messagebox, StringVar

from flash_card import flashCard


# Constants
BACKGROUND_COLOR = "#B1DDC6"
TIMER = 3000 #ms

CHOICES = [
    ("French", 1),
    ("Spanish", 2),
]


# Globals
language = None
data = None
flip = None
word = {}


# Functions
def flip_card():
    card_canvas.change_image(card_back, 'English', word['English'], 'white')
    

def next_card():
    global word, flip

    # Cancels other flips if you press the button before the card flips
    window.after_cancel(flip)

    # get random word and updates card
    try:
        word = random.choice(data)
    except (IndexError, ValueError):
        card_canvas.change_image(card_front, language, 'Congratulations', 'black')
        messagebox.showinfo(title='Oops', message='You learned all words! When you open again your history will be cleared')
        return

    card_canvas.change_image(card_front, language, word[language], 'black')

    flip = window.after(TIMER, flip_card)


def known_word():
    '''Assumes the user knows a word and it doesn't need to be showed again'''
    global data

    if len(data) > 0:
        try:
            data.remove(word)
            new_data = pd.DataFrame(data)
            new_data.to_csv(f'day031/myflashcards/data/{language.lower()}_words_to_learn.csv', index=False)
            next_card()
        except ValueError:
            pass # This error happens if user tries to click to call this func and word == {}
    else:
        window.after_cancel(flip)


def select_language():
    global language
    for lang, val in CHOICES:
        if val == v.get():
            language = lang


# Language Selection window
popup = tk.Tk()
popup.title('Languages')
popup.config(padx=40, pady=20, bg=BACKGROUND_COLOR)
popup.resizable(False, False)

v = tk.IntVar()
tk.Label(popup, text='Choose your learning language: ', bg=BACKGROUND_COLOR).pack()

for choice, val in CHOICES:
    tk.Radiobutton(popup, 
                   text=choice,
                   pady = 2, 
                   variable=v,
                   command=select_language,
                   value=val,
                   bg=BACKGROUND_COLOR).pack()

tk.Button(text='OK', width=15, bg='white', command=popup.destroy).pack(pady=10)
popup.mainloop()

# Opening data by given language
try:
    data = pd.read_csv(f'day031/myflashcards/data/{language.lower()}_words_to_learn.csv').to_dict(orient='records')
except (FileNotFoundError, pd.errors.EmptyDataError):
    data = pd.read_csv(f'day031/myflashcards/data/{language.lower()}_words.csv').to_dict(orient='records')

# Main Window Setup
window = tk.Tk()
window.title('Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.resizable(False, False)

# Card
card_front = tk.PhotoImage(file='C:/100daysofcode/day031/myflashcards/images/card_front.png')
card_back = tk.PhotoImage(file='C:/100daysofcode/day031/myflashcards/images/card_back.png')

card_canvas = flashCard(card_front, language, 'word', 'black')
card_canvas.grid(row=0, column=0, columnspan=2)

flip = window.after(TIMER, next_card)

# Buttons
right_img = tk.PhotoImage(file='C:/100daysofcode/day031/myflashcards/images/right.png')
right_btn = tk.Button(image=right_img, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0, command=known_word)
right_btn.grid(row=1, column=1)

wrong_img = tk.PhotoImage(file='C:/100daysofcode/day031/myflashcards/images/wrong.png')
wrong_btn = tk.Button(image=wrong_img, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

window.mainloop()