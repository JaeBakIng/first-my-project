import os
import random as r
import time as t

slot = ('COW', 'BTS', 'PSY', 'ELF', '777')  # 튜플로 슬롯그림 만듦
ret, chip = [], 100

while True :
    for s in range(3) :
        for k in range(10) :
            print(ret, slot[k % 5], '\n chip =', chip)
            t.sleep(0.1)
            os.system('cls')
        ret.append(slot[r.randrange(5)])
    print(ret)

    if ret[0] == ret[1] and ret[1] == ret[2] :
        chip = chip + 1000
        print('\n!!! 잭팟 !!!', ' chip =', chip)
    elif ret.count('777') == 2 :
        chip = chip + 450
        print('\n앗싸! 777 두 개', ' chip =', chip)
    else : chip = chip - 30

    if chip < 0 or chip > 500 :                 # 칩이 0 미만 500 초과 - 게임 종료
        print('\n이젠 그만~', ' chip =', chip)
        break
    ret.clear()                                 # ret 리스트 리셋
    input('\n슬롯 땡겨 -> Enter key')           # 엔터키 다시 시작
input('아무키나 누르세요')
