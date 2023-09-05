class Fried : 
    name=''
    total = 0
    num = 0
    def __init__(self,name) :
        self.name = name

    def fry(self,min,src='없음') :
        self.num =self.num + 1
        Fried.total = Fried.total + 1
        print(self.name,'튀김 수=',self.num,'전체=',Fried.total)

chicken = Fried('통닭')
shrimp  = Fried('새우')

chicken.fry(4,'갈비 소스')
shrimp.fry(7)
chicken.fry(7)
shrimp.fry(8,'소금')