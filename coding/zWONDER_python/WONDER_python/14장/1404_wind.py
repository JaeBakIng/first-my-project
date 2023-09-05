import os
import random as r
import time as t

wind = [0] * 58
wd = -1                             # wd는 바람 방향
for met in range(58) :
    wind[met] = r.randrange(24)

for k in range(1, 500) :
    if k % r.randrange(20, 50) == 0 :   # k % 무작위 수: 0이면 바람 방향 바꿈
        wd = 0 - wd                         # -1은 +1로, -1은 +1로
    for met in range(58) :
        wind[met] = wind[met] + wd
        if wind[met] < 0 :                  # 화면 벗어나면 밑에서 시작
            wind[met] = r.randrange(24, 30)
        elif wind[met] > 23 :               # 화면 벗어나면 위에서 시작
            wind[met] = r.randrange(-6, 0)
    os.system('cls')
    for jul in range(24) :
        for s in range(r.randrange(5)) :    # 무작위 수로 좌우 흔들림
            print(' ', end = '')
        for met in range(58) :
            if wind[met] == jul :
                print(' ~', end = '')
            else:
                print(' ', end = '')
        print()
    t.sleep(r.random() / 10)            # 화면 깜빡임 방지
input()
