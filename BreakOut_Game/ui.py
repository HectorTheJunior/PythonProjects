import random

ALIGNMENT = 'center'
COLOR = "white"
COLOR_LIST = ['light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki']

class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(random.choice(COLOR_LIST))
        self.header()

    def header(self):
        self.clear()
        self.goto(0, -150)
        self.write('Breakout', align=ALIGNMENT)
        self.goto(0, -180)
        self.write("Press Space to PAUSE or RESUME", align=ALIGNMENT)

    def change_color(self):
        self.clear()
        self.color(random.choice(COLOR_LIST))
        self.header()

    def paused_status(self):
        self.clear()
        self.change_color()
        time.sleep(0.5)

    def game_over(self, win):
        self.clear()
        if win == True:
            self.write('You clear the board', align=ALIGNMENT)
        else:
            self.write("Game Over", align=ALIGNMENT)
