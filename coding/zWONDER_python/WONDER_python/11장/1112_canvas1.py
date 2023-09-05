from tkinter import *
import time as t
win = Tk()

canvas = Canvas(win, width = 1000, height = 200)
canvas.pack()
img = PhotoImage(file = 'man4.png')
canvas.create_image(0, 100, image = img) # 처음 만들어진 객체 id 1번

for k in range(0, 90) :
    if k % 2 == 0 :
        canvas.move(1, 10, 20)  # 1은 캔버스에 만들어진 첫 번째 객체
    else :
        canvas.move(1, 10, -20) # 현재를 기준으로 x방향 +10, y방향 -20
    win.update()            # 윈도우를 새로 그림
    t.sleep(0.1)
win.mainloop()
