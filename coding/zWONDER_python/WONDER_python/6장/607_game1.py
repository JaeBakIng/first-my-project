import random

userwin, comwin = 0, 0      # 승리 횟수를 저장할 변수 - 초기화
for k in range(3) :         # 0부터 2까지 총 3번 반복
    com = random.randrange(0, 2) # for에 속한 블록 시작
    user = int(input('\n홀 0, 짝 1 입력: '))

    if com == user :
        print('사용자 승')          # if에 속한 블록시작: 들여쓰기
        userwin = userwin + 1
    else :
        print('컴퓨터 승')          # else에 속한 블록시작: 들여쓰기
        comwin = comwin + 1
print('\nuserwin = %d, comwin = %d' % (userwin, comwin))
