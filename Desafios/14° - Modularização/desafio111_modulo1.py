'''Crie um módulo chamado moeda.py que tenha as 
funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
import moedas
preço = float(input('Digite um preço: '))
print(f'A metade de {preço} é {moedas.moeda(moedas.metade(preço))};')
print(f'O dobro de {preço} é {moedas.moeda(moedas.dobro(preço))};')
print(f'Aumentando em 10%, teremos {moedas.moeda(moedas.aumentar(preço, 0.1))}.')
