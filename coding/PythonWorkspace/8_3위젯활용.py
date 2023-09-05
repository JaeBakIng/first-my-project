from tkinter import *
win = Tk()

button1 = Button(win, text='b1',fg='light yellow',bg='red')

button2 = Button(win, text='b2',bd = 5, padx = 20)
img = PhotoImage(file ='lotto.png' )
button3 = Button(win,image= img)

button1.pack()
button2.pack(side='bottom')
button3.pack()
win.mainloop()

