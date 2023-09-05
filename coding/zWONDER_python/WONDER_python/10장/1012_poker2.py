import random as r

def prob(max) :                     # 확률반영 무작위 수 생성 함수
    pnum = r.randrange(max ** 2 * 100)
    for k in range(max + 1) :
        if pnum <= (k ** 2 * 100) :
            return k

rule = { 0:'스티플', 1:'포카드', 2:'풀하우스', 3:'플러시',
         4:'스트레이트', 5:'트리플', 6:'투페어', 7:'원페어' }
user, com = [0, 0], [0, 0]
chip = 10

while True :
    com[0], user[0] = r.randrange(1, 14), r.randrange(1, 14)
    com[1], user[1] = prob(7), prob(7)      # 확률 반영 무작위 수 생성
    print('\nyou >', user[0], rule[user[1]], '<', user[1])
    bet = int(input('\tchip = %d, 배팅(0은 포기): ' % chip))
    print('com >', com[0], rule[com[1]], '<', com[1])

    if bet <= 0 or bet > chip: continue     # 이번 판 포기
    if com[1] < user[1] or (com[1] == user[1] and com[0] > user[0]):
        chip = chip - bet                       # com이 이긴 경우
        print('\tcom WIN! chip = %d ' % chip)
    else :                                  # user가 이긴 경우
        chip = chip + bet
        print('\tyou WIN! chip = %d ' % chip)
    if chip <= 0 or chip >= 100: break      # 게임 종료
