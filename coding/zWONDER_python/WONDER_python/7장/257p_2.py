arr = [40, 30, 10, 5, 20, 9]

if 20 in arr :              # 만약 20이 리스트 arr에 있으면
    print(arr.index(20))        # 20의 위치 출력
    arr.remove(20)              # 20과 항목 모두 삭제
print(arr)
