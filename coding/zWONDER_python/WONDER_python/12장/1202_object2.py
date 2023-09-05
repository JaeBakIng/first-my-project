class Fried :                           # Fried 객체 정의 시작
    def fry(self, min, src = '없음') :      # Fried 객체 속한 메소드 fry()
        print(min, '분 튀김, 소스:', src, '\n')

chicken = Fried()                       # Fried 객체 만듦 -> chicken
shrimp = Fried()                        # Fried 객체 만듦 -> shrimp

chicken.fry(4, '갈비 소스')             # chicken.fry(): 통닭 튀기기
shrimp.fry(7)                           # shrimp.fry(): 새우 튀기기
