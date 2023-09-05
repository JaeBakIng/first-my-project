with open('passwd.txt', 'r') as pwdata :
    pwd_dic = {}
    for line in pwdata :                # 한 줄씩 읽어옴
        key = line.strip().split(':')       # 콜론을 기준으로 문자열 분리
        pwd_dic[key[0]] = key[1]            # 딕셔너리 만들기

idst = input('아이디 입력: ')
pwd = input('패스워드 입력: ')

if pwd_dic.get(idst) == pwd :       # 딕셔너리에 idst값과 pwd가 같으면
    print('안녕하세요!')
else :
    print('너 누구니?')
