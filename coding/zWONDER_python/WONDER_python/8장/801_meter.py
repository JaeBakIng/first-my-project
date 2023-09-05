import os
import random as r
import time as t

draw = [0] * 60
for k in range(100) :
    os.system('cls')
    for met in range(60) :
        draw[met] = r.randrange(24)
    for jul in range(24) :      # 화면 0번 줄부터 23번 줄까지 만듬
        for met in range(60) :      # 화면 좌로 60개 막대기 만듬
            if draw[met] > jul :        # 줄번호보다 크면 공백
                print('  ', end='')
            else :                  # 줄번호보다 작으면 ㅁ
                print('ㅁ', end='')
        print()                 # 한 줄 끝나면 줄바꿈
    t.sleep(0.1)            # 화면 깜빡임 방지
