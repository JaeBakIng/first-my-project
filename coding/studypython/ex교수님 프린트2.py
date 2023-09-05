rain = int(input('강우량 입력:'))
wind = int(input('풍속 입력:'))


print()
print("강우량(mm):",rain)
print("풍속(m/s):",wind)
print('현재 강우량은 %dmm 이고, 풍속이 %dm/s미만입니다.' %(rain,wind))

if (rain<100 and wind<30) :
    print("비행가능")
else :
    print("비행불가")

