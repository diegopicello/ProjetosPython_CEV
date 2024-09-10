'''Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.'''
def ficha(jog='<desconhecido>', g=0):
    print(f'O jogador {jog} fez {g} gols no campeonato.')

#programa principal
quer = 'S'
while True:
    jogador = str(input('Digite o nome do jogador: '))
    gols = str(input('Digite o número de gols: '))
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if jogador.strip() == '':
        ficha(g = gols)
    else:
        ficha(jogador, gols)
    quer = str(input('Quer continuar? [S/N]')).strip().upper()
    if quer not in 'Ss':
        break
