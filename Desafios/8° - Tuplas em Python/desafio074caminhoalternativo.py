from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
        randint(1, 10), randint(1, 10),)
print('Sorteei os seguintes números: ', end = '')
for numero in numeros:
    print(numero, end = ' ')
print(f'\nO maior valor sorteado foi {max(numeros)}.')#\n faz pular a linha
print(f'O menor valor sorteado foi {min(numeros)}.')
