import random as r
import time as t

slot=[0,0,0]

for s in range(3) :
    for k in range(3) :
        slot[k]=r.randrange(7,9)
        print('%d ' % slot[k] , end='')
        t.sleep(0.5)
    if slot[0]==7 and slot[1]==7 and slot[2]==7 :
        print('잭팟입니다!')
    else :
        print('아깝습니다!')