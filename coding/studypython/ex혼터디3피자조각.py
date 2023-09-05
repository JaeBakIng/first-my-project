num1=int(input('불고기피자 조각 수: '))
num2=int(input('쉬림프피자 조각 수: '))

print('불고기피자 %d조각' % num1)
print('쉬림프피자 %d조각' % num2)
print('조각 가능?:%s' % (num1 % 2==0 and num2 % 2==0))