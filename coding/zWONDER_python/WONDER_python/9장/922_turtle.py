import turtle as t
import random as r
import time

t.setup(width = 900, height = 700)
t.shape('turtle')
t.penup()
for k in range(100) :
    t.goto(r.randrange(-400, 401), r.randrange(-300, 301))
    time.sleep(r.random() / 2)
