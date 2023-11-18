'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
exp = str(input('Digite sua expressão:'))
lista = []
for letra in exp:
    if letra == '(':
        lista.append('(')
    elif letra == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão está errada.')
