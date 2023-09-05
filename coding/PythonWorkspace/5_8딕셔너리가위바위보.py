import random as r

str  = ['가위','바위','보']
rule = {0:1,1:2,2:0} #가위바위보에서 지는 경우 (가위:바위)(바위:보)(보:가위)

user = int(input('가위 0 바위 1 보 2 선택:'))
com  = r.randrange(3)

print('user=%s, com=%s' % (str[user],str[com]))

if user == com :
    print('비겼습니다.')
elif (rule[com] and user==1) or (rule[com] and user==2) or (rule[com] and user==0): # rule[com] == user 컴퓨터 지는경우(유저가 이기는경우)
    print('user 승!')
else :
    print('com 승!')

print(com)
print(rule[com])