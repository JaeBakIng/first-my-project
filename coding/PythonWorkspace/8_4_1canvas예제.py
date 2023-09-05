from tkinter import *
import time as t
win = Tk()

canvas = Canvas(win, width='1000', height='200')
canvas.pack() #canvas 를 만들어서 win에 붙혀줌

img = PhotoImage(file='slot4.png') 
canvas.create_image(0,100,image=img) #canvas 이미지 객체를 만들어서 x=0 , y=100 인 지점에 이미지를 넣어줌 처음으로 만들었으므로 id는 1번이된다


for k in range(0,91) :
        if(k%2==0) :
                canvas.move(1,10,20) # 1번 객체 canvas를 현재 위치 기준으로 +10,+20 위치로 이동
        else :
                canvas.move(1,10,-20) # 1번 객체 canvas를 현재 위치 기준으로 +10,-20 위치로 이동
        win.update() #윈도우를 k번 마다 다시 업데이트 해줌
        t.sleep(0.1)

win.mainloop()