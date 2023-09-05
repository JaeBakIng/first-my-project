st1 = '과자먹자'

print('count >', st1.count('자'))
print('index >', st1.index('자'))            # 찾는 글자 없으면 에러
print('rindex >', st1.rindex('자'))          # 찾는 글자 없으면 에러
print('find >', st1.find('자'))              # 찾는 글자 없으면 -1
print('find >', st1.find('짜'))              # 찾는 글자 없으면 –1
print('rfind >', st1.rfind('자'))            # 찾는 글자 없으면 -1

print('startswith >', st1.startswith('자'))  # 자로 시작하면 True
print('endswith >', st1.endswith('자'))      # 자로 끝나면 True
