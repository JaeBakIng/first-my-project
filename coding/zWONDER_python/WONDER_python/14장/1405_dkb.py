import os
import random as r
import msvcrt as m      # kbhit()가 있는 모듈
import time as t

draw = [0] * 120
c = '|'                 # 초기값 비(|)
for met in range(120) :
    draw[met] = r.randint(-25, 0)

for k in range(300) :
    os.system('cls')
    for met in range(120) :
        if draw[met] < 25 :
            draw[met] = draw[met] + 1
        else :
            draw[met] = -1
    for jul in range(25) :
        if m.kbhit():               # 키가 눌리면
            m.getch()                   # 눌린 키 제거
            if c == '|' : c = '*'       # 비(|)면 눈(*)으로
            else : c = '|'              # 눈(*)이면 비(|)로
        for met in range(120) :
            if draw[met] == jul :
                print(c, end = '')
            else :
                print(' ', end = '')
        print()
    if c == '*' : t.sleep(0.5) # 눈(*)이면 0.5초간 기다림
input()
