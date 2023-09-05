wlist = ['1line write\n', '2line write\n', '3line write\n']
file = open('test.txt', 'w')
file.writelines(wlist)
file.close()
