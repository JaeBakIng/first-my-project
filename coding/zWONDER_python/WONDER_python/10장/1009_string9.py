import os

def round(st1, num) :
    for k in range(len(st1)) :
        os.system('cls')
        for m in range(len(st1)) :
            for s in range(num) :       # num만큼 줄을 만들어 회전
                print(' ', st1[ (s + k + m) % len(st1) ], end = '')
            print()

for q in range(1, 22) :         # 본문코드 시작
    round('> I LOVE YOU <', q)
