class Fried :                       # Fried 객체 정의
    name = ''                             # Fried 객체 변수 name

    def __init__(self, name) :            # Fried 객체 초기화
        self.name = name

    def fry(self, min, src = '없음') :    # Fried 객체 메소드 fry()
        print(self.name, min, '분 튀김, 소스:', src, '\n')

class Dubbob(Fried) :                # Dubbob 객체 정의: class Fried 상속
    def dbob(self) :                    # 메소드 dbob()
        print(self.name, '덮밥 > ', end = '')
        self.fry(9, '간장 소스')            # 상위객체 Fried의 fry() 호출

chicken = Fried('통닭')
donkaz = Dubbob('돈까스')          # Dubbob 객체 만듦
shrimp = Dubbob('새우')

chicken.fry(4, '갈비 소스')
donkaz.dbob()                       # dbob() 호출 - 상위객체의 fry() 사용
shrimp.fry(7)                       # 상위객체의 fry() 호출: 새우 튀김
