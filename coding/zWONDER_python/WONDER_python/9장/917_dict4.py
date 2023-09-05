dic = {'사과':1800, '포도':2500, '망고':3200}

print(dic.keys())       # .keys() 결과는 dict_keys([])
print(dic.values())     # .values() 결과는 dict_values([])
print(dic.items())      # .items() 결과는 dict_items([])

arr = list(dic.keys())  # .keys() 결과를 리스트 형태로 전환
print(arr)
