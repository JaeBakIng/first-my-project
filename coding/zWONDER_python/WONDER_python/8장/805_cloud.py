import os
import random as r
import time as t

pos, spd = [0] * 25, [0] * 25
for jul in range(25) :
    pos[jul] = r.randrange(-25, 0)      # -25부터 –1까지 구름 위치 만듦
    spd[jul] = r.randrange(1, 10)       # 1부터 9까지 구름 속도 만듦

for k in range(100) :
    os.system('cls')
    for jul in range(25) :
        pos[jul] = pos[jul] + spd[jul]        # 구름 위치는 위치+속도
        if pos[jul] > 110 :                   # 위치가 110보다 크면
            spd[jul] = r.randrange(1, 10)           # 구름 속도 변경
            pos[jul] = 0                            # 다시 시작
        for met in range(110) :
            if pos[jul] == met :
                print('CLOUD', end='')
            else :
                print(' ', end='')
        print()
    t.sleep(1)
input()
