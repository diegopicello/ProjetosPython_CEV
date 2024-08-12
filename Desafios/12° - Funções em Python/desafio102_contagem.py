'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
a) de 1 até 10, de 1 em 1                                                                                                                                              
b) de 10 até 0, de 2 em 2             
c) uma contagem personalizada'''
from time import sleep
def contador(i, f, p):
    if i > f:
        if p > 0:
            p = -p
    else:
        if p < 0:
            p = -p
    print('='*32)
    print(f'Contagem de {i} a {f} de {p} em {p}:')
    sleep(1.3)
    for c in range(i, f+1, p):
        sleep(0.6)
        print(f'{c} ', end='', flush=True)
    print('Fim!')


#código:
contador(1, 10, 1)
contador(10, 0, 2)
print('='*32)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
print('='*32)
