price=int(input('기기값 입력:'))
used =int(input('사용 개월 수:'))

mpay= (price/24)
left=(24-used)

print('\n매달 내는 돈 = %.1f원' %mpay)
print('남은 약정기간= %d개월' %left)
print('위약금=',mpay*left,'원')