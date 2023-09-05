import random as r
import time as t

slot=[0,0,0]

for s in range (3) : 
    for k in range (3) :
        slot[k] = r.randrange(7,9)
        print('%d ' % slot[k] , end='')
        t.sleep(2)


    if slot[0]+slot[1]+slot[2] == 21:
        print('\n잭팟')

        
    else :
        print('\n까비 ㅋ\n')