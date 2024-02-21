'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.                                                                                                  
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.'''
matriz = [[], [], []]
somapares = 0
somaterceira = 0
for c in range(1,4):
    for i in range(1,4):
        valor = int(input(f'Digite um valor para a posição{c}, {i}: '))
        if valor % 2 == 0:
            somapares += valor
        if c == 2:
            if i == 1:
                maior2 = valor
            elif valor >= maior2:
                maior2 = valor
        matriz[c-1].append(valor)
for num in matriz[2]:
    somaterceira += num
print('=-' * 20)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('=-' * 20)
print(f'A soma de todos os valores pares é {somapares};')
print(f'A soma dos valores da terceira coluna resulta em {somaterceira};')
print(f'O maior valor digitado na segunda linha foi {maior2}.')
