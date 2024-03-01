from random import randint

random_number: int = randint(1, 10)
print('Guess the number between 1 and 10 :) Could be included. You have only 3 lives')
lives = 3
while True:
    if lives == 0:
        print('You are done. Try again later')
        break
    try:
        guess: int = int(input(f'You have {lives} lives. \nGuess: '))
    except ValueError as e:
        print('Please type only numbers. Try again')
        continue

    if guess > random_number:
        print("Too high.")
        lives -= 1
    elif guess < random_number:
        print('Too low.')
        lives -= 1
    else:
        print('You got it. Greate job.')
        break
