import random

com = random.randrange(3)
user = int(input('가위0 바위1 보2 선택: '))
print('user = %d, com = %d' % (user, com))

if user == com :
    print('비겼습니다!')
elif (com - user + 1) % 3 == 0 :
    print('user 승!')
else :
    print('com 승!')
