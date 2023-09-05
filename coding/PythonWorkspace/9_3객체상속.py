class Fried : 
    name=''
    def __init__(self,name) :
        self.name = name

    def fry(self,min,src='없음') :
        print(min, '분 튀김, 소스:',src,'\n')

class Dubbab(Fried) :
    def dbob(self) :
        print(self.name,'덮밥 >',end='')
        self.fry(9,'간장소스')

chicken = Fried('통닭')
donkaz  = Dubbab('돈까스')
shrimp  = Dubbab('새우')

chicken.fry(4,'갈비소스')
donkaz.dbob()
shrimp.fry(5,'소금')    
