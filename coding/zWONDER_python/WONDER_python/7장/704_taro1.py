import random as r

taro = ['자유', '시작', '갈등', '풍요', '성공', '자립', '연예', '전진',
        '극복', '회피', '선택', '안정', '희생', '불행', '인내', '유혹',
        '파괴', '균형', '불안', '행복', '결단', '성취']

print('전체 타로카드')
print(taro)
print('\n첫 번째 타로는 =', taro[r.randrange(22)])
print('두 번째 타로는 =', taro[r.randrange(22)])
