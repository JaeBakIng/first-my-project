import os
import random as r

for k in range(200) :                       # 전체 200번 반복
    os.system('cls')
    for s in range(26) :                        # 사운드 미터 26줄 만듦
        for m in range(0, r.randrange(1, 58)) :     # 사운드 미터 1줄 만듦
            print('ㅁ', end = '')                        # ㅁ 한글 미음
        print()
