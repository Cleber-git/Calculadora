def FileFind(arquivo):
    try:
        a = open(arquivo, 'wt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CreateFile(arquivo):
    if not FileFind(arquivo):
        a = open(arquivo, 'wt+')
        a.close()
        print('\033[34mArquivo criado!\033[m')
    else:
        print('O arquivo já existe!')


def WriteText(arquivo):
    nome = str(input('Digite o nome> '))
    idade = int(input('Digite a idade> '))
    a = open(arquivo, 'at')
    a.write(f'{nome:<10}{idade:>10}\n')


def ReadFile(arquivo):
        a = open(arquivo, 'rt')
        print(a.read())
        a.close()

def menu(txt):
    for k, v in enumerate(txt):
        print(f'\033[32m{k+1}-\033[m \033[34m{v}\033[m')

def linha(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(txt.center(tam))
    print('-' * tam)
