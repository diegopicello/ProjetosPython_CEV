'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1,6), 
        'jogador 2': randint(1,6),
        'jogador 3': randint(1,6),
        'jogador 4': randint(1,6)}
ranking = list()
print(10*'=',end='')
print(' Valores sorteados ',end='')
print(10*'=')
for k, v in jogo.items():
    if k not in 'Jogador 4':
        print(f'{k} tirou {v} no dado;')
    else:
        print(f'{k} tirou {v} no dado.')
    sleep(1.3)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
sleep(1.3)
print(10*'=',end='')
print(' Resultados ',end='')
print(10*'=')
sleep(1.3)
for c in range(0, len(ranking)):
    if c != len(ranking)-1:
        print(f'O {ranking[c][0]} foi o {c+1}º colocado ao tirar {ranking[c][1]} no dado;')
    else:
        print(f'O {ranking[c][0]} foi o {c+1}º colocado ao tirar {ranking[c][1]} no dado.')
    sleep(1.3)
