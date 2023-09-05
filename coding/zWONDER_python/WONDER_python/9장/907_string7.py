var1 = '사과'
st1 = '{0}는 과일'
st2 = '{0}, {1}는 과일'

st3 = st1.format(var1)              # {0} 위치에 사과 삽입
print(st3)
st3 = st2.format(var1, '포도')      # {0} 위치에 사과, {1} 위치에 포도 삽입
print(st3)
