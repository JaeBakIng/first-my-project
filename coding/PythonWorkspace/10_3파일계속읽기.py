file = open('text.txt','r')
while True :
    line = file.readline()
    if line == '' :
        break
    print(line,end='')
file.close()

