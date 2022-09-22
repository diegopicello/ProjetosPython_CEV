fat = 1
n = int(input('Digite um número inteiro para calcular seu fatorial: '))
c = n
if n == 1:
    print('1 x 1 = 1')
elif n == 0:
    print('n! = n . (n - 1)! -> considerando n = 1:')
    print('1! = 1 . (1 - 1)!')
    print('1! = 1 . 0!')
    print('1 = 0!')
else:    
    while c > 0:
        fat = c * fat
        if c != 1:
            print('{} x '.format(c), end = '')
        else:
            print('{} = {}'.format(c, fat))
        c -= 1
print('o resultado é {}.'.format(fat))


