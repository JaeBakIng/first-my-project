import turtle as t
import random as r

def pos(ux, uy) :
    global hit
    cx, cy = t.pos()
    if cx >= -20 and cx <= 20 and cy >= -20 and cy <= 20 :
        hit = hit + 1
        t.write('헐', font=('', 10))

hit = 0
scr = t.Screen()
scr.bgpic('man.gif')    # man.gif를 배경 화면으로 표시

t.penup()
t.left(45)
t.goto(-250, -250)
t.pencolor('red')
t.shape('circle')

for s in range(10) :
    for k in range(120) :
        t.fd(r.randrange(2, 11))
        t.onscreenclick(pos)
    t.left(180)
t.write(hit, font=('', 20))
input()
