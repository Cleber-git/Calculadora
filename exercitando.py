from random import randint
from time import sleep

def titulo(txt):
    tam = len(txt) + 4
    print('=' * tam)
    print(txt.center(tam))
    print('=' * tam)

máquina = ''

while True:
    
    aleatório = randint(1, 3)
    
    if aleatório == 1:
        máquina = 'Pedra'

    elif aleatório == 2:
        máquina = 'Papel'

    elif aleatório == 3:
        máquina = 'Tezoura'

    titulo('FAÇA SUA SORTE')

    while True:
        try:
            Jogador = str(input('Pedra, Papel ou Tezoura? ')).capitalize()

        except ValueError:
            print('Verifique se digitou corretamente o que foi pedido! ')

        except:
            print('\033[31mHouve algum erro, tente novamente! \033[m')
            continue

        else:
            break

    print('-=' * 30)
    print('Pedra...')
    sleep(1.5)
    print('Papel...')
    sleep(1.5)
    print('Tezoura!!!')

    print()
    print('-=' * 30)
    print(f'JOGADOR: {Jogador}')
    print(f'MÁQUINA: {máquina}')
    print(f'RESULTADO: ', end='')
    print('-=' * 30)
    if Jogador == máquina:
        print('\033[33mEmpate!\033[m')
        escolha = str(input('Deseja continuar? ')).strip().upper()[0]
        if escolha in 'S':
            continue
        else:
            break
    elif Jogador == 'Pedra' and máquina == 'Papel' or máquina == 'Tezoura' and Jogador == 'Papel' or máquina == 'Pedra' and Jogador == 'Tezoura':
        print('\033[31mMÁQUINA VENCE!\033[m')
        escolha = str(input('Deseja continuar? ')).strip().upper()[0]
        if escolha in 'S':
            continue
        else: 
            break
    else:
        print('\033[34mParabéns, Você venceu!!\033[m')
        break
    print()
print()    
print('-= '* 30)
print()    