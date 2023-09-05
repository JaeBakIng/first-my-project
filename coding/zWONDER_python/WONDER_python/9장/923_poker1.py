import random as r

rule = { 0:'스티플', 1:'포카드', 2:'풀하우스', 3:'플러시',
         4:'스트레이트', 5:'트리플', 6:'투페어', 7:'원페어' }
user, com = [0, 0], [0, 0]
chip = 10

for k in range(5) :
    com[0], user[0] = r.randrange(1, 14), r.randrange(1, 14)
    com[1], user[1] = r.randrange(8), r.randrange(8)
    print('\nyou >', user[0], rule[user[1]], '<', user[1])
    bet = int(input('\tchip = %d, 배팅(0은 포기): ' % chip))
    print('com >', com[0], rule[com[1]], '<', com[1])

    if bet <= 0 or bet > chip : # 이번 판 포기
        continue
    if com[1] < user[1] or (com[1] == user[1] and com[0] > user[0]):
        chip = chip - bet
        print('\tcom WIN! chip =', chip)
    else :
        chip = chip + bet
        print('\tyou WIN! chip =', chip)
    if chip <= 0 :              # chip이 없으면 게임 종료
        break
