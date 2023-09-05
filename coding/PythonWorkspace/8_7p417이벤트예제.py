from tkinter import *
import time as t
win = Tk()

def stop(event) :
    global fd
    fd = 0
    canvas.itemconfig(1, image = img1)    # 1번 객체

def slow(event) :
     global fd
     fd = 1
     canvas.itemconfig(1, image = img1)  # 2번 객체



canvas = Canvas(win, width= 1000, height= 500)
canvas.pack()
img1 = PhotoImage(file = r'C:\Users\qkral\OneDrive\바탕 화면\coding\PythonWorkspace\image\lotto.png')
canvas.create_image(100,100,image = img1)


win.bind('<Enter>',stop)
win.bind('<Leave>',slow)
fd = 1
for k in range(900) :
    canvas.move(1,fd,1)
    win.update()
    t.sleep(0.02)
win.mainloop()