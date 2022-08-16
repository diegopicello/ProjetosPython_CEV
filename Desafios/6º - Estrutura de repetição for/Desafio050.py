soma = 0
totC = 0
for c in range(1,7):
    n = float(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        totC += 1
if totC == 1: 
    print('Dos 6 números, apenas 1 é par e este vale {}.'.format(soma))
elif totC == 0:
    print('Nenhum número informado é par. Portanto, a soma vale 0')
else:
    print('Dos 6 números, {} são pares e a soma destes é igual a {}.'.format(totC, soma))


