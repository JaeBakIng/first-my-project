def cal(num1, num2) :   # def: 사용자가 만든 함수 cal()
    add = num1 + num2
    mul = num1 * num2
    return add, mul         # add와 mul 데이터를 돌려줌

re1, re2 = cal(20, 5)   # return 데이터를 re1과 re2가 받음
print(re1, re2)
