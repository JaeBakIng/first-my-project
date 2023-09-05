pay=10500
hour=18.5

total = int(pay*hour)
tax = int(total*0.03) #세금떄는함수
all = int(total-tax)

print()
print(total)
print(tax)
print(all)