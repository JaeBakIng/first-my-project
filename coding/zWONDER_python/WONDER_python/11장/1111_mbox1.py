from tkinter import *
from tkinter import messagebox # messagebox를 다시 가져옴
win = Tk()

def info() :
    messagebox.showinfo('경고', '누르지 마쇼!')

img = PhotoImage(file = 'man3.png')
button = Button(win, image = img, command = info)
button.pack()
win.mainloop()
