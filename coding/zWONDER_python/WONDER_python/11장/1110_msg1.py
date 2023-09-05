from tkinter import *
win = Tk()
win.geometry('300x100')

msg = Message(win, text = '메시지', width = 100, font = ('', 15))
msg.pack()
win.mainloop()
