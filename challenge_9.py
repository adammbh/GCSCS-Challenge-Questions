import random

names = [
    'Taher',
    'Adam',
    'Ali',
    'Abdo',
    'Ahmed',
    'Youssef',
    'Sheeba',
]

# RANDOM = random.choice(names)
name = input('Enter your name: ')

if name in names:
    print('You\'re cool')
else: 
    print('Nice to meet you!')