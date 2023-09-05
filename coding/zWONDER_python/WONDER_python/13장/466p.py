file = open('test.txt', 'w')        # open(): 파일 준비
for k in range(1, 5) :
    file.write(str(k) + 'line write')   # write(): str만 가능
file.close()                        # close(): 파일 닫기
