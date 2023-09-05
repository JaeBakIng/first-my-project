import random as r
import time as t

point = 60
luck = list()
user = int(input('0~19 입력:'))

for k in range(1,21) :
    rnum = r.randrange(20)
    if rnum != user :
        luck.append(rnum)
        point -= 2
        print()
        print(luck, '>%d point' % point)
        t.sleep(0.5)
    else :
        break
print('총점수 %dpoint' % point)