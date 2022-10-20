precos = ('Lápis', 1.75,
'Borracha', 2,
'Caderno', 15.90,
'Estojo', 25,
'Transferidor', 4.2,
'Compasso', 9.99,
'Mochila', 120.32,
'Canetas', 22.30,
'Livro', 34.90,)
print(30 * '-')
print('LISTAGEM DE PREÇOS'.center(30))
print(30 * '-')
for pos in range(0, len(precos)):
    if pos % 2 == 0:
        print(f'{precos[pos]:.<22}', end = '')
    else:
        print(f'R${precos[pos]:>6.2f}')
