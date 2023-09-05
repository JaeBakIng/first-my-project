import turtle as t
import random as r
import time

def pos(ux, uy) :           # ux, uy : 마우스 x, y 좌표값
    global hit                  # hit: 잡은 수를 저장하는 전역 변수
    cx, cy = t.pos()            # cx, cy : 거북이 x, y 좌표값
    if (ux - cx) < 2.0 and (uy - cy) < 2.0 :
        hit = hit + 1
        t.write('아퍼')

hit = 0
t.penup()
t.pencolor('red')
t.shape('turtle')
for k in range(50) :
    t.goto(r.randrange(-300, 301), r.randrange(-300, 301))
    t.onscreenclick(pos)            # 마우스 눌리면 pos 실행
    time.sleep(r.random() / 3)
t.write(hit, font = ('', 30))   # 문자 크기 30으로 hit 출력
t.done()                        # 화면 사라지는 것 방지
