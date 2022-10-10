"""Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro).
O programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""
cont50 = cont20 = cont10 = cont1 = 0
print('=' * 21)
print('{:^21}'.format("Didico's Bank"))
print('=' * 21)
valor = int(input('Que valor você deseja sacar? R$'))
total = valor
while total >= 50:
    total -= 50
    cont50 += 1
while total >= 20:
    total -= 20
    cont20 += 1
while total >= 10:
    total -= 10
    cont10 += 1
cont1 = total
if cont50 > 0:
    print(f'{cont50} cédulas de 50.')
if cont20 > 0:
    print(f'{cont20} cédulas de 20.')
if cont10 > 0:
    print(f'{cont10} cédulas de 10.')
if cont1 > 0:
    print(f'{cont1} cédulas de 1.')
