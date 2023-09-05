import random
com = random.randrange(2)
user = int(input('홀은 0 짝은1 입력: '))
chip=0 #칩을 사용해주기위해 초기화

if (user == com) :
    chip = chip + 10
    print()
    print('맞았음')

else :
    chip = chip - 10
    print()
    print('틀렸음')

print('칩 =%d' % chip)