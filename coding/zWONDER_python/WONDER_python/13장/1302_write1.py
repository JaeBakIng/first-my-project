file = open('test.txt', 'w')
for k in range(1, 5) :
    file.write(str(k) + 'line write' + '\n')
file.close()
