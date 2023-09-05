dic = {'사과':1900,'포도':2500,'망고':3200}

def get_key(dic_data) :
    arr = list(dic_data.keys()) # 2, key값만 추출하여 arr 리스트 형태로 저장 (시험:value값을 뽑아라)
    return arr # 3, arr값 리턴                                      -->(dic_data.values())   

fruit = get_key(dic) #  1, dic 딕셔너리를 get key함수에 넣어줌

print(fruit) # 4, 리턴된 arr값이 fruit에 저장되고 출력