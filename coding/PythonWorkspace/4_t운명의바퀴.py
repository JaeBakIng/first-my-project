import random as r
import time as t

point=60
luck=list()
user = int(input('0~19입력 (현재 60point): '))

for k in range(1,21) :
    rnum = r.randrange(20)

    if rnum != user :
        point -= 3
        luck.append(rnum)
        print()
        print(luck,'>%d point' % point)
        t.sleep(1)
    else :
        break
print('흭득한 포인트는= %dpoint' % point)