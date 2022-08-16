'''ca = float(input('Digite um cateto: '))
co = float(input('Digite o outro: '))
hip = (co**2 + ca**2)**(1/2)
print('Sua hipotenusa vai medir {:.f}.'.format(hip))'''

from math import hypot
ca = float(input('Digite um cateto: '))
co = float(input('Digite o outro cateto: '))
print('Sua hipotenusa vai medir {:.2f}.'.format(hypot(ca, co)))

