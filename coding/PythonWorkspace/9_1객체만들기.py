class Fried :
    num = 0 
    def fry(self,min,src='없음') :
        self.num = self.num+1
        print(min, '분 튀김, 소스:',src,'self=',self.num,'\n')

chicken = Fried() #class의 설계도면에 따라 만들어지는 객체는 서로 독립적인 객체이다
shrimp = Fried()  #둘다 서로다른 객체

chicken.fry(4,'갈비소스')
chicken.fry(6)
chicken.fry(5,'고천소스')
chicken.fry(7,'불소스')
shrimp.fry(10,'소금') # chicken 과 shrimp 의 결과값은 거의 같지만 엄연히 다른 함수이다 다른함수인걸 판단하는것은 self (class가 생성될때 id 부여해주는 느낌)