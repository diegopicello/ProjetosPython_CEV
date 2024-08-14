'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
def maiornum(* valores):
    maior = 0
    print('=-' * 30)
    print('Analisando os valores apresentados:', flush = True)
    sleep(0.8)
    for num in valores:
        print(f'{num} ', end='', flush = True)
        sleep(0.8)
        if num == valores[0]:
            maior = valores[0]
        elif num > maior:
            maior = num
    if len(valores) > 1:
        print(f'Foram informados {len(valores)} valores ao todo;', flush = True)
        sleep(0.8)
        print(f'O maior valor foi {maior}', flush = True)
        sleep(0.8)
    elif len(valores) == 1:
        print(f'Apenas um valor foi informado, e este valor é {maior};', flush = True)
        sleep(0.8)
    else:
        print('Nenhum valor foi informado!', flush = True)
        sleep(0.8)


    #código:
maiornum(2, 9, 4, 5, 7, 1)
maiornum(4, 7, 0)
maiornum(1, 2)
maiornum(6)
maiornum()
    