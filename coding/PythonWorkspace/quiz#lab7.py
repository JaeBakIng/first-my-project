from tkinter import *
from tkinter import messagebox
win = Tk()
win.title('성적 확인 프로그램')
win.geometry('300x100')
win.resizable(False,False)


def enter() :
    g = float(entry.get())

    if (g<=100) :
        if g >=90 :
            messagebox.showinfo('A','성적은 A입니다')
        elif g >=80 and g<90 :
            messagebox.showinfo('B','성적은 B입니다')
        elif g >=70 and g<80 :
            messagebox.showinfo('C','성적은 C입니다')
        elif g >=60 and g<70 :
            messagebox.showinfo('D','성적은 D입니다')
        else  :
            messagebox.showinfo('F','성적은 F입니다')
    else :
        messagebox.showinfo('오류','성적을 바르게 입력하세요')




label = Label(win,text='성적 입력',font=('',15))
label.pack()
entry = Entry(win,font=('',15))
entry.pack()

button = Button(win, text='성적 확인' ,command=enter)
button.pack()



win.mainloop()