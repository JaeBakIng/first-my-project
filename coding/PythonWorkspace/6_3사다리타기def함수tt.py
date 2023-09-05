import random as r
import time as t

def sadari (st) :
    s=r.randrange(st) # 3, split 으로 나눠진 index값중에 램덤하게 값을 반환
    return s

sdr=[0]
sdr = input('사다리 타기 항목 입력:').split() # 1, space bar 를 기준으로 항목을 나눠서 배열로 만듦
for k in range(len(sdr)) : 
    a = sadari(len(sdr))  # 2, a 변수에 sdr의 인덱스 값 만큼 함수 호출
    t.sleep(0.5)
    print()
    print(k,'번은',sdr[a]) # 4, 반환된 index값을 받아서 list의 항목 print
    del(sdr[a]) # 중복을 없애기 위함