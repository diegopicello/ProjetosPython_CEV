'''Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
jogador = {}
gols = []
time = []
totalgols = 0
c1 = 0
qual = 0
quer = 'S'
while True:
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input('Digite o total de partidas: '))
    for c in range (0, partidas):
        gol = int(input(f'Gols na {c+1}ª partida: '))
        gols.append(gol)
        totalgols += gol
    jogador['gols'] = gols[:]
    jogador['total'] = totalgols
    jogador['código'] = c1
    c1 += 1
    time.append(jogador.copy())
    gols.clear()
    while True:
        quer = str(input('Quer continuar? [S/N]: ')).strip()
        if quer not in 'SsNn':
            print('Insira apenas caracteres válidos!')
        else:
            break
    if quer in 'Nn':
        break
print(time)
print('Código      Nome         Gols            Total')
for c in range(0, len(time)):
    print(f'{c:<12}', end='')
    print(f'{str(time[c]["Nome"]):<12}', end=' ')
    print(f'{str(time[c]["gols"]):<12}', end=' ')
    print(f'{str(time[c]["total"]):<10}')
while True:
    while True:
        qual = int(input('Qual jogador deseja mostrar? (999 para parar) '))
        if qual not in range(0, len(time)):
            print(f'Erro! O jogador de código {qual} não existe.')
        else:
            break
    if qual == 999:
        break
    print(f'Levantamento do jogador {time[qual]["Nome"]}:')
    for i in range(0, len(time[qual]["gols"])):
        if i < len(time[qual]["gols"]) - 1:
            print(f'No {i+1}º jogo marcou {time[qual]["gols"][i]} gols;')
        else:
            print(f'E {time[qual]["gols"][i]} gols na última partida.')
