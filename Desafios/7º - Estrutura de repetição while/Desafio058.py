from random import choice
tottent = 1
print('Sou seu computador...')
print('Acabei de pensar num número entre 1 e 10.')
print('Será que você consegue adivinhar qual foi?')
seq = list(range(1, 11))
numcomput = choice(seq) #Poderia usar também a função randint()
numuser = int(input('Qual é o seu palpite? '))
while numuser != numcomput:
    tottent += 1
    if numuser > numcomput:
        numuser = int(input('Menos... Tente novamente! '))
    if numuser < numcomput:
        numuser = int(input('Mais... Tente novamente! '))        
print('Você acertou! o número que o computador escolheu foi {}!'.format(numcomput))
print('Você precisou de {} tentativas até acertar.'.format(tottent))
