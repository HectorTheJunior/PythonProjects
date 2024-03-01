from random import choice

def run_game():
    word: str = choice(['kitchen', 'table', 'chair', 'shelf', 'door', 'window', 'roof', 'carpet',
                        'sing', 'toilet', 'bed', 'computer'])

    user_name: str = input('What is your name?\n')
    print(f"Welcome to Hangman {user_name}")

    """Setup"""
    guessed: str = ""
    tries: int = 5

    """Game"""

    while tries > 0:
        blanks: int = 0

        print("Word: ", end='')
        for letter in word:
            if letter in guessed:
                print(letter, end='')
            else:
                print("_ ", end='')
                blanks += 1
        print()  # Adding some space

        if blanks == 0:
            print('You got it')
            break

        guess: str = input('Enter a letter: ')

        if len(guess) > 1:
            print("Oh no.. You want to cheat? Ony 1 letter at the time!!")
            continue


        if guess in guessed:
            print(f'You already used the letter {guess}')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry that was wrong.. There is no {guess} in that word\n'
                  f'Tries remaining: {tries}')

        if tries < 1:
            print("Sorry you loose. Better luck next time")
            break


run_game()
