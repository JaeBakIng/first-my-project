from tkinter import *

def press() :                   # button이 눌리면 실행되는 함수 press
    global hit                      # hit를 전역 변수로 사용
    hit = hit + 1
    label.config(text=str(hit))     # .config(): 레이블 문자 변경

hit = 0
win = Tk()
label = Label(win, text=str(hit), font=('', 10), bg='#bbffff')
button = Button(win, text='버튼 1', bd=5, padx=50, command=press)
label.pack()
button.pack()
win.mainloop()
