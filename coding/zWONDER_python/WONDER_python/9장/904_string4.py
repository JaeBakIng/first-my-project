st1 = input('문자열 입력: ')

for k in range(len(st1) - 1, -1, -1) : # k값은 len(st1) - 1부터 0까지
    print(st1[k], end = '')
