with open('passwd.txt','r') as pwdata :
    pwd_dic={}
    for line in pwdata :
        key = line.strip().split(':')
        pwd_dic[key[0]] = key[1]

user_id = input('아이디 입력:')
user_pw = input('비밀번호 입력:')

if pwd_dic.get(user_id) == user_pw :
    print('환영합니다')
else:
    print('오류')

print()
print(pwd_dic.get(user_id))