import time
import os

min = int(input('분 입력: '))
sec = int(input('초 입력: '))

limit = min * 60 + sec
for m in range(limit, -1, -1) :
    os.system('cls')
    print('%d분 : %d초' % (min, sec))
    time.sleep(1)
    sec = sec - 1
    if sec < 0 :
        min = min - 1
        sec = 59                # 59부터 새로운 초 다시 시작
print('그만 튀겨!')     # if에 상관없이 무조건 실행되는 일반코드
