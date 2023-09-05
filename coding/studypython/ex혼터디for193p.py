import random

userwin = 0
comwin  = 0

for k in range(3) :
    com=random.randrange(2)
    user=int(input('홀 0 짝 1 입력: '))

    if (user==com) :
        print('유저 승!')
        userwin += 1
    else :
        print('컴퓨터 승!')
        comwin += 1

print()
print('userwin=%d , comwin=%d' % (userwin,comwin))
