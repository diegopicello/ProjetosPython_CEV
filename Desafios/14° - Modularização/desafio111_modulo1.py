'''Crie um módulo chamado moeda.py que tenha as 
funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
import moedas
preço = float(input('Digite um preço: '))
print(f'A metade de {moedas.moeda(preço)} é {moedas.metade(preço)};')
print(f'O dobro de {moedas.moeda(preço)} é {moedas.dobro(preço)};')
print(f'Aumentando em 10%, teremos {moedas.aumentar(preço, 0.1)}.')
