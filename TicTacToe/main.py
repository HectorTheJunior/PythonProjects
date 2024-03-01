import random

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for _ in range(3):
                row.append("-")
            self.board.append(row)

    def set_random_player(self):
        return random.randint(0, 1)

    def swap_player_turn(self, player):
        return "X" if player == '0' else '0'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def fix_spot(self, row, col, player):
        self.board[row][col] = player


    def player_win(self, player):
        win = None

        p = len(self.board)
        #check the rows
        for i in range(p):
            win = True
            for k in range(p):
                if self.board[i][k] != player:
                    win = False
                    break
            if win:
                return win

        #and now the col.
        for i in range(p):
            win = True
            for k in range(p):
                if self.board[k][i] != player:
                    win=False
                    break
            if win:
                return win
        #diagonals.
        win = True
        for i in range(p):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(p):
            if self.board[i][p - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def start_the_game(self):
        self.create_board()

        player = 'X' if self.set_random_player() == 1 else '0'

        while True:
            print(f'Player {player} turn')

            self.show_board()

            row, col = list(map(int, input("Where you want to put your marker? Enter row and column nuber").split()))
            print()

            #enter the input
            self.fix_spot(row -1, col - 1, player)

            #check if won

            if self.player_win(player):
                print(f'Player {player} win the game')
                break

            #check for draw

            if self.is_board_filled():
                print("DRAW!!")
                break
            player = self.swap_player_turn(player)

        print()
        self.show_board()

tic_tac_toe = TicTacToe()
tic_tac_toe.start_the_game()
