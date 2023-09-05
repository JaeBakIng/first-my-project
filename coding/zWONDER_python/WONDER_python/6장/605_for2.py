sum = 0                     # 변수는 사용 전에 초기화해야 한다
for k in range(2, 31, 2) :  # 0부터 59까지 k에 대입
    print('%d ' % k, end = '')
    sum = sum + k
print('\nsum =', sum)
