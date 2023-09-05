birth = int(input('이번 달 생일? 1은 yes, 0은 no: '))
age = int(input('나이 입력: '))

if birth == 1 and age >= 19 :
    print('\n당첨! 모히또 한 잔')
else :
    print('\n음료수 한 잔')      # if의 조건이 거짓일 때 실행 - 들여쓰기
