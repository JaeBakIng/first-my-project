import random

chip = 10
for k in range(5) :
    com = random.randrange(1, 11)
    user = random.randrange(1, 11)
    print('\nyour num = %d, chip = %d ' % (user, chip), end = '')
    bet = int(input('배팅(0은 포기): '))
    print('com num =', com)

    if bet <= 0 or bet > chip : continue    # 이번 판 포기
    if com > user:
        chip = chip - bet
        print('컴퓨터 승! chip =', chip)
    else :
        chip = chip + bet
        print('사용자 승! chip =', chip)
    if chip <= 0 : break                    # chip이 없으면 게임 종료
