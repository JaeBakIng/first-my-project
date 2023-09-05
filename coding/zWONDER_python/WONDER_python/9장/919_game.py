import random as r

str = ['가위', '바위', '보']
rule = {0:1, 1:2, 2:0}      # 지는 경우의 수를 딕셔너리로 만듦

com = r.randrange(3)
user = int(input('가위0 바위1 보2 선택: '))
print('user = %s, com = %s' % (str[user], str[com]))

if user == com :
    print('비겼습니다')
elif rule[com] == user :    # rule[com] == user이면 com이 지는 경우
    print('user 승!')
else :
    print('com 승!')
