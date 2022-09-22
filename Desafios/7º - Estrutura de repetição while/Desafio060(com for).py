n = int(input('Digite um número inteiro não negativo: '))
f = 1
print('{}! = '.format(n), end = '')
for c in range(n, 0, -1):
    print('{}'.format(n), end = '')
    if n > 1:
        print(' x ', end = '')
    else:
        print(' = ', end = '')
    f *= n
    n -= 1
print(f)