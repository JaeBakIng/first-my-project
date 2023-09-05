person=int(input('인원수:'))

pizza =person//4
pizza= pizza+int(person % 4 !=0)

print()
print('주문 피자 개수 %d판'% pizza)
print('총 피자 가격 %d원'%(pizza*12000))
print('배달온 피자 개수 %d'%(pizza+pizza))