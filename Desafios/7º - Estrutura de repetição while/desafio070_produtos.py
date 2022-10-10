"""Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""
c = total = c1000 = maisbarato = 0
print('=' * 21)
print("    Didico's shop")
print('=' * 21)
while True:
    c += 1
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        c1000 += 1
    if c == 1:
        maisbarato = preco
        nomemaisbarato = produto
    else:
        if preco < maisbarato:
            maisbarato = preco
            nomemaisbarato = produto
    escolha = ' '
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if escolha in 'Nn':
        break
print('{:=^40}'.format('Fim do programa'))
print(f'O total da compra foi de R${total:.2f}')
if c1000 == 1:
    print('Há um produto custando mais de R$1000.00.')
elif c1000 == 0:
    print('Não há produtos custando mais de R$1000.00.')
else:
    print(f'Ao todo, há {c1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomemaisbarato} custando R${maisbarato}.')
