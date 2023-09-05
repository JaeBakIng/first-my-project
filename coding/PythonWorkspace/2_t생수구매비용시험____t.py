#한팩에 15개 10000원 낱개는 1개 900원

person=int(input('MT사람의 수:'))
onep=int(input('1인당 생수 개수:'))

pack=(person*onep)//15 #사람의수가 n명일때 몇팩을 사야하는지의 함수
bottle=(person*onep)%15#사람의수가 n명하고 조금 남을때 낱개몇개를 사야하는지의 함수
total=(pack*10000)+(bottle*900) #총 물구매에 사용된 돈
print()
print('필요한 생수 개수%d개'% (person*onep))
print('생수 팩 구매량%d개, %d원'%(pack,pack*10000))
print('생수 낱개 구메량%d개, %d원'%(onep,onep*900))
print('생수총 구매비용 %d원'%(total))