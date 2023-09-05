coupon = int(input('쿠폰 개수 입력: '))

if coupon >= 20 :
    print('\n여행가방') # 쿠폰 >= 20: 여행가방
if coupon >= 10 :
    print('\n다이어리') # 쿠폰 >= 10: 다이어리
if coupon < 10 :
    print('\n커피 1잔') # 쿠폰 < 10: 커피 1잔
