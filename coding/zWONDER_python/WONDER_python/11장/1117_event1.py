from tkinter import *
from tkinter import messagebox
win = Tk()

def m_click(event) :            # 이벤트 호출 함수는 괄호 안에 event 필요
    messagebox.showinfo('경고', '건들지 마쇼!')

img = PhotoImage(file = 'man3.png')
label = Label(win, image = img)
label.pack()

win.bind('<Button>', m_click)   # bind: 마우스 클릭과 m_click(event) 연결
win.mainloop()
