phour = 12800
wtime = int(input('근무한 시간:'))
meal = wtime // 4

if wtime >= 40 :
    total=(phour*wtime)+ (meal*10000)
    total=total+(total*0.1)
else :
    total=(phour*wtime) + (meal*9000)
    total=total+(total*0.02)
print()
print('근무한 시간=%d'%(wtime))
print('급여=%.1f'%(total))