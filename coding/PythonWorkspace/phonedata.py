b_price=int(input('기본 통신비:'))
b_data=int(input('기본 데이터량:'))
o_price=int(input('1기가당 추가 통신비'))
used=int(input('한달 기본 사용량'))

add= (used-b_data)*o_price
total=add+b_price

print('\n%d기가까지 %d원'%(b_data,b_price))
print('%d기가 사용하면 %d원' %(used,total))