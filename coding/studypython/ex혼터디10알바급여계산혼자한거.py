wtime = int(input('근무한 시간: '))

perh=12800
meal = wtime // 4

total1 = (perh*wtime) + (meal*9000)
total2 = (perh*wtime) + (meal*10000)

if wtime>=40 :
    print('급여 = %d' % (total2 + total2*0.1))

else :
    print('급여 = %d' % (total1 + total1*0.02))