arr = [0,0,0]

arr[0] = int(input('첫 번째 값:'))
arr[1] = int(input('두 번째 값:'))
arr[2] = int(input('세 번째 값:'))

sum = arr[0]+arr[1]+arr[2]
avr = sum / 3
print()
print('합=%d , 평균=%d' % (sum,avr))