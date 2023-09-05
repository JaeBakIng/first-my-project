person = int(input('인원수: '))

order = person // 4
order = order + int(person % 4 != 0)

print('\n주문 피자 개수 %d판' % order)
print('총 피자 가격 %d원' % (order * 12000))
