coupon = int(input('쿠폰 개수 입력: '))

if coupon >= 20 :
    print('\n여행가방')     # 쿠폰 20 이상: 여행가방
elif coupon >= 10 :
    print('\n다이어리')     # 쿠폰 20 미만 10 이상: 다이어리
elif coupon < 10 :
    print('\n커피 1잔')    # 쿠폰 10 미만: 커피 1잔

input()                 # 키보드를 눌러야만 종료
