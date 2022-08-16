from random import choice
from time import sleep
print('-=-' * 13)
print('Pensarei em um número, tente adivinhar!')
print('-=-' * 13)
seq = [0,1,2,3,4,5]
numComput = choice(seq)
numUser = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if numComput == numUser:
    print('Parabéns, você acertou!')
else:
    print('Que pena!, você errou! Eu pensei em {} e você em {}'.format(numComput, numUser))
    




