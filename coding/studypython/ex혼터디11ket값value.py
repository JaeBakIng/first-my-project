def get_key(dic_data) :
    arr = list(dic_data.keys())
    return arr

dic = {'사과':1900,'포도':2500,'망고':3200}
fruit = get_key(dic)
print(fruit)