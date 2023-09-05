import random

com = random.randrange(3)

user = int(input('가위=0 바위=1 보=2 입력: '))

if user==com :
    print('무승부!')

elif ((user==0 and com==2) or (user==1 and com==0) or (user==2 and com==1)) :
    print('user 승!')

else :
    print('com 승!')