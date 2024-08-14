'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista. 
A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
def sorteio(lst):
    print('Sorteando os valores da lista:')
    for c in range(0, 5):
        num = randint(0, 20)
        lst.append(num)
        print(f'{lst[c]}, ', end='')
        c += 1
    print('Pronto!')
def somapar(lst):
    soma = 0
    for valor in lst:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lst}, temos o valor {soma}.')

#código
numeros = []
sorteio(numeros)
somapar(numeros)
