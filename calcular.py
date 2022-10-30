from time import sleep
num = int(input('Digite o número desejado para o cálculo: '))
print('-'* 30)
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')
    sleep(1.5)
print('-'* 30)

print('fim do progranma')
