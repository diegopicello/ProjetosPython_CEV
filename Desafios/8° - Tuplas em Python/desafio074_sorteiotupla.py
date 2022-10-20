'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

import random

n1 = random.randint(0, 10)
maior = menor = n1
n2 = random.randint(0, 10)
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
n3 = random.randint(0, 10)
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
n4 = random.randint(0, 10)
if n4 > maior:
    maior = n4
if n4 < menor:
    menor = n4
n5 = random.randint(0, 10)
if n5 > maior:
    maior = n5
if n5 < menor:
    menor = n5
todos = (n1, n2, n3, n4, n5)
print(todos)
print(f'O maior foi {maior} e o menor foi {menor}.')
