with open('passwd.txt','r') as pwdata :
    pw_dic = {}
    for line in pwdata :
        key = line.strip().split(':')
        pw_dic[key[0]] = key[1]

id = input('아이디 입력:')
pw = input('비밀번호 입력:')

if pw_dic.get(id) == pw :
    print('안녕')
else :
    print('??')