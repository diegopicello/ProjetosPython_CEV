'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
<<<<<<< HEAD
pesquerda = 0
pdireita = 0
expressao = str(input('Digite uma expressão matemática: '))
listaexp = expressao.split()
for c in enumerate(listaexp):
    if [c] == '(':
        pesquerda += 1
    if [c] == ')':
        pdireita += 1
if pesquerda == pdireita:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida.')
=======
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
>>>>>>> e79cec3cce63a0e887496775a85fa76e5d233f8f
