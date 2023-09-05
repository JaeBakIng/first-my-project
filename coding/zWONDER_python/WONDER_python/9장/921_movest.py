import os
import math
import time as t

st = 'Phython is worderful code'
for k in range(200) :
    os.system('cls')
    for s in range(25) :
        for m in range(int(math.sin(s + k) * 6 + 10)) :     # 사인 곡선 만듦
            print(' ', end = '')
        print(st[s])
    t.sleep(0.1)                                        # 화면 깜빡임 방지
input('아무 키나 누르세요')
