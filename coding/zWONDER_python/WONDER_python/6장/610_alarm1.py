import time
import os

min = int(input('분 입력: '))
sec = int(input('초 입력: '))

for m in range(min, -1, -1) :
    for s in range(sec, -1, -1) :
        os.system('cls')
        print('%d분 : %d초' % (m, s))
        time.sleep(1)
    sec = 59                # 59부터 새로운 초 다시 시작
print('그만 튀겨!')     # if에 상관없이 무조건 실행되는 일반코드
