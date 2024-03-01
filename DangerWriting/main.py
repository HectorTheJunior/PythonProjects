from classes import Window, WritingText, StartButton, Timer
import time
from tkinter.messagebox import showinfo


countdown = 0
start_time = 0
end_time = 0

window = Window()
text = WritingText()
start_button = StartButton()
timer = Timer()


def start_app(sth):
    global start_time
    text.focus()
    start_timer(5)
    start_time = time.time()


def start_timer(count):
    global countdown
    if count >= 0:
        timer.config(text=f'You have {count} sec left')
        countdown = window.after(1000, start_timer, count - 1)
    else:
        text.end_app()
        showinfo("HAHA", "You are done!!!!")
        calculate_time()
        window.destroy()


def calculate_time():
    global start_time, end_time
    end_time = time.time()
    running_time = round(end_time - start_time)
    showinfo('Your score', f" You was writing for {running_time} sec")


def check_for_writing(sth):
    global countdown
    window.after_cancel(countdown)
    timer.config(text='You have 5 sec left')
    start_timer(5)


start_button.bind('<Button>', start_app)
text.bind("<Key>", check_for_writing)


window.mainloop()
