tot = termos = num = 0
cont = False
while cont == False:
    num = float(input('Digite um número [999 para parar]: '))
    if num != 999:
        tot += num
        termos += 1
    else:
        cont = True
print('Você digitou {} números e a soma deles foi {}.'.format(termos, tot))
