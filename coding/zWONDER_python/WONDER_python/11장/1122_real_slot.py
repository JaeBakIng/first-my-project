from tkinter import *
from tkinter import messagebox
import time as t
import random as r

def slot() :
    for k in range(250) :       # 이미지를 회전하는 반복문
        canvas.itemconfig(k % 3 + 1, image = imgs[k % 4])
        win.update()
        t.sleep(k / 4000)           # k가 증가할수록 느리게 돌아감
    for k in range(3) :
        ret[k] = r.randrange(4)     # 3개의 ret 리스트에 무작위 수 저장
        canvas.itemconfig(k + 1, image = imgs[ret[k]])
                                    # 결과를 확인하고 메시지를 출력하는 부분
    if ret[0] == ret[1] and ret[1] == ret[2] :
        messagebox.showinfo('슬롯머신', '잭팟!!')
    elif ret[0] == ret[1] or ret[1] == ret[2] or ret[0] == ret[2] :
        messagebox.showinfo('슬롯머신', '2개 맞았네!')
    else: messagebox.showinfo('슬롯머신', '오늘운세 꽝!')

win = Tk()
canvas = Canvas(win, width = 900, height = 200)
canvas.pack()
button = Button(win, text='슬롯 땡겨', font=('', 20), command=slot)
button.pack(fill = 'x')
                                # 변수 및 위젯 설정 부분
imgs, ret = [], [0] * 3         # imgs 2개 그림을 저장하는 리스트
for k in range(1, 5) :          # slotk.png 4개를 imgs 리스트에 저장함
    imgs.append(PhotoImage(file = 'slot' + str(k) + '.png'))
for k in range(3) :             # x축 150, 450, 750에 그림 객체 만듦
    canvas.create_image(k * 300 + 150, 100, image = imgs[0])
win.mainloop()
