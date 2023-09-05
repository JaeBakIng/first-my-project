from tkinter import *
win = Tk()

button1 = Button(win, text='b1',fg='light yellow',bg='red')

button2 = Button(win, text='b2',bd = 5, padx = 20)

img = PhotoImage(file = 'lotto.png' )
button3 = Button(win,image= img)

button1.grid(row = 1, column = 0)
button2.grid(row = 0, column = 1)
button3.grid(row = 2, column = 2)
win.mainloop()
