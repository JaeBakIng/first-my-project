import time as t

file = open('text.txt','r')
while True :
    line = file.readline()
    if line == '' :
        break
    print(line , end='')
    t.sleep(0.5)
file.close()