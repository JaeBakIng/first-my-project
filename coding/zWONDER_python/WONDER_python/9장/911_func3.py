st1 = ' 과자 먹자 '

print('center <%s>' % st1.center(20))       # 20칸 만든 후 중앙 정렬
print('center <%s>' % st1.center(20, '*'))  # 중앙 정렬: 빈칸 별표
print('rjust <%s>' % st1.rjust(20))
print('ljust <%s>' % st1.ljust(20))

print('strip <%s>' % st1.strip())
print('rstrip <%s>' % st1.rstrip())
print('lstrip <%s>' % st1.lstrip())
