class Fried :                       # Fried 객체 정의
    num = 0                             # Fried 객체 변수 num

    def fry(self, min, src = '없음') :
        self.num = self.num + 1             # 객체 변수 num 1증가
        print(min, '분 튀김, 소스:', src, 'n=', self.num, '\n')

chicken = Fried()                   # Fried 객체 만듦

chicken.fry(4, '갈비 소스')
chicken.fry(6)
chicken.fry(5, '고천 소스')
chicken.fry(7, '불 소스')
