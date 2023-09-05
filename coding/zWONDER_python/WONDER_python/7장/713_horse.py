import random as r
import time as t
import os

horse = [-9] * 13
go = True
while go :
    os.system('cls')
    for k in range(13) :
        horse[k] = horse[k] + r.randrange(9)  # 무작위 수로 말 이동
        for s in range(horse[k]) :
            print(' ', end = '')                # 말 위치만큼 공백문자
        print('%2d:>\n' % k)
        if horse[k] > 100 :                 # 결승점에 도달하면
            win = k                             # win = 승리말 번호
            go = False                          # while 반복문 종료
    t.sleep(1)
print('%d번 말 승' % win)
input()
