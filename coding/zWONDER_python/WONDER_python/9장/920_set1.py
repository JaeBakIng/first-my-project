st1 = set([1, 2, 3, 4, 5, 6])
st2 = set([3, 4, 5, 6, 7, 8])

print('교집합', st1 & st2)         # st1.intersection(st2)도 같은 코드
print('합집합', st1 | st2)         # st1.union(st2)도 같은 코드
print('차집합', st1 - st2)         # st1.diffrence(st2)도 같은 코드
print('두 집합이 같은가?', st1 == st2)
print('두 집합이 완전히 다른가?', st1.isdisjoint(st2))
