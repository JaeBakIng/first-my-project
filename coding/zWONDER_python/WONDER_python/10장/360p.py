def func_2() :          # func2() 호출 전에 먼저 정의
    print('함수 2번')

def func_1() :          # func1() 호출 전에 먼저 정의
    print('함수 1번')
    func_2()

print('본문코드')       # 본문코드: 가장 먼저 실행
func_1()
