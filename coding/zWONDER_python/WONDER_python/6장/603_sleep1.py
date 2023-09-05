import os
import time             # time.sleep()이 있는 모듈

order = 60
while order > 0 :
    print('%d 통닭 튀긴다' % order)
    order = order - 1
    time.sleep(1)           # time.sleep(1): 1초간 멈춤
    os.system('cls')
print('60마리 다 튀김')

input()
