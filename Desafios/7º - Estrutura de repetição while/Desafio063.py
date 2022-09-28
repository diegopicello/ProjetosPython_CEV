a1 = 0
a2 = 1
a0 = 0
print('-' * 22)
print('Sequência de Fibonacci')
print('-' * 22)
n = int(input('Quantos termos você deseja mostrar? '))
if n == 0:
    print('Fim da execução com nenhum termo mostrado.')
elif n == 1:
    print('0 -> FIM')
else:
    c = n
    print('{} -> {} -> '.format(a1, a2), end = '')
    for c in range(3, n+2):
        if c != n + 1:
            a0 = a1 + a2
            a1 = a2
            a2 = a0
            print('{} -> '.format(a0), end = '')
        else:
            print('FIM')
