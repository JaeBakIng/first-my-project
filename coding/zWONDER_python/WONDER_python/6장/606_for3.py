mul = 1                     # 곱셈임으로 초기값은 1
for k in range(9, 0, -2) :  # 0부터 59까지 k에 대입
    print('%d ' % k, end = '')
    mul = mul * k
print('\nmul =', mul)
