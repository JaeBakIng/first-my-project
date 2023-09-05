st1 = '문자열'

for k in range(len(st1)) :      # k값은 0부터 len(st1) -1까지 변화
    print('< %s >' % st1[k])

for k in st1 :                  # k값은 문자열 st1의 모든 값
    print('< %s >' % k)

if '문' in st1 :                 # 문 있으면 True
    print('문 있음')
