from tkinter import *


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('650x650')
        self.title("Be quick of loose everything")
        self.config(bg='yellow')

        self.explanation = Label(text="If you won't be writing anything for 5 sec you'll loose everything.",
                                 fg='red', bg='yellow')
        self.explanation.grid(column=0, columnspan=2, row=0)


class WritingText(Text):
    def __init__(self):
        super().__init__()
        self.config(fg='red')
        self.grid(column=0, row=2, columnspan=2)

    def end_app(self):
        self.delete("1.0", END)


class StartButton(Button):

    def __init__(self):
        super().__init__()
        self.config(text="Let's Go", bg='green', fg='black')
        self.grid(row=4, column=0, columnspan=2)


class Timer(Label):

    def __init__(self):
        super().__init__()
        self.config(text="You have 5 sec", fg='black', bg='teal')
        self.grid(column=0, row=1, columnspan=2)
