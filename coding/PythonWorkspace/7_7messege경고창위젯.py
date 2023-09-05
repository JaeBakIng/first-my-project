from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('300x200')

def info () :
    messagebox.showinfo('xxxxxx','누르지마시오!')

button = Button(win, text='*경고*',command=info)
button.pack()

win.mainloop()

