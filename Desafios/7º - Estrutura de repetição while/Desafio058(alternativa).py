from random import randint
computador = randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar num número entre 1 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False #fica com false pois você ainda não acertou.
tottent = 0
while not acertou: #enquanto você não acertou (poderia ser "while acertou == False").
    jogador = int(input('Qual é o seu palpite? '))
    tottent += 1
    if jogador == computador:
        acertou = True #quando acertou é verdadeiro (você acertou), acaba o "while".
    else:
        if jogador < computador:
            print('Mais... Tente novamente! ')
        elif jogador > computador:
            print('Menos... Tente novamente! ')
print('Você acertou! o número que o computador escolheu foi {}!'.format(computador))
print('Você precisou de {} tentativas até acertar.'.format(tottent))
