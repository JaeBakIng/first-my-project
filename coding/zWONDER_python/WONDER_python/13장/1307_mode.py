file = open('test.txt', 'a')    # a: 기존 파일에 이어쓰기
file.write(input('입력: '))     # 키보드에서 입력은 write()
file.close()                    # close(): 파일 닫기
