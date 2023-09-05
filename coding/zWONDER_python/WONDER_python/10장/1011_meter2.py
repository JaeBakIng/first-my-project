import os
import random as r
import msvcrt                       # kbhit()가 있는 모듈

def cmeter(jul, ch = '>') :
    for k in range(200) :
        os.system('cls')
        for s in range(jul) :
            if msvcrt.kbhit() :                 # 코드 실행 중간 키가 눌리면 True
                ch = chr(ord(msvcrt.getch()))       # 문자로 바꿔 ch에 저장
            for m in range(0, r.randint(1, 110)) :
                print(ch, end='')
            print()

cmeter(20, '>')
