import os               # os.system() 이 있눈 모듈

order = 60
while order > 0 :
    print('%d 통닭 튀긴다' % order)
    order = order - 1
    os.system('cls')        # os.system() OS명령어 사용, cls 화면 지우기
print('60마리 다 튀김')

input()                 # 콘솔창이 사라지는 것 방지
