din = float(input('quantos reais você quer usar? R$'))
dol = float(input('quanto está o dólar hoje? $'))
compr = din/dol
print('com R${} (reais), você pode comprar ${:.3} (dólares)'.format(din, compr))
