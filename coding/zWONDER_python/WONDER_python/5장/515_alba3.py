perh = 12800
wtime = int(input('근무한 시간: '))
meal = wtime // 4

if wtime >= 40 :
    sum = (wtime * perh) + (meal * 10000)
    sum = sum + (sum * 0.1)
else :
    sum = (wtime * perh) + (meal * 9000)
    sum = sum + (sum * 0.02)
print('급여 =', sum)
