from lib import *

while True:
    linha('MENU DE CADASTRO')
    menu(['Criar arquivo','Cadastrar uma pessoa', 'Ver lista', 'Sair do sistema'])
    print('-'*20)
    escolha = int(input('Digite o número correspondente ao que deseja fazer> '))
    if escolha == 4:
        break
    arq = str(input('Digite o nome do arquivo com sua extensão> '))
    if escolha == 1:
        CreateFile(arq)
    elif escolha == 2:
        WriteText(arq)
    elif escolha == 3:
        ReadFile(arq)
    else:
        print('\033[31mERRO! Digite um valor válido.\033[m')
linha('SAINDO, ATÉ LOGO...')
