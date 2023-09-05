with open('passwd.txt','r') as pwdata :
    pwd_dic={}
    for k in pwdata :
        line = k.strip().split(':')
        pwd_dic[line[0]]=line[1]

id = input('아이디 입력:')
pw = input('비밀번호 입력:')

if pwd_dic[id] == pw :
    print('환영합니다')
else :
    print('???')