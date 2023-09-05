import random as r
import time as t

point = 60
luck = list()           # 빈 리스트를 만든다
user = int(input('0~19 입력(현재 60point): '))

for k in range(1, 21) : # 1부터 20까지 반복
    rnum = r.randrange(20)
    if rnum != user :       # 같지 않으면
        point = point - k       # k만큼 포인트에서 뺀다
        luck.append(rnum)       # 리스트에 값 추가
        print('\n', luck, '> %dpoint' % point)
        t.sleep(2)
    else :
        break
print('\n오늘 %dpoint' % point)
