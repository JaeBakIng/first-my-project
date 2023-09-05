from tkinter import *
from tkinter import messagebox
win = Tk()

def msg() :
    messagebox.showinfo('안내','지원하지 않는 기능입니다.')

def quit() :
    win.destroy()



menubar = Menu(win)
f1= Menu(menubar , tearoff=0) #메뉴바에 들어갈 f1 menu 생성하고 저장(tearoff=0)
f1.add_command(label='새 파일',command=msg)
f1.add_command(label='열기',command=msg)
f1.add_command(label='저장',command=msg)
f1.add_separator()
f1.add_command(label='Exit',command=quit)

menubar.add_cascade(label='File',menu=f1) #f1 메뉴 이름을 File 로 함
win.config(menu=menubar)

win.mainloop()
