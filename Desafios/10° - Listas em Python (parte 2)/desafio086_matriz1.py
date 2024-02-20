'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.'''
matriz = [[], [], []]
for c in range(1,4):
    for i in range(1,4):
        valor = int(input(f'Digite um valor para a posição{c}, {i}: '))
        matriz[c-1].append(valor)
print(matriz[0])
print(matriz[1])
print(matriz[2])
