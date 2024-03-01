from random import randint

def rolling_the_dice(number: int):
    numbers = []
    if number <= 0:
        raise ValueError

    for _ in range(number):
        numbers.append(randint(1,6))
    return numbers


def main():
    while True:
        try:
            user_input: str = input('How many dice you want to roll?')
            if user_input.lower() == 'exit':
                print('Thanks for playing :)')
                break
                """Thanks to that asterix and print 'sep' function. The outcome will look better :D """
            numbers_on_dice = rolling_the_dice(int(user_input))
            print(*number_on_dice, sep=", ")
            print(f"The sum of that is: {sum(numbers_on_dice)}")

        except ValueError:
            print('Please enter valid number...')


main()
