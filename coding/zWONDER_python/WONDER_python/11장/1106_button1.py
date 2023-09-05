from tkinter import *
win = Tk()

button1 = Button(win, text='b1', fg='light yellow', bg='#ff0000')
button2 = Button(win, text='b2', bd=5, padx=20)
img = PhotoImage(file='man2.png')
button3 = Button(win, image = img)

button1.pack()
button2.pack()
button3.pack()
win.mainloop()
