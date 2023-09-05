import random

com = random.randrange(0, 2)    # randrange(0, 2): 0과 1 사이 무작위 수
user = int(input('홀 0, 짝 1 입력: '))
chip = 0                        # 변수는 사용 전에 초기화해야 함

if com == user :
    chip = chip + 10                # if의 조건이 참일 때 블록
    print('\n맞췄음')
else :
    chip = chip - 10                # if의 조건이 거짓일 때 블록
    print('\n틀렸음')
print('chip = %d' % chip)       # if에 상관없이 무조건 실행되는 일반코드
