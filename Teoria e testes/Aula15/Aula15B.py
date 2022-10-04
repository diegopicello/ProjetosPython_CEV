n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n #ele está somando o 999 mesmo esse sendo apenas um flag!
#gambiarra possível: colocar s -= 999 após finalizar a repetição. Como resolver? parte C!
print('A soma vale {}'.format(s))
