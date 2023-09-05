arr = [0, 0, 0]         # 리스트도 사용하기 전에 초기화 해야 한다
arr[0] = int(input('첫 번째 값: '))
arr[1] = int(input('두 번째 값: '))
arr[2] = int(input('세 번째 값: '))

sum = arr[0] + arr[1] + arr[2]
ave = sum / 3
print('합 = %d, 평균 = %.2f' % (sum, ave))
