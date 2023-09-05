dic = {'사과':1800, '포도':[2500, 2800]}

if dic.get('멜론') == None :  # key(멜론)가 dic 안에 없으면
    dic['멜론'] = 2900            # 멜론: 2900 삽입
print(dic)
