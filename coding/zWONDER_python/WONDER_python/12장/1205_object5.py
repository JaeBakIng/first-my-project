class Fried :                   # Fried 객체 정의
    num = 0                         # Fried 객체 변수 num
    name = ''                       # Fried 객체 변수 name

    def __init__(self, name) :      # Fried 객체 초기화 함수
        self.name = name

    def fry(self, min, src = '없음') :
        self.num = self.num + 1
        print(self.name, min, '분 튀김, 소스:', src, 'n=', self.num, '\n')

chicken = Fried('통닭')           # chicken 객체 만듦: 객체 이름 통닭
shrimp = Fried('새우')            # shrimp 객체 만듦: 객체 이름 새우

chicken.fry(4, '갈비 소스')
shrimp.fry(7)
chicken.fry(5, '고천 소스')
shrimp.fry(7)
