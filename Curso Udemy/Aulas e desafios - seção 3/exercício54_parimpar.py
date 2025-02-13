"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número INTEIRO: ')

try:
    numint = int(num)
    par = numint % 2 == 0

    if par:
        print(
            f'O número {numint} é par.'
            )
    else:
        print(
            f'O numéro {numint} é ímpar.'
            )

except (TypeError, ValueError):
    print(
        'O valor digitado não é um número inteiro!'
        )
