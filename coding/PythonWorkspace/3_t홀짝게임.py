import random

com = random.randrange(0,2)
user = int(input('홀 0 , 짝 1 입력:'))
chip=0

if com==user :
    chip =chip + 10
    print()
    print('맞았음')
    print('칩= %d'% chip)
else :
    chip = chip- 10
    print()
    print('틀렸음')
    print('칩= %d'% chip)



    