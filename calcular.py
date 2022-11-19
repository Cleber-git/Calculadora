from time import sleep
while True:
    num = float(input('Digite o número desejado para o cálculo: '))
    if num == 0:
        break
    print('-'* 30)
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
        sleep(2)
    print('-'* 30)

print('fim do programa')
