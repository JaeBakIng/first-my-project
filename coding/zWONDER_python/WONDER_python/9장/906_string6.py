arr = [0]
arr = input('3개 입력: ').split()
b = map(int, arr) # map(): arr의 모든 데이터를 정수로 바꿈

for k in b :
    print(k * 2)
