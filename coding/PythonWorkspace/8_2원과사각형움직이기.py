from tkinter import *
import random as r
import time as t
win = Tk()

canvas = Canvas(win, width=1000,height=500)
canvas.pack()
id1 = canvas.create_oval(0,240,20,260,fill='red') #x1,y1,x2,y2 이므로 20,20 크기의 원이 생성됨 위치는 10,250
id2 = canvas.create_rectangle(980,240,1000,260,fill='blue')# 20,20 크기의 사각형이 생성되고 위치는 990,250

for k in range (150) :
    canvas.move(id1, r.randrange(10),r.randrange(-10,11)) #id1번(원) 의 객체를 0~9의 무작위수로 오른쪽으로 -10~10무작위수로 위아래로 움직이게 함
    canvas.move(id2, r.randrange(-9,1),r.randrange(-10,11))# id2번(사각형) 의 객체를 -9~0의 무작위 수로 왼쪽으로 -10~10무작위수로 위아래로 움직이게 함
    win.update()
    t.sleep(0.05)

win.mainloop()