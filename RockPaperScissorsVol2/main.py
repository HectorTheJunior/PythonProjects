from random import choice
import sys


class RPS:
    def __init__(self):
        print("Welcome to Rock Paper Scissors 12000!!!")
        self.moves: dict = {'rock': '✊', 'paper': '✋', "scissors": '✌️'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.user_points = 0
        self.computer_points = 0

    def play_game(self):
        print(f"You vs PC. Score: {self.user_points}|{self.computer_points}")
        user_move: str = input('Rock, Paper, Scissors >>').lower()

        if user_move == 'exit':
            print("Thanks for playing")
            sys.exit()

        if user_move not in self.valid_moves:
            print('Sorry but you have to enter valid move')
            return self.play_game()

        computer_move: str = choice(self.valid_moves)

        self.display_moves(user_move, computer_move)
        self.check_moves(user_move, computer_move)


    def display_moves(self, user_move: str, computer_move: str):
        print("----------")
        print(f'You choose: {self.moves[user_move]}\n The computer choose: {self.moves[computer_move]}')
        print("----------")

    def check_moves(self, user_move: str, computer_move: str):
        if user_move == computer_move:
            print("It's a tie!")
        elif user_move == 'scissors' and computer_move == 'rock':
            print('Ups, Points for computer')
            self.computer_points += 1
        elif user_move == 'paper' and computer_move == 'scissors':
            print('Ups. Points for computer')
            self.computer_points += 1
        elif user_move == 'rock' and computer_move == 'paper':
            print('Ups. Points for computer')
            self.computer_points += 1
        else:
            print('Nice. Points for you')
            self.user_points += 1
        if self.computer_points == 3:
            print('Computer wins!!')
            sys.exit()
        elif self.user_points == 3:
            print("You win congrats !!!")
            sys.exit()

rps = RPS()

while True:
    rps.play_gam
