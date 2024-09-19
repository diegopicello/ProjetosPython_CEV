'''Crie um módulo chamado moeda.py que tenha as 
funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
import moeda
preço = float(input('Digite um preço: '))
print(f'A metade de {preço} é {moeda.moeda(moeda.metade(preço))};')
print(f'O dobro de {preço} é {moeda.moeda(moeda.dobro(preço))};')
print(f'Aumentando em 10%, teremos {moeda.moeda(moeda.aumentar(preço, 0.1))}.')
