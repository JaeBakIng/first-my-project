wtime = int(input('근무한 시간:'))
perh=12800
meal = wtime // 4

if wtime >= 40 :
    total = (perh * wtime) + (meal * 10000)
    total = total + (total * 0.1)
else :
    total = (perh * wtime) + (meal * 9000)
    total = total + (total *0.02)

print()
print('급여= %d' % total)