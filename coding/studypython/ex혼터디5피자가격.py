person=int(input('인원수: '))

order= person // 4
#order = order + int(person % 4 != 0)
if (person % 4 != 0) : #사람수가 나머지가 있을때 피자개수 한판 추가
    order = order + 1 

print()
print('주문피자 개수 %d판' % order)
print('총 피자 가격 %d원' % (order*12000))
