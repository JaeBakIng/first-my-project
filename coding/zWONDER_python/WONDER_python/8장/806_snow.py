import os
import random as r
import time as t

snow = [0] * 120
for jul in range(120) :
    snow[jul] = r.randrange(-25, 0) # 눈 높이: 화면 밖에서 시작

for k in range(50) :
    for met in range(120) :
        if snow[met] < 23 :             # 눈 높이 < 23이면
            snow[met] = snow[met] + 1         # 눈 높이 1 증가

    os.system('cls')
    for jul in range(24) :
        for met in range(120) :
            if snow[met] == jul :
                print('*', end='')
            else :
                print(' ', end='')
        print()
    t.sleep(1)
input()
