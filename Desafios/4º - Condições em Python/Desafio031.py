d = float(input('Qual é a distância da sua viagem (em km)? '))
if d <= 200:
    preco = d * 0.50
else:
    preco = d * 0.45
print('Sua viagem de {:.2f}km custará {:.2f}R$.'.format(d, preco))