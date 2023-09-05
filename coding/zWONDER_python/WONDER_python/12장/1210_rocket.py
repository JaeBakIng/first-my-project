from turtle import *
from random import *
setup(width = 900, height = 700)

class Rocket(Turtle) :      # class Rocket 정의 - Turtle로부터 상속
    def fire(self) :            # Rocket 메소드 fire()
        self.pencolor('#F3E1E1')
        self.penup()
        self.goto(-451, randrange(-340, 340))
        self.pendown()
        for k in range(1, 120) :
            self.pensize((121 - k) / 4)
            self.fd(k / 7)

roc = Rocket()              # class Rocket 객체 roc
for k in range(7) :
    roc.fire()                  # fire() 메소드 호출
done()
