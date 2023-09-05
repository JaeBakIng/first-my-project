from tkinter import *
import random as r
import time as t
win = Tk()

canvas = Canvas(win, width = 1000, height = 500)
canvas.pack()
id1 = canvas.create_oval(0, 240, 20, 260, fill = 'red')
id2 = canvas.create_rectangle(980, 240, 1000, 260, fill = 'blue')

for k in range(150) :
    canvas.move(id1, r.randrange(10), r.randrange(-10, 11))
    canvas.move(id2, r.randrange(-9, 1), r.randrange(-10, 11))
    win.update()
    t.sleep(0.1)
