from tkinter import *
win = Tk()
win.geometry('300x100')

def name(event) :
    label.config(text = '이름: ' + svar.get())

label = Label(win, text = '이름 입력', font = ('', 15))
label.pack()
svar = StringVar() # 문자열 객체 만듦
entry = Entry(win, textvariable = svar, font=('', 15))
entry.pack()
entry.bind('<Return>', name)
win.mainloop()
