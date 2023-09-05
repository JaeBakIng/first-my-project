from turtle import *
from random import *

class Fwork(Turtle) :                   # Fwork 객체 정의 - Turtle로부터 상속
    def fire(self) :                        # Fwork 메소드 fire()
        self.setheading(90)                     # 터틀 객체 북쪽으로 회전
        self.penup()
        self.goto(randrange(-450, 450), -350)   # 무작위 수 만들어 이동
        self.pendown()
        self.pencolor(100, 100, 150)
        for k in range(1, randrange(70, 110)) : # 폭죽 발사
            self.pensize(k % 2 + 1)
            self.fd(k / 10)
        for k in range(1, 50) :                     # 폭죽 터짐
            self.pencolor(220, randrange(150,255), randrange(150,255))
            self.pensize(k * 3)
            self.backward(k / 10)

setup(width = 1000, height = 700)           # 화면 셋업
colormode(255)
bgcolor(0, 0, 60)

fwork = Fwork()                             # Fwork 객체 만듦
for k in range (7) :
    fwork.fire()                                # fire 메소드 호출
done()
