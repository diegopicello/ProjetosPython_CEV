'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
precos = ('Lápis', '1.75',
'Borracha', '2.00',
'Caderno', '15.90',
'Estojo', '25.0',
'Transferidor', '4.20',
'Compasso', '9.99',
'Mochila', '120.32',
'Canetas', '22.30',
'Livro', '34.90',)
print(20 * '=-')
print('LISTAGEM DE PREÇOS'.center(40))
print(20 * '=-')
for c in range(0, len(precos), 2):
    print(precos[c].ljust(27, '.') + 'R$' + precos[c+1].rjust(11))
print(20 * '=-')
