with open('test.txt', 'r') as file :
    lines = file.read().splitlines()
    for k in range(len(lines)) :
        print(lines[k], end = '')
