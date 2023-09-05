from tkinter import *
from tkinter import messagebox

def btn ():
    color = et.get()
    lb['bg'] = color
    messagebox.showinfo('설정','색상을'+ color +'로 변경합니다.')


win = Tk()

lb = Label(win,text='아래 빈칸에 색상을 입력하세요' ,width=40)
lb.pack()

et = Entry(win, width=40)
et.pack()

bt = Button(win,text='클릭',width=40 , command=btn)
bt.pack()

win.mainloop()