from tkinter import *
import time as t
win = Tk()

canvas = Canvas(win, width=1000, height=200)
canvas.pack()

img = PhotoImage(file=r'C:\Users\qkral\OneDrive\바탕 화면\coding\PythonWorkspace\image\lotto.png')
canvas.create_image(0,100,image=img)

for k in range(0,90) :
    if (k%2==0) :
        canvas.move(1,10,20) #id 1 인 함수를 움직여라
    else :
        canvas.move(1,10,-20)
    
    win.update() # 움직일때마다 업데이트를 해줌
    t.sleep(0.01)
win.mainloop()
# 1/3/17 은 한쌍