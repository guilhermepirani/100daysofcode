'''Translates an input to the NATO phonetic alphabet'''

import pandas as pd

# Reads csv and saves it in a dict with key:value = letter:code
df = pd.read_csv('C:/100daysofcode/day026/NATOtranslator/nato_phonetic_alphabet.csv')
nato_dict = {row['letter']:row['code'] for index, row in df.iterrows()}

# Prompts user for word
in_word = input('Enter a word to translate: ').upper()

# Translates and prints word in NATO alphabet
out_word = [nato_dict[letter] for letter in in_word]
print(out_word)