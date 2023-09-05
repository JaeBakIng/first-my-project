import turtle as t

t.pencolor('#FFCCBB')
t.left(90)
t.goto(0, -500)
for k in range(500) :
    t.pensize((600 - k) / 15)
    t.fd(k / 80)
