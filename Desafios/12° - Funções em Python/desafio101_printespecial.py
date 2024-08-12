'''Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''
def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
#programa principal
escreva('Olá;')
escreva('Sou Diego;')
escreva('Bem-vindo ao meu portfólio!')