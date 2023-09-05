from tkinter import *
import time as t
win = Tk()

def stop(event) :                       # 마우스가 윈도우 위로 올라오면
    global fd
    fd = 0                                  # fd = 0: 움직이지 않음
    canvas.itemconfig(1, image = img1)      # itemconfig(): img1로 변경

def slow(event) :                       # 마우스가 윈도우에서 떠나면
    global fd
    fd = 1                                  # fd = 1: 오른쪽으로 움직임
    canvas.itemconfig(1, image = img2)      # itemconfig(): img2로 변경

canvas = Canvas(win, width = 1000, height = 200)
canvas.pack()
img1 = PhotoImage(file = 'man1.png')
img2 = PhotoImage(file = 'man2.png')
canvas.create_image(100, 100, image = img2)
win.bind('<Enter>', stop)
win.bind('<Leave>', slow)

fd = 1
for k in range(900) :
    canvas.move(1, fd, 0)                   # fd만큼 움직임
    win.update()
    t.sleep(0.02)                           # 너무 빨리 이동하는 것 방지
win.mainloop()
