'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
from time import sleep
jogador = {}
gols = []
totalgols = 0
jogador['Nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input('Digite o total de partidas: '))
for c in range (0, partidas):
    gol = int(input(f'Gols na {c+1}ª partida: '))
    gols.append(gol)
    totalgols += gol
jogador['gols'] = gols
jogador['total'] = totalgols
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas e marcou {jogador["total"]} gols.')
sleep(1.2)
for c in range(0, partidas):
    if c != partidas - 1:
        print(f'Marcou {gols[c]} gol na {c+1}ª partida;')
    else:
        print(f'E marcou {gols[c]} gol na última partida.')
    sleep(1.2)
