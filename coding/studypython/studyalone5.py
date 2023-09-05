from tkinter import *
from tkinter import messagebox

def button(event) :
    user_id = et1.get()
    if user_id in IDPW :
        if IDPW[user_id] == et2.get()  :
            messagebox.showinfo('성공','환영합니다')
        else :
            messagebox.showinfo('실패','비밀번호가 일치하지 않습니다')
    else :
        messagebox.showinfo('실패','아이디가 존재하지 않습니다.')
        


win = Tk()
win.title('로그인 하세요')
win.resizable(False,False)

IDPW = {"시르메":"abc123" , "alswo2817":"te7129un!"}



lb1 = Label(win,text='아이디')
et1 = Entry(win,width=40)
lb1.pack()
et1.pack()

lb2 = Label(win,text='비밀번호')
et2 = Entry(win , width=40, show='*')
lb2.pack()
et2.pack()

btn = Button(win,text='로그인',command=button)
btn.pack(fill='x')

win.bind('<Return>',button)

win.mainloop()