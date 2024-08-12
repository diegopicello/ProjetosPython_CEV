'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
jogos = []
umjogo = []
print('=' * 30)
print('Jogo da Mega Sena')
print('=' * 30)
quantjogos = int(input('Quantos jogos você deseja gerar? '))
for c in range(1, quantjogos + 1):
    cont = 0
    while True:
        num = randint(1,60)
        if num not in umjogo:
            umjogo.append(num)
            cont += 1
        if cont == 6:
            break
    umjogo.sort()
    jogos.append(umjogo[:])
    print(f'Jogo {c}: {umjogo}')
    umjogo.clear()
print(jogos)
print('=' * 20)
print('Boa sorte!')
print('=' * 20)
