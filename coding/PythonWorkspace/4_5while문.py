import random

com = random.randrange(1,21)

while True :
    user = int(input('1~20사이 숫자 입력:'))
    if com == user :
        print('맞췄습니다')
        break
    elif com > user :
        print('업!')
    else :
        print('다운!')