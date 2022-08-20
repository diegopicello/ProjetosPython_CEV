n = 1
totimpar = totpar = 0 #essa estrutura de "recebe" é válida e economiza linha, só cuidado.
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: #deve funcionar o teste somente se n for diferente de zero, pois este não é par nem ímpar, mas sim nulo!
        if n % 2 == 0:
            totpar += 1
        else:
            totimpar += 1
print('Foram digitados {} números pares e {} números ímpares'.format(totpar, totimpar))
print('Acabou.')
