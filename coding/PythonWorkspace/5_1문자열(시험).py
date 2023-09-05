st1 = '문자열'
for k in range(len(st1)) : #st1의 문자개수만큼 for문 돌림(3번)
    print("<%s>" % st1[k]) #문자열의 개수이기 때문에 st1[k] 로 써줘야댐

for k in st1 : #k는 st1의 모든 값 
    print("<%s>" % k)

if '문' in st1 : #st1에 문이라는 문자열이 있으면 
    print('문 있음')#print