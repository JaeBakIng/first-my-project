r = int(input('강우량을 입력하시오:'))
w = int(input('풍속을 입력하시오:'))

if r<100 and w<30 :
    print('현재강우량은 %dmm이고,풍속은 %dm/s입니다' % (r,w))
    print('비행상태:비행 가능')
if r>=100 and w>=30 :
    print('현재강우량은 %dmm이고,풍속은 %dm/s입니다' % (r,w))
    print('비행상태:비행 불가')
print('오류입니다')