import random as r

mine = [0] * 30
chip = 0                                # game = 5 게임 횟수
for k in range(30) :
    mine[k] = r.randrange(-29, 0)           # -29에서 -1까지 음수로 저장

for g in range(5, 0, -1) :
    print('\n')
    for k in range(30) :                    # 0부터 29까지 출력
        print('%3d' % k, end = '')
    print('\n')
    for k in range(30) :                    # mine값 출력
        if mine[k] < 0 :                        # 음수: 아직 안 열어봄
            print(' -', end = '')
        else:                                   # 양수: 이미 열어봄
            print('%3d' % mine[k], end = '')

    print('\n\n%d번 피해야 함, chip = %d' % (g, chip))
    num = int(input('번호 입력: '))
    if num < 0 or num > 29 or mine[num] > 0 :   # 양수: 이미 열어봄
        continue
    if mine[num] > -23 :                        # 30 더했을 때 8 이상 폭탄 아님
        mine[num] = mine[num] + 30                  # 30 더해 양수로 바꿈
        chip = chip + mine[num]
    else :                                      # 30 더했을 때 7 이하 폭탄
        print('꽝!! 지뢰 터졌음')
        break
print('\nYour Chip = %d' % chip)
input()
