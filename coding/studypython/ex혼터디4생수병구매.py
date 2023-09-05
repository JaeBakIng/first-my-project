from functools import total_ordering


person=int(input('MT 인원수: '))
amount=int(input('1인당 생수 개수: '))

pack = (person * amount) // 15
bottle= (person * amount) % 15
total=person*amount
total2=(pack*10000) + (bottle*900)

print()
print('필요한 생수 개수:%d' % total)
print('생수 팩 구매량 %d개 %d원' % (pack,pack*10000))
print('생수 낱개 구매량 %d개 %d원' % (bottle,bottle*900))
print('총 구매 비용 %d원' % total2)