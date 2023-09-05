from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('300x200')

def click(event) :
    messagebox.showinfo('경고','건들지 마시오!')

button1 = Button(win,text='경고', bd=10,padx=30)
button1.pack()

win.bind('<B1-Motion>',click) # 마우스 좌클릭
win.mainloop()