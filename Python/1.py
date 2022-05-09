number = int(input('팩토리얼을 구할 정수 입력:'))
x = factorial = 1

for x in range(1,number+1):
    factorial *=x
print('%d ! = %d'%(number, factorial))
