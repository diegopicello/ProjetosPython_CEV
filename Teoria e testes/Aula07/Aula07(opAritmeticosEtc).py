n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
ad = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
Di = n1 // n2
p = n1 ** n2
print('a adição vale {}, a subtração vale {}, a multiplicação vale {},'.format(ad, s, m), end=' ')
print('a divisão vale {:.4}, a divisão inteira vale {} e a potenciação vale {}.'.format(d, Di, p))

