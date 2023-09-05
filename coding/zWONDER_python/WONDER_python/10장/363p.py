def fry(min, source = '없음') :   # def: 사용자가 만든 함수 fry()
    print('\n튀김옷 입히기')          # 들여쓰기부터 시작
    print(min, '분 튀기기')
    print('소스 바르기 =', source)    # fry() 함수 끝

fry(4, '갈비 소스')
fry(6)                              # 매개 변수 source에 값이 없으면 기본값 사용
fry(5, '고천 소스')
fry(7, '불 소스')
