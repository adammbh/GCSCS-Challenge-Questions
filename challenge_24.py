import random
userinput = ""

choices = [
    'rock',
    'paper',
    'scissors'
]

userinput = input("Rock, paper, or scissors?")
robotinput = random.choices(choices)

if (userinput == robotinput):
    print('Its a tie')
if (userinput == "Rock" & robotinput == "Paper"):
    print('I win!')
else:
    print('You win')
