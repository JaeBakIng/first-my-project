phone=int(input('기계값 입력: '))
use=int(input('사용 개월 수: '))

money= phone / 24
left= 24-use
total=money*left

print()
print('매달 내는 돈 = %d원' % money)
print('남은 약정 기간 = %d개월' % left)
print('위약금 = %.1f원' % total)