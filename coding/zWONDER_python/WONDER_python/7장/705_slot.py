import random as r
import time as t

slot = [0, 0, 0] # slot = [0] * 3도 같은 코드
for s in range(3) :
    for k in range(3) :
        slot[k] = r.randrange(7, 9) # 무작위 수 7, 8 생성
        print('%d ' % slot[k], end = '')
        t.sleep(2)
    if slot[0] + slot[1] + slot[2] == 21 : # 모두 7인지 검사
        print('\n잭팟이 터졌네요')
        break
    else :
        print('\n아까워\n')
