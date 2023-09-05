with open('passwd.txt','r') as pwdata :
    pwd_dic = {}
    for line in pwdata : # pwdata의 줄 만큼 실행
        key = line.strip().split(':') # key value 형태의 값을 :콜론 기준으로 나눔
        pwd_dic[key[0]] = key[1] #pwd_dic 이 딕셔너리 형태고 메모장을 보면 ID:PW 형태로 인덱스가 0,1 이라서 pwd_dic에 넣어줌

id = input('아이디:')
pw = input('패스워드:')

if pwd_dic.get(id) == pw : # pwd_dic 딕셔너리의 key 값(id)이 입력한 pw값(value) 와 일치할때 #pwd_dic.get(id) 는 id 에 key 해당되는 key 값을 넣으면 value 값을 반환 해준다 
    print('환영합니다')
else :
    print('아이디 또는 비밀번호가 일치하지 않습니다')
