import random as r

com = r.randrange(1,21)


while True :
    user = int(input('1부터 20까지 숫자 입력:'))
    if user==com :
        print('정답!')
        break
    elif user < com :
        print('업!')
    else :
        print('다운!')

