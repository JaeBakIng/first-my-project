def get_key(dic_data) :
        arr = list(dic_data.keys()) #2, dic 딕셔너리에서 key 값만 가져와서 리스트형태로 return 해줌
        return arr

dic = {'사과':2000 , '포도':1800 ,'배':1200} #딕셔너리 만듬
fruit = get_key(dic) # 1, 만든 get_key 함수에 dic 값을 넣어줌 3, return한 값이 fruit에 저장됨
print(fruit)