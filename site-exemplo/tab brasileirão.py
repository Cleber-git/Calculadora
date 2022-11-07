def título(txt):
    tam = len(txt) + 16
    print('=' * tam)
    print(txt.center(tam))
    print('=' * tam)


# programa principal
times = ('Palmeiras', 'Corinthians', 'Fluminense', 'Athletico - PR', 'Flamengo', 'Internacional', 'Atlético - MG', 'Bragantino', 'Santos', 'São Paulo', 'Goiás', 'Bota Fogo','América - MG', 'Ceará', 'curitiba', 'Avaí', 'Cuiabá', 'Fortaleza', 'Atlético - GO', 'Juventude')

título('OS TIMES DO BRASILEIRÃO')
for k, v in enumerate(times):
    print(f'{k+1}º- {v.ljust(10)}')
print('=' * 30)

título('OS CINCO PRIMEIROS TIMES')
for k, v in enumerate(times[0:5]):
    print(f'{k+1}º- {v}')
print('=' * 30)

título('OS QUATRO ÚLTIMOS TIMES')
for k, v in enumerate(times[-1:-5:-1]):
    print(f'{k+1}º- {v}')
print('=' * 30)

título('POSIÇÃO DO FLAMENGO')
print(f'    -O flamengo ta na {times.index("Flamengo") + 1}ª posição.')
print()
título('Esse formulário está datado de 06 de agosto do ano de 2022 Às 14:21')
