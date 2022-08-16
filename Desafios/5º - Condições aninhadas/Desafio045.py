from random import randint
print('''Suas opções:
[ 0 ] PEDRA;
[ 1 ] PAPEL;
[ 2 ] TESOURA.''')
escolha = int(input('Qual é sua jogada? '))
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
escolhaMaquina = randint(0, 2)
if escolha == 0:
    if escolhaMaquina == 0:
        print('A máquina escolheu {} e você escolheu {}! Empate!'.format(opcoes[escolhaMaquina], opcoes[escolha]))
    elif escolhaMaquina == 1:
        print('A máquina escolheu {} e você escolheu {}! Que pena, você perdeu!'.format(opcoes[escolhaMaquina], opcoes[escolha]))
    else:
        print('A máquina escolheu {} e você escolheu {}! Você venceu!'.format(opcoes[escolhaMaquina], opcoes[escolha]))
elif escolha == 1:
    if escolhaMaquina == 0:
        print('A máquina escolheu {} e você escolheu {}! Você venceu!'.format(opcoes[escolhaMaquina], opcoes[escolha]))
    elif escolhaMaquina == 1:
        print('A máquina escolheu {} e você escolheu {}! Empate!'.format(opcoes[escolhaMaquina], opcoes[escolha]))
    else:
        print('A máquina escolheu {} e você escolheu {}! Que pena, você perdeu!'.format(opcoes[escolhaMaquina], opcoes[escolha]))
elif escolha == 2:
    if escolhaMaquina == 0:
        print('A máquina escolheu {} e você escolheu {}! Que pena, você perdeu!'.format(opcoes[escolhaMaquina], opcoes[escolha]))
    elif escolhaMaquina == 1:
        print('A máquina escolheu {} e você escolheu {}! Você venceu!'.format(opcoes[escolhaMaquina], opcoes[escolha]))
    else:
        print('A máquina escolheu {} e você escolheu {}! Empate!'.format(opcoes[escolhaMaquina], opcoes[escolha]))
else:
    print('Opção inválida! Tente novamente com os números citados acima.')



