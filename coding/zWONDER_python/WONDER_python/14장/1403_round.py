import os
import random as r

rain = [0] * 60
for met in range(60) :
    rain[met] = met % 25    # 1씩 증가시키면서 사선으로 배치

for k in range(300) :
    for met in range(60) :
        if met % 2 == 0 :       # 짝수 줄은 +1: 아래로 내려옴
            if rain[met] < 24 :
                rain[met] = rain[met] + 1
            else :
                rain[met] = -1
        else :                  # 홀수 줄은 -1: 위로 올라감
            if rain[met] > 0 :
                rain[met] = rain[met] - 1
            else :
                rain[met] = 24
    os.system('cls')
    for jul in range(25) :
        for met in range(60) :
            if rain[met] == jul :
                print('<>', end='')
            else :
                print(' ', end='')
        print()
input()
