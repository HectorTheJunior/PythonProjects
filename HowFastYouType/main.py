import tkinter
import tkinter as tk


root = tk.Tk()
root.title("How fast are you?")

root.geometry("700x700")

root.option_add('*Label.Font', 'Lato 20')
root.option_add("*Button.Font", 'Lato 20')


def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget("text")[0].lower():
            labelRight.configure(text=labelRight.cget('text')[1:])
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except tkinter.TclError:
        pass

def reset_labels():
    text = "The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by fox whelps. Bawds jog, flick quartz, vex nymphs. Waltz, bad nymph, for quick jigs vex! Fox nymphs grab quick-jived waltz. Brick quiz whangs jumpy veldt fox. Bright vixens jump; dozy fowl quack. Quick wafting zephyrs vex bold Jim. Quick zephyrs blow, vexing daft Jim. Sex-charged fop blew my"
    splitPoint = 0
    global labelLeft
    labelLeft = tk.Label(root, text=text[0:splitPoint], fg='grey')
    labelLeft.place(relx=0.5, rely=0.5, anchor='e')

    global labelRight
    labelRight = tk.Label(root, text = text[splitPoint:], fg='grey')
    labelRight.place(relx=0.5, rely=0.5, anchor='w')

    global currentLetterLabel
    currentLetterLabel = tk.Label(root, text=text[splitPoint], fg='black')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor='n')

    global timeLeftLabel
    timeLeftLabel = tk.Label(root, text=f'0 Seconds', fg='grey')
    timeLeftLabel.place(relx=0.5, rely=0.4, anchor='s')

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)

    global passedSeconds
    passedSeconds = 0

    root.after(60000, stopTest)
    root.after(1000, addSecond)

def stopTest():
    global writeAble
    writeAble = False

    amoutWords = len(labelLeft.cget('text').split(' '))

    timeLeftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    global resultLabel
    resultLabel = tk.Label(root, text=f'Words per min: {amoutWords}', fg='black')
    resultLabel.place(relx=0.5, rely=0.4, anchor='center')

    global resultButton
    resultButton = tk.Button(root, text='Retry', command=restart)
    resultButton.place(relx=0.5, rely=0.6, anchor='center')

def restart():
    resultLabel.destroy()
    resultButton.destroy()

    reset_labels()

def addSecond():
    global passedSeconds
    passedSeconds += 1

    timeLeftLabel.configure(text=f'{passedSeconds} Sec')

    if writeAble:
        root.after(1000, addSecond)


reset_labels()
root.mainloop()
