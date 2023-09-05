st1 = '소문자abc 대문자ABC'

print('split >', st1.split())               # 공백을 기준으로 문자열 분리
print('split >', '1:2:3'.split(':'))        # 콜론(:)을 기준으로 문자열 분리
print('join >', ':'.join(st1))              # st1을 콜론(:)과 결합
print('replace >', st1.replace(' ', '*'))   # 공백문자를 별표로 바꾸기

print('upper >', st1.upper())
print('lower >', st1.lower())
print('swapcase >', st1.swapcase())
print('title >', st1.title())
