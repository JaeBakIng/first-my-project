wlist = ['1line write\n','2line write\n','3line write\n']
file = open('text.txt','w')
file.writelines(wlist) #리스트 값을 한줄씩 쓰는함수
file.close()