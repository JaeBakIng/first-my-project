arr = [20, 30, 10, 5, 20, 9]

arr.append(50)          # 리스트 맨 뒤에 새 항목 만들고 50 저장
print('.append(50) >', arr)

b = arr.pop()           # 리스트 맨 뒤에 항목 삭제
print('.pop() >', arr, b)

arr.insert(1, 60)       # 1번 위치에 60 삽입: 나머지 뒤로 밀림
print('.insert(1, 60) >', arr)

arr.remove(20)          # 항목 삭제: 맨 처음 나오는 20을 삭제
print('.insert(1, 60) >', arr)

arr.clear()             # 리스트 모든 값 삭제
print('.clear() >', arr)
