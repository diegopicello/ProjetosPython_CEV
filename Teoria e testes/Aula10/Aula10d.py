n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('Sua nota foi {:.2f}.'.format(m))
if m>7:
    print('Parabéns! Você passou!')
else:
    print('Que pena! Recuperação!')
