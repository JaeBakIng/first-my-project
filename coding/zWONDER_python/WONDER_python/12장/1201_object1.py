class Fried :                           # Fried 객체 정의 시작
    def fry(self, min, src = '없음') :      # Fried 객체 속한 메소드 fry()
        print(min, '분 튀김, 소스:', src, '\n')

chicken = Fried()                       # Fried 객체 만듦 -> chicken

chicken.fry(4, '갈비 소스')             # chicken.fry(): 객체의 함수 호출
chicken.fry(6)
chicken.fry(5, '고천 소스')
chicken.fry(7, '불 소스')
