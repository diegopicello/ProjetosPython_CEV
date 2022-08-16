dias = int(input('Quantos dias alugados? '))
kmrod = float(input('Quantos km rodados? '))
pdias = dias * 60
pkmrod = kmrod * 0.15
totp = pdias + pkmrod
print('O total a pagar é de R${:.2f}.'.format(totp))
