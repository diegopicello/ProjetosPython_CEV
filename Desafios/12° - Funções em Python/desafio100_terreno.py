'''Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''
def area(ba, alt):
    terreno = ba * alt
    print(f'A área de um terreno de {ba}m x {alt}m é de {terreno}m².')

#programa principal
print('Controle de terrenos')
print('='*30)
largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
area(largura, comprimento)
