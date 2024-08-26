'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, 
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''
def fatorial(num, show = True):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = {f}')
    return f


print(fatorial(6, show = True))
print(fatorial(4, show = False))
