import turtle as t

t.colormode(255)
t.left(90)
t.goto(0, -500)
for k in range(500) :
    t.color(170, int(k / 2), int(k / 2))
    t.pensize((600 - k) / 15)
    t.fd(k / 80)
