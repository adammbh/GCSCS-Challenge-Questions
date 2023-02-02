import random
guess = ""

randomnum = 7
guess = int(input('What number am i thinking about? '))

if randomnum == guess: 
    print('You guessed it right.')
else:
    print('No, i was thinking about: ' + str(randomnum))