'''Crie um módulo chamado moeda.py que tenha as 
funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from utilidadesCeV import moedas
from utilidadesCeV import dados
preço = dados.leiaDinheiro('Digite um preço: ')
moedas.resumo(preço, 10, 20)
