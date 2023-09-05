from tkinter import *
from turtle import hideturtle

def press() :
    global hit
    hit += 1
    label.config(text=str(hit))

hit = 0
win = Tk()

label = Label(win , text=str(hit),font=('',10),bg='#bbffff')
button = Button(win, text='클릭',bd=5,padx=50, command=press)

label.pack()
button.pack()

win.mainloop()