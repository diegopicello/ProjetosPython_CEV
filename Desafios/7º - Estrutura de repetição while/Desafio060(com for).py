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
    for c in range(c, 0, -1):
        fat = fat * n
        if n != 1:
            print('{} x '.format(n), end = '')
        else:
            print('{} = {}'.format(n, fat))
        n -= 1
print('O resultado do fatorial é {}.'.format(fat))
