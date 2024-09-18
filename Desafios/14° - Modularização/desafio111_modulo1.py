'''Crie um módulo chamado moeda.py que tenha as 
funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
import moeda
preço = float(input('Digite um preço: '))
print(f'A metade de {preço} é {moeda.metade(preço):.2f};')
print(f'O dobro de {preço} é {moeda.dobro(preço):.2f};')
print(f'Aumentando em 10%, teremos {moeda.aumentar(preço, 0.1):.2f}.')
