import os
import random as r
import time as t

flw = [0] * 59
for met in range(59) :
    flw[met] = r.randrange(0, 24) # 0부터 23까지 꽃 높이:0이 제일 긴 꽃

for k in range(23, -1, -1) :
    os.system('cls')
    for jul in range(24) :
        for met in range(59) :
            if flw[met] + k == jul :
                print(' @', end='')     # 꽃봉오리 출력
            elif flw[met] + k < jul :
                print(' |', end = '')   # 꽃줄기 출력
            else :
                print('  ', end = '')   # 공백 출력
        print()
    t.sleep(1)
input()
