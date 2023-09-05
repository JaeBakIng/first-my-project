class Fried :
    num = 0  #멤버변수 2개
    name='' #4, 변수에 값이 저장됨

        #initialize 생성자(멤버 함수의 일종)
    def __init__(self,name) : # 2, name parameter에 값이 들어가고
        self.name = name #3, 이줄 self.name을 거쳐
    # 생성자의 역할
    # 1,멤버 변수 초기화
    # 2,객체의 초기화 담당  (시험!!)



    def fry(self,min,src='없음') :
        self.num = self.num+1
        print(self.name,min, '분 튀김, 소스:',src,'self=',self.num,'\n')

chicken = Fried('통닭') # 1, 객체를 만들면서 초기화
shrimp = Fried('새우')

chicken.fry(4,'갈비소스')
chicken.fry(6)
chicken.fry(5,'고천소스')
chicken.fry(7,'불소스')
shrimp.fry(10,'소금')


        