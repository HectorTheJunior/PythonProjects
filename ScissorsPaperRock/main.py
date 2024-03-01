""" All you need to do is importing 'random' """

import random

choice = ['Scissors', 'Paper', 'Rock']

human_score = 0
computer_score = 0

print('Hello. Will play this Greate game up to 3 points.')

game_is_on = True
while game_is_on:
    print(f'Score:{human_score}|{computer_score}')
    human = input("Chose: Scissors, Paper, Rock\n")
    computer = random.choice(choice)
    print(computer)
    if human == 'Scissors' and computer == 'Paper':
        print("Greate")
        human_score += 1
    elif human == "Paper" and computer == 'Rock':
        print("Greate")
        human_score += 1
    elif human == "Rock" and computer == "Scissors":
        print('Greate')
        human_score += 1
    elif human == computer:
        print("Draw! No points")
    else:
        print("Computer scores")
        computer_score += 1
    if human_score == 3:
        print('You win')
        game_is_on = False
    elif computer_score == 3:
        print('You loose')
        game_is_on = False
