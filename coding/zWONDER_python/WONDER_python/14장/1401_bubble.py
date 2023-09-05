import os
import math
import random as r
import time as t

bubb = [0] * 58
for met in range(58) :
    bubb[met] = r.randrange(24, 72)             # 화면 밖에서 물방울 시작

for k in range(300) :
    for met in range(58) :
        if bubb[met] > 0 :                          # 물방울 높이 > 0이면
            bubb[met] = bubb[met] - 1                   # 높이 1 감소
        else:                                       # 화면 밖에서 다시 시작
            bubb[met] = r.randrange(24, 48)
    os.system('cls')
    for jul in range(24) :
        for s in range(int(math.sin(jul) * 3 + 3)): # 사인값만큼 옆으로
            print(' ', end = '')
        for met in range(58) :
            if bubb[met] == jul :
                print(' O', end = '')
            else:
                print(' ', end = '')
        print()
    t.sleep(0.03)                               # 화면 깜빡임 방지
input()
