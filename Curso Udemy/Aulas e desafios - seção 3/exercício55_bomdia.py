"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite a hora (e apenas a hora!) atual: ')

try:
    horaint = int(hora)
    bomdia = 0 <= horaint <= 11
    boatarde = 12 <= horaint <= 17
    boanoite = 18 <= horaint <= 23
    if bomdia:
        print('Bom dia!')
    elif boatarde:
        print('Boa tarde!')
    elif boanoite:
        print('Boa Noite!')
    else:
        print('Não conheço essa hora.')

except (TypeError, ValueError):
    print('Erro! Digite apenas números inteiros.')
