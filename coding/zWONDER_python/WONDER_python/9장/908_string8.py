import os
import time as t

st1 = '> I LOVE YOU <'

for k in range(len(st1) * 10) :
    os.system('cls')
    for m in range(len(st1)) :
        print(' ', st1[ (k + m) % len(st1) ]) # 한 글자씩 회전
    t.sleep(0.2)
