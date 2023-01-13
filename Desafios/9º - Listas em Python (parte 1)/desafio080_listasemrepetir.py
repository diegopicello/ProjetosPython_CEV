'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.'''
lista = []
for c in range(1, 6):
    n = int(input('Digite um valor: '))
    if c == 1 or n > lista[-1]:
        lista.append(n)
        if c == 1:
            print('Valor adicionado no começo da lista.')
        else:
            print('Valor adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor {n} adicionado na posição {pos}.')
                break
            pos += 1
print('A lista final é: ')
for c, termos in enumerate(lista):
    if c < len(lista) - 1:
        print(f'Número {termos} na posição {c}, ', end = '')
    else:
        print(f'Número {termos} na posição {c}. ')