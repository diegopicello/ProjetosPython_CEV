"""Calculadora com while"""

print('='*40)
print(f'{' Calculadora ':=^40}')
print('='*40)

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador: (+-*/) ')

    NUMEROSVALIDOS = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        NUMEROSVALIDOS = True

    except ValueError:
        NUMEROSVALIDOS = None
        print('Erro: um dos números digitados ou ambos são inválidos.')
        continue

    OPERADORES_PERMITIDOS = '+-*/'
    if operador not in OPERADORES_PERMITIDOS:
        print('Erro: o operador digitado é inválido.')
        continue
    if len(operador)>1:
        print('Erro: digite apenas um operador por vez.')
        continue

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float+num_2_float:.2f}')
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = {num_1_float-num_2_float:.2f}')
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = {num_1_float*num_2_float:.2f}')
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = {num_1_float/num_2_float:.2f}')
    else:
        print('Um erro passou batido.')

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')

    if sair:
        break
print('Obrigado e volte sempre.')
