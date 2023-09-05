arr = [20, 30, 10, 5, 20, 9]

x = arr.index(30)       # 30이 있는 위치의 인덱스를 알려줌
print('.index(30) >', x)

x = arr.count(20)       # 리스트에 20이 몇 개나 있는지 알려줌
print('.count(20) >', x)

arr.sort()              # 리스트 오름차순 정렬
print('.sort() >', arr)

arr.reverse()           # 리스트 내림차순 정렬
print('.reverse() >', arr)
