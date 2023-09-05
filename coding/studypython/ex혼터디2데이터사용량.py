bprice=int(input('기본 통신비: '))
bdata=int(input('기본 데이터량 '))
add_price=int(input('1기가당 추가 통신비: '))
month=int(input('한 달 기본 사용량: '))

add= (month-bdata)*add_price #추가 통신비용
total= bprice + add #기본 통신비 + 추가 통신비용

print()
print('%d기가 까지 %d원' % (bdata,bprice))
print('%d기가 까지 사용하면 %d원' % (month,total))