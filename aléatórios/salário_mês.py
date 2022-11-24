def valor_h(salário, horas_dia):
    horas_mês = horas_dia * 21
    valor_hora = salário / horas_mês 

    return valor_hora


# programa principal
sal = float(input('Digite seu salário: '))
horas = int(input('Digite a sua carga horária por dia: '))
resultado = valor_h(sal, horas)

print(f'Sua hora de trabalho custa R${resultado:.2f}.')
