'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
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
