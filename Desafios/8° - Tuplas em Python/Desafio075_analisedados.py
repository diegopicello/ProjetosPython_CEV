'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9;
B) Em que posição foi digitado o primeiro valor 3;
C) Quais foram os números pares.'''
totpar = 0
numeros = ((int(input('Digite um número: '))), (int(input('Digite outro número: '))),
    (int(input('Digite mais um número: '))), (int(input('Digite o último número: '))))
print('Você digitou os números: ', end = '')
for numero in numeros:
    print(numero, end = ' ')
vezes9 = numeros.count(9)
if vezes9 == 0:
    print('\nO valor 9 não foi digitado.')
elif vezes9 == 1:
    print('\n O valor 9 foi digitado uma vez.')
else:
    print(f'\n O valor 9 foi digitado {vezes9} vezes')
if 3 in numeros:
    posicao3 = numeros.index(3) + 1
    print(f'O primeiro valor 3 aparece na {posicao3}º posição.')
else:
    print('O valor 3 não foi digitado.')
for c in range(0, 4):
    if numeros[c] % 2 == 0:
        totpar += 1
print(f'Ao todo, há {totpar} valores pares.')
