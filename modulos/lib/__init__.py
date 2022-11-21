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


def WriteText(arquivo, text=''):
    text = str(input('Digite o texto: '))
    a = open(arquivo, 'at')
    a.write(text)


def ReadFile(arquivo):
        a = open(arquivo, 'rt')
        print(a.read())
        a.close()
