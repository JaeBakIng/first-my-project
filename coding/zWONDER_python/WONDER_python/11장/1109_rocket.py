from tkinter import *
import turtle as t

def rocket() :               # button이 눌리면 실행되는 함수 rocket()
    t.reset()                       # t.reset(): 처음으로 되돌리는 함수
    t.pencolor('#FFCCBB')
    t.left(90)
    t.goto(0, -500)
    for k in range(500) :
        t.pensize((600 - k) / 15)
        t.fd(k / 80)

t.pencolor('red')           # 터틀 그래픽 화면을 나타나게 함
win = Tk()
button = Button(win, text = '로켓 발사', padx = 50, command = rocket)
button.pack()
win.mainloop()
