'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.                                                                                                                
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
pessoas = []
dados = []
maiorpeso = menorpeso = 0
continuar = 'Ss'
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] >= maiorpeso:
            maiorpeso = dados[1]
        elif dados[1] <= menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = input('Quer continuar? [S/N] ').strip()
    if continuar not in 'Ss':
        break
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorpeso}, o qual foi medido em:', end = ' ')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'{p[0]} ')
print(f'O menor peso foi de {menorpeso}, o qual foi medido em:', end = ' ')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'{p[0]} ')
