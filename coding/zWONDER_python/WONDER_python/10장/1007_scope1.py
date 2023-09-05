def doomari() :     # def: 사용자가 만든 함수 doomari()
    hosik = 10          # doomari() 함수 안에서만 유효한 지역 변수
    print(hosik)

hosik = 100         # 본문코드 시작: hosik 변수 만들어 100 저장
doomari()
print(hosik)
