import random

userwin , comwin = 0 , 0

for k in range(3) :
    com = random.randrange(2)
    print()
    user = int(input('홀수 0 짝수 1 입력: '))

    if (com == user) :
        print('사용자 승')
        userwin += 1
    else :
        print('컴퓨터 승')
        comwin += 1

print()
print('userwin=%d , comwin=%d' % (userwin,comwin))
