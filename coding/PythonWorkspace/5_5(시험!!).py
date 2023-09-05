up, low, dig, pct = 0, 0, 0, 0

pswd = input('암호 생성:')
if pswd.isalnum() == False :
    pct = 1

for k in pswd :
    if k.isupper() : up=1
    elif k.islower() : low = 1
    elif k.isdigit() : dig = 1

if up+low+dig+pct >= 3 :
    print('사용가능')
else :
    print('!사용불가!')