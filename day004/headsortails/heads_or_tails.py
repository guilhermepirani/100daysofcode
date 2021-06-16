'''Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
There are many ways of doing this. But to practice what we learnt in the last lesson,
you should generate a random number, either 0 or 1.
Then use that number to print out Heads or Tails. '''

from random import randint

# Generates 0 or 1 randomly
toss = randint(0, 1)

# Print result
if toss == 0:
    print('Heads')
else:
    print('Tails')