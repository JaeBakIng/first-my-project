import os
import random as r
import time as t

rain = [0] * 120
for jul in range(120) :
    rain[jul] = r.randrange(-25, 0) # 비 높이: 화면 밖에서 시작

for k in range(300) :
    for met in range(120) :
        if rain[met] < 25 :                 # 비 높이 < 25이면
            rain[met] = rain[met] + 1           # 비 높이 1 증가
        else :                              # 처음부터 다시 시작
            rain[met] = r.randrange(-25, 0)

    os.system('cls')
    for jul in range(25) :
        for met in range(120) :
            if rain[met] == jul :
                print('|', end = '')
            else :
                print('  ', end = '')
        print()
    t.sleep(0.05)                   # 화면 깜빡임 방지
input()
