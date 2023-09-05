def get_key(dic_data) :         # def: 사용자가 만든 함수 get_key()
    arr = list(dic_data.keys())     # .keys() 결과를 리스트 형태로 전환
    return arr                      # 리스트 arr 반환

dic = {'사과':1800, '포도':2500, '망고':3200}
fruit = get_key(dic)
print(fruit)
